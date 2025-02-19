import pandas as pd

# Load the dataset
df = pd.read_csv("data/dessert_recipes.csv")  # Make sure this file exists

# Define dessert-related keywords
dessert_keywords = [
    "dessert", "cake", "cookie", "brownie", "pie", "pudding", "ice cream",
    "tart", "cupcake", "cheesecake", "muffin", "candy", "sweet", "frosting"
]

# Define cultural keywords to filter out (but save separately)
cultural_keywords = [
    "indian", "chinese", "asian", "mexican", "french", "italian", "japanese", "korean",
    "thai", "turkish", "middle eastern", "greek", "filipino", "vietnamese", "caribbean"
]

# Step 1: Filter for only desserts (if needed)
df_desserts = df[
    df["tags"].str.contains("|".join(dessert_keywords), case=False, na=False) |
    df["name"].str.contains("|".join(dessert_keywords), case=False, na=False)
]

# Step 2: Separate American vs. Cultural desserts
df_american_desserts = df_desserts[
    ~df_desserts["tags"].str.contains("|".join(cultural_keywords), case=False, na=False)
]
df_cultural_desserts = df_desserts[
    df_desserts["tags"].str.contains("|".join(cultural_keywords), case=False, na=False)
]

# Step 3: Downsample American desserts to 25%
df_sampled = df_american_desserts.sample(frac=0.25, random_state=42)

# Save the final datasets
df_sampled.to_csv("recipes.csv", index=False)  # Final dataset
df_cultural_desserts.to_csv("cultural_desserts.csv", index=False)  # Saved for later

print(f"Original dessert count: {len(df_desserts)}")
print(f"American desserts kept: {len(df_sampled)} (25% sample)")
print(f"Cultural desserts saved separately: {len(df_cultural_desserts)}")
print("Filtering complete! Final dataset saved as 'recipes.csv'.")
