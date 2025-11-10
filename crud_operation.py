from db_connection import get_connection

# ==============================
# CUSTOMER CRUD
# ==============================
def add_customer(name, email, city):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO customers (name, email, city) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, city))
    conn.commit()
    conn.close()
    print("✅ Customer added successfully!")

def get_customers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_customer(customer_id, name=None, email=None, city=None):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE customers SET name=%s, email=%s, city=%s WHERE customer_id=%s"
    cursor.execute(query, (name, email, city, customer_id))
    conn.commit()
    conn.close()
    print("✅ Customer updated successfully!")

def delete_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM customers WHERE customer_id=%s"
    cursor.execute(query, (customer_id,))
    conn.commit()
    conn.close()
    print("🗑️ Customer deleted successfully!")

# ==============================
# PRODUCT CRUD
# ==============================
def add_product(name, category, price):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO products (product_name, category, price) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, category, price))
    conn.commit()
    conn.close()
    print("✅ Product added successfully!")

def get_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_product(product_id, name=None, category=None, price=None):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE products SET product_name=%s, category=%s, price=%s WHERE product_id=%s"
    cursor.execute(query, (name, category, price, product_id))
    conn.commit()
    conn.close()
    print("✅ Product updated successfully!")

def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM products WHERE product_id=%s"
    cursor.execute(query, (product_id,))
    conn.commit()
    conn.close()
    print("🗑️ Product deleted successfully!")
