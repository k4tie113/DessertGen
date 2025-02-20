import pandas as pd

# Load the full dataset
df = pd.read_csv("filtered_data.csv")

# Sample a smaller subset (10,000 recipes or all available)
df_sampled = df.sample(n=min(10000, len(df)), random_state=42)

# Save the sampled dataset
df_sampled.to_csv("filtered_data_sampled.csv", index=False)

print(f"Original dataset size: {len(df)}")
print(f"Sampled dataset size: {len(df_sampled)} (saved as 'filtered_data_sampled.csv')")
