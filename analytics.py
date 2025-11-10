import pandas as pd
from db_connection import get_connection

def monthly_sales_trend():
    conn = get_connection()

    query = """
    SELECT 
        DATE_FORMAT(sale_date, '%Y-%m') AS month,
        SUM(quantity) AS total_quantity,
        SUM(p.price * s.quantity) AS total_sales
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY DATE_FORMAT(sale_date, '%Y-%m')
    ORDER BY month;
    """

    df = pd.read_sql(query, conn)
    conn.close()

    print(df)
    df.to_csv('sales_report.csv', index=False)
    print("📁 Sales report saved as 'sales_report.csv'")

if __name__ == "__main__":
    monthly_sales_trend()
