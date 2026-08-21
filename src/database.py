import sqlite3


DATABASE_NAME = "sales_analytics.db"


def load_to_database(df):

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    try:

        df.to_sql(
            name="sales_transactions",
            con=connection,
            if_exists="replace",
            index=False
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM sales_transactions
            """
        )

        record_count = cursor.fetchone()[0]

        print(
            f"Successfully loaded "
            f"{record_count} records into SQLite"
        )

    finally:

        connection.close()