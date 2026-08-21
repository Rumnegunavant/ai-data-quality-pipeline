import random
from pathlib import Path

import pandas as pd


def generate_sales_data(num_records=100):

    random.seed(42)

    customers = [
        "Rahul Sharma",
        "Priya Patil",
        "Amit Kumar",
        "Sneha Singh",
        "Rohan Verma",
        "Anjali Deshmukh"
    ]

    products = [
        "Laptop",
        "Mobile",
        "Headphones",
        "Keyboard",
        "Monitor"
    ]

    data = []

    for i in range(num_records):

        quantity = random.randint(1, 5)
        price = random.randint(500, 100000)

        data.append({
            "transaction_id": i + 1,
            "customer_name": random.choice(customers),
            "product": random.choice(products),
            "quantity": quantity,
            "amount": quantity * price,
            "transaction_date": (
                f"2026-08-{random.randint(1, 20):02d}"
            )
        })

    df = pd.DataFrame(data)

    # ---------------------------------------
    # Intentionally introduce data issues
    # ---------------------------------------

    # Duplicate records
    df = pd.concat(
        [df, df.iloc[:3]],
        ignore_index=True
    )

    # Missing value
    df.loc[5, "customer_name"] = None

    # Negative amount
    df.loc[10, "amount"] = -5000

    # Invalid quantity
    df.loc[15, "quantity"] = -2

    source_folder = Path("data/source")
    source_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = source_folder / "sales_data.csv"

    df.to_csv(
        file_path,
        index=False
    )

    print("=" * 60)
    print("SAMPLE DATA GENERATED")
    print("=" * 60)
    print(f"Total records generated: {len(df)}")
    print(f"File location: {file_path}")

    return str(file_path)


if __name__ == "__main__":
    generate_sales_data() 