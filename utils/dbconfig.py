import mysql.connector

def dbconfig():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="pm",
            passwd="password"
        )
    except 