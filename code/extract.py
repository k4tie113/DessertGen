import pandas as pd
import ast
import re

def extract_time_from_steps(steps):
    """Extracts estimated time from recipe steps using regex."""
    time_pattern = re.findall(r'(\d+)\s*(?:hour|hr|minute|min)', steps, re.IGNORECASE)
    if time_pattern:
        total_minutes = sum([int(t) * 60 if 'hour' in steps.lower() else int(t) for t in time_pattern])
        return total_minutes
    return None  # Return None if no time is found

def apply_ingredient_substitutions(user_ingredients, substitution_df):
    """Expands user ingredients list with possible substitutes."""
    expanded_ingredients = set(user_ingredients)
    for ingredient in user_ingredients:
        substitutes = substitution_df.get(ingredient, [])
        expanded_ingredients.update(substitutes)
    return list(expanded_ingredients)

def format_recipe(recipe):
    """Formats the recipe output for readability."""
    formatted_recipe = f"""
## {recipe['name']}

### Ingredients:
""" + "\n".join([f"- {ingredient}" for ingredient in ast.literal_eval(recipe['ingredients'])]) + "\n" + """
### Instructions:
""" + "\n".join([f"{i+1}. {step}" for i, step in enumerate(ast.literal_eval(recipe['steps']))]) + "\n" + f"""
### Estimated Time:
{recipe['estimated_time']} minutes
"""
    return formatted_recipe

def find_best_matching_recipe(user_ingredients, user_time, df, substitution_df):
    def count_matching_ingredients(recipe_ingredients, user_ingredients):
        """Count how many user ingredients match the recipe ingredients."""
        try:
            recipe_set = set(ast.literal_eval(recipe_ingredients))  # Convert string list to actual Python list
            user_set = set(user_ingredients)
            return len(recipe_set.intersection(user_set))
        except (SyntaxError, ValueError):
            return 0  # Handle any parsing errors gracefully

    def time_difference(recipe_time, user_time):
        """Calculate the absolute difference between user time and recipe time."""
        try:
            return abs(recipe_time - int(user_time.split()[0]))
        except (ValueError, AttributeError, TypeError):
            return float('inf')  # If parsing fails, set a high difference

    # Expand ingredients with possible substitutes
    expanded_ingredients = apply_ingredient_substitutions(user_ingredients, substitution_df)

    # Extract estimated time for each recipe
    df["estimated_time"] = df["steps"].apply(lambda x: extract_time_from_steps(str(x)))

    # Apply matching functions to all recipes
    df["matching_ingredients"] = df["ingredients"].apply(lambda x: count_matching_ingredients(x, expanded_ingredients))
    df["time_difference"] = df["estimated_time"].apply(lambda x: time_difference(x, user_time))

    # Sort by lowest time difference first, then highest matching ingredients
    best_match = df.sort_values(by=["time_difference", "matching_ingredients"], ascending=[True, False]).iloc[0]

    # Format and return the best recipe
    return format_recipe(best_match)


