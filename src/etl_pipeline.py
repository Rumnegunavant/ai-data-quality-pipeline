import pandas as pd


def clean_data(df):

    cleaned_df = df.copy()

    initial_records = len(cleaned_df)

    # Remove duplicate records
    cleaned_df = cleaned_df.drop_duplicates()

    # Remove invalid quantity
    cleaned_df = cleaned_df[
        cleaned_df["quantity"] > 0
    ]

    # Remove invalid amount
    cleaned_df = cleaned_df[
        cleaned_df["amount"] > 0
    ]

    # Handle missing customer names
    cleaned_df["customer_name"] = (
        cleaned_df["customer_name"]
        .fillna("Unknown")
    )

    # Convert transaction date
    cleaned_df["transaction_date"] = pd.to_datetime(
        cleaned_df["transaction_date"],
        errors="coerce"
    )

    # Remove records with invalid dates
    cleaned_df = cleaned_df.dropna(
        subset=["transaction_date"]
    )

    # Add ETL metadata
    cleaned_df["processed_timestamp"] = (
        pd.Timestamp.now()
    )

    final_records = len(cleaned_df)

    rejected_records = (
        initial_records - final_records
    )

    metrics = {
        "input_records": initial_records,
        "processed_records": final_records,
        "rejected_records": rejected_records
    }

    return cleaned_df, metrics