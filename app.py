import streamlit as st

from agent import ask_tutor

from ui import (
    load_css,
    show_header,
    show_hero,
    show_footer
)


# =================================
# PAGE CONFIG
# =================================

st.set_page_config(

    page_title="Study Tutor AI",

    page_icon="✦",

    layout="wide",

    initial_sidebar_state="collapsed"
)


# =================================
# LOAD UI
# =================================

load_css()

show_header()

show_hero()


# =================================
# FEATURE CARDS
# =================================

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">
                💡
            </div>

            <div class="feature-title">
                Learn
            </div>

            <div class="feature-description">
                Get clear explanations for difficult
                concepts using simple language and examples.
            </div>

        </div>
        """,

        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">
                🧠
            </div>

            <div class="feature-title">
                Practice
            </div>

            <div class="feature-description">
                Test your understanding with quizzes
                and practice questions.
            </div>

        </div>
        """,

        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">
                ⚡
            </div>

            <div class="feature-title">
                Improve
            </div>

            <div class="feature-description">
                Get feedback and learn from your
                mistakes.
            </div>

        </div>
        """,

        unsafe_allow_html=True
    )


# =================================
# CHAT MEMORY
# =================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# =================================
# DISPLAY CHAT
# =================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =================================
# CHAT INPUT
# =================================

question = st.chat_input(
    "Ask your tutor anything..."
)


if question:

    # Save user message

    st.session_state.messages.append({

        "role": "user",

        "content": question

    })


    # Display user message

    with st.chat_message("user"):

        st.markdown(question)


    # Generate tutor response

    with st.chat_message("assistant"):

        with st.spinner("Tutor is thinking..."):

            try:

                response = ask_tutor(question)

                st.markdown(response)


                st.session_state.messages.append({

                    "role": "assistant",

                    "content": response

                })


            except Exception as e:

                st.error(
                    "Something went wrong. "
                    f"Details: {e}"
                )


# =================================
# FOOTER
# =================================

show_footer()
