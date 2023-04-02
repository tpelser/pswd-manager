import sqlite3
from .models import CREATE_PASSWORD_DATA_TABLE, INSERT_INTO_PASSWORD_DATA_TABLE, FETCH_PASSWORD_DATA_BY_WEBSITE
from utils.hashing import hash_password

def db_config():
    conn = sqlite3.connect("pwd_manager.db")
    cursor = conn.cursor()
    cursor.execute(CREATE_PASSWORD_DATA_TABLE)
    conn.commit()
    conn.close()

def add_password_data(website: str, email: str, username: str, password: str):
    password_hash = hash_password(password)
    conn = sqlite3.connect("pwd_manager.db")
    cursor = conn.cursor()
    cursor.execute(INSERT_INTO_PASSWORD_DATA_TABLE, (website, email, username, password_hash))
    conn.commit()    
    conn.close()


def get_password_data_by_website(website):
    conn = sqlite3.connect('pwd_manager.db')
    cursor = conn.cursor()
    cursor.execute(FETCH_PASSWORD_DATA_BY_WEBSITE, (website,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return PasswordData(*result)
    else:
        return None