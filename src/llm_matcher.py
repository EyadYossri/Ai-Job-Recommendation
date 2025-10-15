
import json
import google.generativeai as genai
from src.config import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE
import time

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

def evaluate_candidate(cv_json, job_json):
    model = genai.GenerativeModel(MODEL_NAME)
    prompt = f"""
Compare the candidate's details with the job description and rate suitability.

Job Description:
{job_json}

Candidate:
{cv_json}

Return only valid JSON with:
{{
  "score": number (0–100),
  "reason": "short explanation why they fit or not"
}}
"""
    response = model.generate_content(prompt, generation_config={"temperature": TEMPERATURE})
    result_text = response.text.strip()

    # 🧹 Clean up code fences and extra text like ```json
    result_text = result_text.replace("```json", "").replace("```", "").strip()

    try:
        # Convert string JSON → dict safely
        result_json = json.loads(result_text)
    except json.JSONDecodeError:
        # fallback if Gemini adds text before JSON
        start = result_text.find("{")
        end = result_text.rfind("}") + 1
        result_json = json.loads(result_text[start:end])

    return result_json


def rank_candidates(job_json, cvs_json):
    results = []
    for cv_info in cvs_json:
        cv_name = cv_info["file_name"]
        cv_json = cv_info["cv_data"]

        evaluation = evaluate_candidate(cv_json, job_json)

        results.append({
            "cv_name": cv_name,
            "score": evaluation.get("score", 0),
            "reason": evaluation.get("reason", "No reason provided.")
        })
        time.sleep(60)

    return results

