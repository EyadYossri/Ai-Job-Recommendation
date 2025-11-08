# 🤖 LLM Job Recommender

**LLM Job Recommender** is an AI-powered Streamlit web app that analyzes job descriptions and candidate CVs using **Google’s Gemini LLM** to find the best candidate matches.  

It automatically:
- Extracts text from job description and CV PDFs  
- Uses **Gemini AI** to parse key details such as skills, education, and experience  
- Compares each CV with the job description  
- Produces a **ranked list of candidates** based on suitability scores  

---

## 🧠 Key Features
- 📄 **PDF Extraction** using `PyMuPDF` (`pymupdf`)  
- 🧩 **LLM Analysis** powered by `google-generativeai`  
- 🔐 **Secure Configuration** with `.env` file (API keys hidden)  
- ⚡ **Streamlit Frontend** for smooth user interaction  
- 🧮 **Candidate Ranking** with AI-generated reasoning  

---

## 🧰 Tech Stack
| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit |
| **Backend** | Python |
| **AI Model** | Google Gemini API |
| **PDF Parsing** | PyMuPDF |
| **Environment Config** | python-dotenv |

---

## 🚀 How It Works
1. Upload a **job description PDF**.  
2. Upload one or more **candidate CVs**.  
3. The app:
   - Extracts and parses all PDFs.  
   - Compares job requirements and candidate profiles.  
   - Displays a ranked result with suitability scores.  

---

## ⚙️ Setup Instructions
```bash
# Clone the repository
git clone https://github.com/EyadYossri/Ai-Job-Recommendation.git
cd Ai-Job-Recommendation

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # (Windows)

# Install dependencies
pip install -r requirements.txt

# Create .env file
GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini-2.5-flash-lite
TEMPERATURE=0.2

# Run the app
streamlit run src/streamlit_app.py
```

## 🟥 Streamlit App

You can also try the **Streamlit version** here:  
[https://ai-job-recommendation.streamlit.app/](https://ai-job-recommendation.streamlit.app/)
