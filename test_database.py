import sqlite3
import pandas as pd


connection = sqlite3.connect(
    "sales_analytics.db"
)

query = """
SELECT
    product,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_sales,
    ROUND(AVG(amount), 2) AS average_sales
FROM sales_transactions
GROUP BY product
ORDER BY total_sales DESC
"""

result = pd.read_sql_query(
    query,
    connection
)

print(result)

connection.close()