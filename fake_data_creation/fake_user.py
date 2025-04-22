import pandas as pd
from faker import Faker
import random

fake = Faker()

num_listing = 20

data = []
for _ in range(num_listing):
    data.append({
        "id": fake.unique.random_int(min=1, max=9999),
        "name": fake.name(),
        "email": fake.email(),
        "age": fake.random_int(18, 60),
        "city": fake.city(),
        "created_at": fake.date_this_year()
    })

    df = pd.DataFrame(data)
    df.to_csv("user_data.csv", index=False)

print("Random user_data.csv created successfully")
