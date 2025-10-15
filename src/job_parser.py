import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE

genai.configure(api_key=GEMINI_API_KEY)

def parse_job_description(text):
    model = genai.GenerativeModel(MODEL_NAME)
    prompt = f"""
Extract key information from the following job description.

Return JSON like:
{{
  "title": "string",
  "company": "string (if mentioned)",
  "skills_required": ["skill1", "skill2"],
  "experience_required": "short text",
  "education_required": "short text",
  "other_details": "summary"
}}

Job Description:
{text}
"""
    response = model.generate_content(prompt, generation_config={"temperature": TEMPERATURE})
    return response.text
