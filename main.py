from crud_operation import (
    add_customer, get_customers,
    add_product, get_products
)
from analytics import monthly_sales_trend

if __name__ == "__main__":
    # --- Add sample data ---
    add_customer("Anoop Tripathi", "anoop@example.com", "Delhi")
    add_product("Bluetooth Speaker", "Electronics", 2500)

    # --- View all customers and products ---
    print(get_customers())
    print(get_products())

    # --- Generate monthly sales trend ---
    monthly_sales_trend()
