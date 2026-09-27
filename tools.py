from crewai.tools import tool


@tool("Calculator")
def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.
    Use this tool when an accurate calculation is required.
    """

    try:
        allowed = "0123456789+-*/().% "

        if not all(char in allowed for char in expression):
            return "Invalid mathematical expression."

        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return f"Calculation result: {result}"

    except Exception:
        return "Unable to calculate this expression."


@tool("Quiz Generator")
def quiz_generator(topic: str) -> str:
    """
    Generate instructions for creating a study quiz.
    """

    return f"""
Create a short quiz about:

{topic}

The quiz must contain:

- 3 questions
- Conceptual questions
- Practical questions
- Correct answers
- Short explanations
"""
