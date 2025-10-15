import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    MODEL_NAME = st.secrets.get("MODEL_NAME", "gemini-pro-latest")
    TEMPERATURE = float(st.secrets.get("TEMPERATURE", 0.2))
else:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-pro-latest")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.2))
