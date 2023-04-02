import sqlite3
from .models import CREATE_PASSWORD_DATA_TABLE, INSERT_INTO_PASSWORD_DATA_TABLE, SELECT_PASSWORD
from ..utils.hashing import hash_password

def db_config():
    conn = sqlite3.connect("pwd_manager.db")
    cursor = conn.cursor()
    
    cursor.execute(CREATE_PASSWORD_DATA_TABLE)
    
    conn.commit()
    conn.close()

def add_password_data(website: str, email: str, username: str, password: str):
    password_hash = hash_password(password)
    conn = sqlite3.connect("pwd_manager.db")
    cursor = conn.cursor
    cursor.execute(INSERT_INTO_PASSWORD_DATA_TABLE, (website, email, username, password_hash))
    conn.commit()
    conn.close()

def get_password_data():
    conn = sqlite3('pwd_manager.db')
    cursor = conn.cursor()
    cursor.execute(SELECT_PASSWORD)
    password_data = cursor.fetchall()
    conn.close()
    return password_data