import os
from crewai import LLM

def get_llm():
 return LLM(
model="groq/llama-3.3-70b-versatile",
api_key=os.environ.get("GROQ_API_KEY"),
base_url="https://api.groq.com/openai/v1",
temperature=0.2
)
