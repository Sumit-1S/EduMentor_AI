import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

from langchain_google_genai import ChatGoogleGenerativeAI

model = genai.GenerativeModel("gemini-3.5-flash")

def ask_gemini(prompt: str):
    response = model.generate_content(prompt)
    return response.text