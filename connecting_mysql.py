import pandas as pd
import mysql.connector

df = pd.read_csv(
    r"C:\Users\user\OneDrive\Desktop\Python Minis\HR Project\user_data_updated.csv")

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456789",
    database="random_users"
)

cursor = conn.cursor()

cursor.execute("USE random_users")
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    age INT,
    city VARCHAR(100),
    created_at DATE
)
""")

# insert data

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO users (id, name, email, age, city, created_at)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        name=VALUES(name), email=VALUES(email), age=VALUES(age),
        city=VALUES(city), created_at=VALUES(created_at)
                   """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("Data inserted into MySQL Successfully")
