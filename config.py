import os
from crewai import LLM


def get_llm():
    return LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=os.environ.get("GROQ_API_KEY"),
        temperature=0.2
    )
