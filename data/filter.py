import pandas as pd

# Load the dataset
df = pd.read_csv("recipes.csv")  # Make sure this file exists

# Define dessert-related keywords
dessert_keywords = [
    "dessert", "cake", "cookie", "brownie", "pie", "pudding", "ice cream",
    "tart", "cupcake", "cheesecake", "muffin", "candy", "sweet", "frosting"
]

# Step 1: Filter for only desserts (if needed)
df_desserts = df[
    df["tags"].str.contains("|".join(dessert_keywords), case=False, na=False) |
    df["name"].str.contains("|".join(dessert_keywords), case=False, na=False)
]

# Step 3: Downsample American desserts to 25%
df_sampled = df_desserts.sample(frac=0.25, random_state=42)

# Save the final datasets
df_sampled.to_csv("filtered_data.csv", index=False)  # Final dataset

print(f"Original dessert count: {len(df_desserts)}")
print(f"Desserts kept: {len(df_sampled)} (25% sample)")

