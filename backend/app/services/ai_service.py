from app.llm.gemini import ask_gemini

class AIService:
    @staticmethod
    def chat(prompt:str):
        return ask_gemini(prompt=prompt)