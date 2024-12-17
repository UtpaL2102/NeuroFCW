from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import getpass
from dotenv import load_dotenv

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.7,
    max_tokens=2048,
    timeout=None,
    max_retries=2
)

def give_output(prompt:str)->str:
    messages = [
        (
            "system","You are a helpful code assistant that generates optimized python codes. Give the code for user query",
        ),
        ("human", prompt),
    ]
    ai_msg = llm.invoke(messages)
    return ai_msg.content