# 🤖 AI-Powered Data Quality Monitoring Pipeline

> An end-to-end Data Engineering pipeline for automated data validation, ETL processing, database loading, and AI-powered data quality analysis.

## 🏗️ Architecture

```text
📄 Source CSV
      │
      ▼
📥 Data Ingestion
      │
      ▼
🔍 Data Quality Validation
      │
      ▼
🤖 AI Analysis (Ollama + Llama 3.2)
      │
      ├── 📊 Data Quality Report
      ▼
⚙️ ETL Transformation
      │
      ▼
🗄️ SQLite Database
      │
      ▼
📁 Processed File Storage
```

## ✨ Features

* 📥 Automated CSV ingestion
* 🔍 Schema validation
* ❌ Null value detection
* 🔁 Duplicate detection
* ⚠️ Invalid value detection
* 📅 Date validation
* ⚙️ ETL transformation
* 🤖 AI-powered analysis using Ollama + Llama 3.2
* 🗄️ SQLite database loading
* 📝 Pipeline logging and reporting
* 📁 Automated file management

## 🛠️ Tech Stack

| Technology   | Usage                |
| ------------ | -------------------- |
| 🐍 Python    | Pipeline Development |
| 🐼 Pandas    | Data Processing      |
| 🗄️ SQLite   | Database             |
| 🤖 Ollama    | Local LLM            |
| 🦙 Llama 3.2 | AI Analysis          |
| 🔀 Git       | Version Control      |

## 📁 Project Structure

```text
AI-Data-Quality-Pipeline/
│
├── data/
├── src/
│   ├── ingestion.py
│   ├── validation.py
│   ├── ai_analysis.py
│   ├── transformation.py
│   └── database_loader.py
│
├── reports/
├── logs/
├── main.py
├── requirements.txt
└── README.md
```

## 🚀 Run the Project

```bash
# Clone repository
git clone <repository-url>

# Install dependencies
pip install -r requirements.txt

# Pull AI model
ollama pull llama3.2

# Run pipeline
python main.py
```

## 🎯 Key Highlights

This project demonstrates:

**Data Ingestion • Data Quality • ETL • Python • Pandas • SQLite • AI/LLM Integration • Git**

---

⭐ **If you found this project useful, consider giving it a star!**
