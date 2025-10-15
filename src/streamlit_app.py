import streamlit as st
import tempfile
from pdf_extractor import extract_text_from_pdf
from job_parser import parse_job_description
from cv_parser import parse_cv
from llm_matcher import rank_candidates
import time

st.set_page_config(page_title="LLM Job Recommender", page_icon="🤖")

st.title("🤖 LLM-Powered Job Recommendation System")

# --- Upload job description ---
st.header("1️⃣ Upload Job Description PDF")
job_file = st.file_uploader("Upload a job description", type=["pdf"])

# --- Upload CVs ---
st.header("2️⃣ Upload Candidate CVs (PDFs)")
cv_files = st.file_uploader("Upload multiple CVs", type=["pdf"], accept_multiple_files=True)

if st.button("Analyze Candidates") and job_file and cv_files:
    with st.spinner("Extracting job description..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(job_file.read())
            job_text = extract_text_from_pdf(tmp.name)
        job_json = parse_job_description(job_text)

    cvs_json = []
    progress = st.progress(0)

    for i, cv_file in enumerate(cv_files):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(cv_file.read())
            cv_text = extract_text_from_pdf(tmp.name)
        parsed_cv = parse_cv(cv_text)
        cvs_json.append({
            "file_name": cv_file.name,
            "cv_data": parsed_cv
        })

        time.sleep(60)
        progress.progress((i + 1) / len(cv_files))

    st.success("✅ All CVs processed!")

    st.subheader("📊 Ranking Candidates...")
    results = rank_candidates(job_json, cvs_json)

    st.write("### 🧠 Results")
    for r in results:
        st.json(r)
