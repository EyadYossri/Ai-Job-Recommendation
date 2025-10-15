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
# Clone the repos
