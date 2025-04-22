import pandas as pd
import random
from faker import Faker

fake = Faker()

# Load the CSV
df = pd.read_csv(
    r"C:\Users\user\OneDrive\Desktop\Python Minis\HR Project\data_upgradation\user_data.csv")

# Number of rows to update (e.g., 5)
num_updates = 5

# Randomly choose row indices to update
rows_to_update = random.sample(range(len(df)), num_updates)

for i in rows_to_update:
    df.at[i, 'age'] = random.randint(18, 60)
    df.at[i, 'city'] = fake.city()

# Save to the same CSV or a new file
df.to_csv("user_data_updated.csv", index=False)

print("✅ CSV file updated and saved as 'user_data_updated.csv'")
