import mysql.connector
from datetime import date
import pandas as pd

def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anoop1023@",
        database="retail_sales_db"
    )
    return conn

conn=get_connection()
print("Connection Successfull")
conn.close()


# def insert_sample_data():
#     conn=get_connection()
#     cursor=conn.cursor()

#     customers = [
#         ("Anoop", "anoop@example.com", "Delhi"),
#         ("Ravi", "ravi@example.com", "Mumbai")
#     ]

#     products = [
#         ("Laptop", "Electronics", 60000),
#         ("Headphones", "Electronics", 2000),
#         ("Chair", "Furniture", 3000)
#     ]

#     cursor.executemany("INSERT INTO customers (name, email, city) VALUES (%s, %s, %s)", customers)
#     cursor.executemany("INSERT INTO products (product_name, category, price) VALUES (%s, %s, %s)", products)

#     conn.commit()
#     conn.close()
#     print("✅ Sample data inserted successfully!")

# insert_sample_data()

# def record_sale(customer_id,product_id,quantity):
#     conn=get_connection()
#     cursor=conn.cursor()

#     print(f"DEBUG: inserting sale -> customer_id={customer_id}, product_id={product_id}, quantity={quantity}")

#     cursor.execute("""
#         INSERT INTO sales (customer_id, product_id, quantity, sale_date)
#         VALUES (%s, %s, %s, %s)
#     """, (customer_id, product_id, quantity, date.today()))
    
#     conn.commit()
#     conn.close()
#     print("🛒 Sale recorded successfully!")

# record_sale(3,1,2)

def sales_report():
    conn = get_connection()
    query = """
        SELECT c.name AS customer, p.product_name, p.price, s.quantity,
               (p.price * s.quantity) AS total_sale, s.sale_date
        FROM sales s
        JOIN customers c ON s.customer_id = c.customer_id
        JOIN products p ON s.product_id = p.product_id
    """
    df = pd.read_sql(query, conn)
    conn.close()

    print("\n📄 SALES REPORT:")
    print(df)

    # Total revenue per product
    product_sales = df.groupby('product_name')['total_sale'].sum()
    print("\n💰 Total Sales by Product:")
    print(product_sales)

    # Optional: plot results
    product_sales.plot(kind='bar', title='Total Sales by Product', ylabel='Revenue (INR)')

sales_report()
                       
