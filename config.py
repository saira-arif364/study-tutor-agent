import os
from crewai import LLM

import os
from crewai import LLM


def get_llm():
    return LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=os.environ.get("GROQ_API_KEY"),
        temperature=0.2
    )
def get_llm():

    return LLM(
        model="openai/gpt-oss-120b",
        api_key=os.environ.get("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0.2
    )
