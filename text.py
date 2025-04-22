import pandas as pd
import mysql.connector

# Load updated CSV
df = pd.read_csv(
    r"C:\Users\user\OneDrive\Desktop\Python Minis\HR Project\user_data_updated.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="random_users"
)

cursor = conn.cursor()

# Create database if it doesn't exist
# cursor.execute("CREATE DATABASE IF NOT EXISTS demo_db")
cursor.execute("USE random_users")

# Create table
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

# Convert 'created_at' to MySQL-friendly format
df['created_at'] = pd.to_datetime(
    df['created_at'], dayfirst=True).dt.strftime('%Y-%m-%d')

# Insert data
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

print("✅ Data inserted into MySQL successfully!")
