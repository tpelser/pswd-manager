import sqlite3
from .models import CREATE_PASSWORD_DATA_TABLE, INSERT_INTO_PASSWORD_DATA_TABLE, FETCH_PASSWORD_DATA_BY_WEBSITE, PasswordData
import os

db_path = os.path.join("usr", "pwd_manager.db")

def db_config():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(CREATE_PASSWORD_DATA_TABLE)
    conn.commit()
    conn.close()

def add_password_data(website: str, email: str, username: str, password: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(INSERT_INTO_PASSWORD_DATA_TABLE, (website, email, username, password))
    conn.commit()    
    conn.close()

def get_password_data_by_website(website):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(FETCH_PASSWORD_DATA_BY_WEBSITE, (website,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return PasswordData(*result)
    else:
        return None