from fastapi import FastAPI, HTTPException
from models import User
from database import get_connection

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Welcome to the HR API!"}


@app.get("/users")
def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


@app.post("/users")
def create_user(user: User):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (id, name, email, age, city, created_at)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (user.id, user.name, user.email, user.age, user.city, user.created_at))
        conn.commit()
    except:
        conn.rollback()
        raise HTTPException(status_code=400, detail="User insert failed")
    finally:
        cursor.close()
        conn.close()
    return {"msg": "User created successfully"}


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE users
        SET name=%s, email=%s, age=%s, city=%s, created_at=%s
        WHERE id=%s
    """, (user.name, user.email, user.age, user.city, user.created_at, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"msg": "User updated successfully"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"msg": "User deleted successfully"}
