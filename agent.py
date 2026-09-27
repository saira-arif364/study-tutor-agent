from crewai import Agent, Task, Crew

from config import get_llm
from tools import calculator, quiz_generator


# --------------------------------
# LLM
# --------------------------------

llm = get_llm()


# --------------------------------
# STUDY TUTOR AGENT
# --------------------------------

study_tutor = Agent(
    role="Study Tutor",

    goal="""
    Help students understand academic concepts,
    practice their knowledge, and improve their learning.
    """,

    backstory="""
    You are a patient and friendly AI study tutor.

    You explain difficult concepts in simple language.

    You adapt explanations to the student's level.

    You use examples and analogies when helpful.

    You create practice questions and quizzes.

    You evaluate student answers and explain mistakes
    constructively.

    You remember useful information about the student's
    learning preferences when available.
    """,

    llm=llm,

    tools=[
        calculator,
        quiz_generator
    ],

    memory=True,

    verbose=True
)


# --------------------------------
# ASK TUTOR
# --------------------------------

def ask_tutor(question):

    task = Task(
        description=f"""
        The student asks:

        {question}

        Act as a personal study tutor.

        Follow these rules:

        1. Understand what the student is asking.

        2. Explain the answer clearly.

        3. Use simple language when appropriate.

        4. Give an example when useful.

        5. Use the Calculator tool when
           accurate calculation is required.

        6. Use the Quiz Generator tool when
           the student requests a quiz.

        7. If the student provides an answer,
           evaluate it and explain mistakes.

        8. Use relevant remembered information
           about the student when available.

        9. Encourage learning instead of simply
           giving answers.
        """,

        expected_output="""
        A helpful tutoring response.

        Give a clear explanation.

        Use examples when appropriate.

        End with a short practice question
        when useful.
        """,

        agent=study_tutor
    )

    crew = Crew(
        agents=[study_tutor],
        tasks=[task],
        memory=True,
        verbose=True
    )

    result = crew.kickoff()

    return str(result)
