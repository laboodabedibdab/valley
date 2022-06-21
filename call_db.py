import mysql.connector
from config import host, user, password, db_name
try:
    connection = mysql.connector.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name
    )
    print("successfully connected...")
    try:
        cursor = connection.cursor()
    except Exception as ex2:
        print("BAN",ex2)
except Exception as ex:
    print("Connection refused...")
    print(ex)