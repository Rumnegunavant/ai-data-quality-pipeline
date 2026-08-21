import json
import ollama


MODEL_NAME = "llama3.2"


def analyze_data_quality(report):

    report_json = json.dumps(
        report,
        indent=4
    )

    prompt = f"""
You are an experienced Data Quality Engineer and
Data Engineering AI Assistant.

Analyze the following data quality report.

DATA QUALITY REPORT:

{report_json}

Provide your response using exactly these sections:

1. OVERALL ASSESSMENT
Give a short summary of the overall data quality.

2. CRITICAL ISSUES
Identify the most important issues.

3. POTENTIAL BUSINESS IMPACT
Explain how these issues could affect reporting,
analytics, or business decisions.

4. POSSIBLE ROOT CAUSES
Suggest reasonable possible causes based on the
reported patterns. Do not present uncertain causes
as facts.

5. RECOMMENDED ACTIONS
Provide practical recommendations for fixing or
preventing these issues.

6. SEVERITY
Classify the overall severity as:
LOW, MEDIUM, or HIGH.

Keep the answer clear and professional.
"""

    try:

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional "
                        "Data Quality AI Assistant."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content

    except Exception as error:

        return (
            "AI ANALYSIS FAILED\n"
            f"Reason: {error}\n\n"
            "Please verify that Ollama is running "
            "and that the model is installed."
        )