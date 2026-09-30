import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        /* ================================
           MAIN APP
        ================================= */

        .stApp {
            background:
                radial-gradient(
                    circle at 15% 10%,
                    rgba(0, 174, 255, 0.14),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 85% 80%,
                    rgba(99, 102, 241, 0.12),
                    transparent 30%
                ),
                #050816;

            color: #f5f7ff;
        }

        .block-container {
            max-width: 1100px;
            padding-top: 2rem;
            padding-bottom: 5rem;
        }


        /* ================================
           HEADER
        ================================= */

        .ai-header {
            display: flex;
            align-items: center;
            justify-content: space-between;

            padding: 18px 22px;

            border: 1px solid rgba(80, 190, 255, 0.18);
            border-radius: 18px;

            background: rgba(10, 18, 40, 0.72);

            backdrop-filter: blur(18px);

            box-shadow:
                0 0 35px rgba(0, 174, 255, 0.08);

            margin-bottom: 30px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .brand-icon {
            width: 42px;
            height: 42px;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 13px;

            background:
                linear-gradient(
                    135deg,
                    #00c6ff,
                    #2563eb
                );

            box-shadow:
                0 0 22px rgba(0, 198, 255, 0.45);

            font-size: 21px;
        }

        .brand-title {
            font-size: 18px;
            font-weight: 700;
            letter-spacing: 0.4px;
        }

        .brand-subtitle {
            font-size: 12px;
            color: #8d9ab7;
            margin-top: 2px;
        }

        .online {
            font-size: 12px;
            color: #6ee7b7;

            padding: 7px 11px;

            border-radius: 20px;

            background:
                rgba(16, 185, 129, 0.08);

            border:
                1px solid rgba(16, 185, 129, 0.2);
        }


        /* ================================
           HERO
        ================================= */

        .hero {
            text-align: center;
            padding: 40px 20px 25px;
        }

        .hero-badge {
            display: inline-block;

            padding: 7px 14px;

            border-radius: 30px;

            border:
                1px solid rgba(0, 198, 255, 0.25);

            background:
                rgba(0, 198, 255, 0.07);

            color: #65d9ff;

            font-size: 12px;

            margin-bottom: 18px;
        }

        .hero h1 {
            font-size: clamp(34px, 6vw, 62px);

            line-height: 1.05;

            margin: 0;

            font-weight: 800;

            letter-spacing: -2px;

            background:
                linear-gradient(
                    90deg,
                    #ffffff,
                    #72d8ff,
                    #818cf8
                );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            max-width: 620px;

            margin: 18px auto;

            color: #9ba8c5;

            font-size: 16px;

            line-height: 1.7;
        }


        /* ================================
           FEATURE CARDS
        ================================= */

        .feature-card {
            padding: 22px;

            min-height: 135px;

            border-radius: 17px;

            border:
                1px solid rgba(120, 160, 255, 0.12);

            background:
                linear-gradient(
                    145deg,
                    rgba(16, 29, 58, 0.9),
                    rgba(7, 14, 32, 0.85)
                );

            transition:
                transform 0.2s ease,
                border-color 0.2s ease;

            margin-bottom: 15px;
        }

        .feature-card:hover {
            transform: translateY(-3px);

            border-color:
                rgba(0, 198, 255, 0.3);
        }

        .feature-icon {
            font-size: 25px;
            margin-bottom: 10px;
        }

        .feature-title {
            font-weight: 700;
            color: #f4f7ff;
            margin-bottom: 6px;
        }

        .feature-description {
            color: #8795b2;
            font-size: 13px;
            line-height: 1.5;
        }


        /* ================================
           CHAT MESSAGES
        ================================= */

        div[data-testid="stChatMessage"] {
            background:
                rgba(12, 22, 46, 0.72);

            border:
                1px solid rgba(90, 160, 255, 0.10);

            border-radius: 16px;

            margin-bottom: 12px;
        }


        /* ================================
           CHAT INPUT
        ================================= */

        div[data-testid="stChatInput"] {
            border-top:
                1px solid rgba(70, 150, 255, 0.12);
        }

        div[data-testid="stChatInput"] textarea {
            color: #000000 !important;

            background-color: #ffffff !important;

            caret-color: #000000 !important;

            -webkit-text-fill-color: #000000 !important;
        }

        div[data-testid="stChatInput"] textarea::placeholder {
            color: #666666 !important;
            opacity: 1 !important;
            -webkit-text-fill-color: #666666 !important;
        }

        div[data-testid="stChatInput"] textarea:focus {
            color: #000000 !important;

            background-color: #ffffff !important;

            -webkit-text-fill-color: #000000 !important;
        }


        /* ================================
           BUTTONS
        ================================= */

        .stButton > button {
            width: 100%;

            border-radius: 12px;

            border:
                1px solid rgba(0, 198, 255, 0.2);

            background:
                rgba(12, 25, 52, 0.75);

            color: #dcecff;

            font-weight: 600;

            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            border-color: #00c6ff;

            color: #ffffff;

            background:
                rgba(0, 198, 255, 0.10);

            box-shadow:
                0 0 18px rgba(0, 198, 255, 0.16);

            transform:
                translateY(-1px);
        }


        /* ================================
           FOOTER
        ================================= */

        .footer {
            text-align: center;

            color: #566581;

            font-size: 12px;

            margin-top: 40px;
        }


        /* ================================
           MOBILE
        ================================= */

        @media (max-width: 768px) {

            .block-container {
                padding-left: 15px;
                padding-right: 15px;
            }

            .ai-header {
                padding: 14px 16px;
            }

            .hero {
                padding-top: 25px;
            }

            .hero h1 {
                letter-spacing: -1px;
            }

            .brand-subtitle {
                display: none;
            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )


def show_header():
    st.markdown(
        """
        <div class="ai-header">

            <div class="brand">

                <div class="brand-icon">
                    ✦
                </div>

                <div>

                    <div class="brand-title">
                        Study Tutor AI
                    </div>

                    <div class="brand-subtitle">
                        Your intelligent learning companion
                    </div>

                </div>

            </div>

            <div class="online">
                ● AI Online
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def show_hero():
    st.markdown(
        """
        <div class="hero">

            <div class="hero-badge">
                ✦ AI-POWERED LEARNING
            </div>

            <h1>
                Learn smarter.<br>
                Understand deeper.
            </h1>

            <p>
                Your personal AI tutor that explains concepts,
                creates quizzes, checks your answers,
                and helps you learn at your own pace.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


def show_footer():
    st.markdown(
        """
        <div class="footer">
            Built with Streamlit · CrewAI · Groq
        </div>
        """,
        unsafe_allow_html=True
    )
