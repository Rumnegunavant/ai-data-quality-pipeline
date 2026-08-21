import pandas as pd
class DataValidator:

    REQUIRED_COLUMNS = [
        "transaction_id",
        "customer_name",
        "product",
        "quantity",
        "amount",
        "transaction_date"
    ]

    def validate_schema(self, df):

        return [
            column
            for column in self.REQUIRED_COLUMNS
            if column not in df.columns
        ]

    def check_null_values(self, df):

        null_counts = df.isnull().sum()

        return {
            column: int(count)
            for column, count in null_counts.items()
            if count > 0
        }

    def check_duplicates(self, df):

        return int(df.duplicated().sum())

    def check_invalid_values(self, df):

        issues = {}

        if "quantity" in df.columns:

            invalid_quantity = (
                df["quantity"] <= 0
            ).sum()

            if invalid_quantity > 0:

                issues["invalid_quantity"] = int(
                    invalid_quantity
                )

        if "amount" in df.columns:

            invalid_amount = (
                df["amount"] <= 0
            ).sum()

            if invalid_amount > 0:

                issues["invalid_amount"] = int(
                    invalid_amount
                )

        return issues

    def check_invalid_dates(self, df):

        converted_dates = df["transaction_date"]

        invalid_dates = converted_dates.isna().sum()

        return int(invalid_dates)

    def validate(self, df):

        # Convert date safely for validation
        df = df.copy()

        df["transaction_date"] = pd.to_datetime(
            df["transaction_date"],
            errors="coerce"
        )

        report = {
            "total_records": len(df),
            "missing_columns": self.validate_schema(df),
            "null_values": self.check_null_values(df),
            "duplicate_records": self.check_duplicates(df),
            "invalid_value_issues":
                self.check_invalid_values(df),
            "invalid_dates":
                self.check_invalid_dates(df)
        }

        return report