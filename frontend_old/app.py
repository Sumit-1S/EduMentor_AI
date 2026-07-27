import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="EduMentor AI",
    page_icon="",
    layout="wide"
)

st.title("EduMentor AI")

st.write("Welcome to EduMentor AI!")

if st.button("Check Backend Status"):

    response = requests.get(f"{BACKEND_URL}/health")

    if response.status_code == 200:
        st.success(response.json()["message"])

    else:
        st.error("Backend is not running")

