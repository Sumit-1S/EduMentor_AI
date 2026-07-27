import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings

from app.AI.prompts import SYSTEM_PROMPTS

from langchain_core.messages import (
    SystemMessage,
    HumanMessage, 
    AIMessage
)

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash",
    google_api_key=settings.GEMINI_API_KEY,
    temperature=0.3
)

def ask_llm(messages):
    messages.insert(0,SystemMessage(content=SYSTEM_PROMPTS))
    print(messages)
    
    response = llm.invoke(messages)

    content = response.content

    if isinstance(content,list):
        text = ""
        for item in content:
            if isinstance(item,dict):
                text+=item.get("text","")
            else:
                text+=str(item)
        return text
    return str(content)