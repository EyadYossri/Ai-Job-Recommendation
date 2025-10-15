import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE

genai.configure(api_key=GEMINI_API_KEY)

def parse_cv(cv_text):
    model = genai.GenerativeModel(MODEL_NAME)
    prompt = f"""
Extract the candidate's key details and return in JSON format:
{{
  "cv_file_name":"string",
  "name": "string (if found)",
  "skills": ["skill1", "skill2"],
  "education": "string",
  "experience": "summary of work experience",
  "certifications": ["optional list"]
}}

CV Content:
{cv_text}
"""
    response = model.generate_content(prompt, generation_config={"temperature": TEMPERATURE})
    return response.text
