import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="random_users"
    )
    return connection
