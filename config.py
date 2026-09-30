import os

import crewai.llms.cache as crew_cache
from crewai import LLM


# Fix for CrewAI sending cache_breakpoint
# to providers such as Groq that do not support it.
crew_cache.mark_cache_breakpoint = lambda msg: msg


def get_llm():
    return LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=os.environ.get("GROQ_API_KEY"),
        temperature=0.2
    )
