import mysql.connector

def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anoop1023@",
        database="retail_sales_db"
    )
    return conn

