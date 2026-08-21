import json
import logging
from pathlib import Path

import pandas as pd

from src.data_generator import generate_sales_data
from src.validator import DataValidator
from src.etl_pipeline import clean_data
from src.database import load_to_database
from src.file_manager import move_file
from src.ai_analyzer import analyze_data_quality


# ---------------------------------------
# Create required directories
# ---------------------------------------

Path("logs").mkdir(
    exist_ok=True
)

Path("reports").mkdir(
    exist_ok=True
)


# ---------------------------------------
# Logging configuration
# ---------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(message)s"
    ),
    handlers=[
        logging.FileHandler(
            "logs/pipeline.log"
        ),
        logging.StreamHandler()
    ]
)


def main():

    logging.info(
        "AI Data Quality Pipeline Started"
    )

    try:

        # -----------------------------------
        # STEP 1: Generate source data
        # -----------------------------------

        logging.info(
            "Generating source data"
        )

        source_file = generate_sales_data()

        # -----------------------------------
        # STEP 2: Read source file
        # -----------------------------------

        logging.info(
            "Reading source file"
        )

        df = pd.read_csv(
            source_file
        )

        logging.info(
            f"Total input records: {len(df)}"
        )

        # -----------------------------------
        # STEP 3: Data Quality Validation
        # -----------------------------------

        logging.info(
            "Running data quality checks"
        )

        validator = DataValidator()

        quality_report = validator.validate(
            df
        )

        print("\n")
        print("=" * 60)
        print("DATA QUALITY REPORT")
        print("=" * 60)

        print(
            json.dumps(
                quality_report,
                indent=4,
                default=str
            )
        )

        # -----------------------------------
        # STEP 4: Save quality report
        # -----------------------------------

        with open(
            "reports/data_quality_report.json",
            "w"
        ) as file:

            json.dump(
                quality_report,
                file,
                indent=4,
                default=str
            )

        logging.info(
            "Data quality report saved"
        )

        # -----------------------------------
        # STEP 5: AI Analysis
        # -----------------------------------

        logging.info(
            "Sending report to Local AI Model"
        )

        ai_analysis = analyze_data_quality(
            quality_report
        )

        print("\n")
        print("=" * 60)
        print("AI DATA QUALITY ANALYSIS")
        print("=" * 60)

        print(ai_analysis)

        # Save AI analysis

        with open(
            "reports/ai_analysis.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(ai_analysis)

        logging.info(
            "AI analysis saved"
        )

        # -----------------------------------
        # STEP 6: ETL Transformation
        # -----------------------------------

        logging.info(
            "Starting ETL transformation"
        )

        cleaned_df, metrics = clean_data(
            df
        )

        print("\n")
        print("=" * 60)
        print("PIPELINE METRICS")
        print("=" * 60)

        print(
            json.dumps(
                metrics,
                indent=4
            )
        )

        # -----------------------------------
        # STEP 7: Load to SQLite
        # -----------------------------------

        logging.info(
            "Loading cleaned data to SQLite"
        )

        load_to_database(
            cleaned_df
        )

        # -----------------------------------
        # STEP 8: Move source file
        # -----------------------------------

        logging.info(
            "Moving processed file"
        )

        new_location = move_file(
            source_file,
            "data/processed"
        )

        logging.info(
            f"File moved to: {new_location}"
        )

        # -----------------------------------
        # Pipeline success
        # -----------------------------------

        logging.info(
            "Pipeline completed successfully"
        )

        print("\n")
        print("PIPELINE STATUS: SUCCESS")

    except Exception as error:

        logging.exception(
            f"Pipeline failed: {error}"
        )

        print("\n")
        print("PIPELINE STATUS: FAILED")


if __name__ == "__main__":

    main()