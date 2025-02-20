import pandas as pd
from extract import find_best_matching_recipe

# Load the dataset (update with your actual file path)
df = pd.read_csv("../data/filtered_data_sampled.csv")

# Load ingredient substitutions
substitutions = pd.read_csv("../data/ingredient_substitutions.csv").set_index("ingredient")["substitutes"].apply(lambda x: x.split(", ")).to_dict()

def main():
    print("Welcome to the Dessert Recipe Matcher! 🍰")
    
    # Get user ingredients input
    user_ingredients = input("Enter ingredients you have (comma-separated): ").strip().split(", ")
    
    # Get user time input
    user_time = input("Enter maximum cooking time (e.g., '30 minutes'): ").strip()

    # Find the best matching recipe
    best_recipe = find_best_matching_recipe(user_ingredients, user_time, df, substitutions)

    # Display the recipe
    print("\n🎉 Here's the best matching recipe for you!\n")
    print(best_recipe)

if __name__ == "__main__":
    main()
