AI-Powered Data Quality Monitoring Pipeline

A local Data Engineering project that performs automated data ingestion, data quality validation, ETL transformation, AI-powered data quality analysis, file management, and database loading.

Architecture
Source CSV
    |
    v
Data Ingestion
    |
    v
Data Quality Validation
    |
    v
Local AI Analysis
    |
    +----> Data Quality Report
    |
    v
ETL Transformation
    |
    v
SQLite Database
    |
    v
Processed File Storage
    
Features
Automated CSV data generation
Schema validation
Null value detection
Duplicate detection
Invalid value detection
Date validation
ETL transformation
Local LLM integration using Ollama
AI-generated data quality analysis
Pipeline logging
SQLite database loading
Automated file movement
Pipeline reporting
Technologies Used
Python
Pandas
SQLite
Ollama
Llama 3.2
Git