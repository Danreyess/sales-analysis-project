import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Parámetros
num_rows = 2000

products = [
    ("Laptop Pro 15", "Electronics"),
    ("Laptop Air 13", "Electronics"),
    ("Wireless Mouse", "Electronics"),
    ("Office Chair", "Furniture"),
    ("Standing Desk", "Furniture"),
    ("Water Bottle", "Accessories"),
    ("Noise Cancelling Headphones", "Electronics"),
    ("Backpack Travel", "Accessories"),
    ("Coffee Maker", "Home"),
    ("Smartwatch", "Electronics"),
]

payment_methods = ["Credit Card", "Debit Card", "PayPal", "Apple Pay", "Cash"]
cities = ["Toronto", "Vancouver", "Mexico City", "New York", "Chicago", "Shanghai"]

data = []

start_date = datetime(2023, 1, 1)

for i in range(num_rows):
    product, category = random.choice(products)
    price = round(random.uniform(10, 2500), 2)
    quantity = random.randint(1, 4)
    date = start_date + timedelta(days=random.randint(0, 700))

    row = {
        "order_id": fake.uuid4(),
        "order_date": date.strftime("%Y-%m-%d"),
        "product": product,
        "category": category,
        "price": price,
        "quantity": quantity,
        "customer_id": fake.random_int(min=1000, max=9999),
        "city": random.choice(cities),
        "payment_method": random.choice(payment_methods),
    }

    data.append(row)

df = pd.DataFrame(data)
df.to_csv("data/sales_data.csv", index=False)

print("Dataset generado correctamente en data/sales_data.csv")
