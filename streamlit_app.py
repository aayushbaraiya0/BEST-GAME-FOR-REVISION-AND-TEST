# =========================================================
# 🎮 CHANAKYA AI GAME - ULTRA FAST VERSION
# =========================================================

import streamlit as st
from groq import Groq
import random
import json

# =========================================================
# 🎮 PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="🎮 Chanakya AI Game",
    page_icon="🎮",
    layout="centered"
)

# =========================================================
# 🔐 FREE GROQ API
# =========================================================

# CREATE:
# .streamlit/secrets.toml
#
# ADD:
#
# GROQ_API_KEY="your_api_key"

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# =========================================================
# ⚡ FAST CSS
# =========================================================

st.markdown("""
<style>

.stApp {

    background: linear-gradient(
        130deg,
        #ff0000,
        #ff7300,
        #48ff00,
        #00c3ff,
        #7a00ff
    );

    background-size: 400% 400%;

    animation: rgb 12s ease infinite;
}

@keyframes rgb {

    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

h1 {

    color: cyan !important;

    text-align: center;

    text-shadow: 0 0 12px cyan;
}

.main-card {

    background: rgba(0,0,0,0.78);

    padding: 18px;

    border-radius: 15px;

    border: 1px solid cyan;

    margin-bottom: 15px;
}

.stButton>button {

    width: 100%;

    background: black;

    color: cyan;

    border: 1px solid cyan;

    border-radius: 10px;

    font-weight: bold;
}

.stButton>button:hover {

    background: cyan;

    color: black;
}

label,p,span {

    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# 📚 DATABASE
# =========================================================

DB = {

    "Std 6": {

        "Maths": [

            "Knowing Our Numbers",
            "Whole Numbers",
            "Fractions",
            "Decimals",
            "Mensuration",
            "Algebra"
        ],

        "Science": [

            "Food",
            "Components of Food",
            "Plants",
            "Water",
            "Electricity",
            "Magnets"
        ]
    },

    "Std 7": {

        "Maths": [

            "Integers",
            "Fractions",
            "Simple Equations",
            "Triangles",
            "Perimeter and Area"
        ],

        "Science": [

            "Nutrition",
            "Heat",
            "Acids Bases and Salts",
            "Respiration",
            "Light"
        ]
    },

    "Std 8": {

        "Maths": [

            "Rational Numbers",
            "Linear Equations",
            "Squares",
            "Graphs",
            "Factorisation"
        ],

        "Science": [

            "Metals",
            "Coal",
            "Combustion",
            "Cell",
            "Sound"
        ]
    },

    "Std 9": {

        "Maths": [

            "Number Systems",
            "Polynomials",
            "Triangles",
            "Circles",
            "Statistics"
        ],

        "Science": [

            "Matter",
            "Atoms",
            "Motion",
            "Gravitation",
            "Sound"
        ]
    },

    "Std 10": {

        "Maths": [

            "Real Numbers",
            "Polynomials",
            "Quadratic Equations",
            "Trigonometry",
            "Probability"
        ],

        "Science": [

            "Chemical Reactions",
            "Acids Bases and Salts",
            "Carbon",
            "Electricity",
            "Environment"
        ]
    }
}

# =========================================================
# ⚡ FAST BULK QUESTION GENERATOR
# =========================================================

@st.cache_data(show_spinner=False)

def generate_questions(std, subject, chapter, total_questions):

    prompt = f"""
    Generate {total_questions} MCQ questions in Gujarati.

    Standard: {std}
    Subject: {subject}
    Chapter: {chapter}

    Return ONLY valid JSON list.

    Example:

    [
      {{
        "question":"...",
        "options":["A","B","C","D"],
        "answer":"A"
      }}
    ]
    """

    try:

        response = client.chat.completions.create(

            model="llama3-8b-8192",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7,

            max_tokens=3000
        )

        text = response.choices[0].message.content

        start = text.find("[")
        end = text.rfind("]") + 1

        json_text = text[start:end]

        questions = json.loads(json_text)

        valid_questions = []

        for q in questions:

            if (
                "question" in q
                and "options" in q
                and "answer" in q
                and len(q["options"]) == 4
            ):

                valid_questions.append(q)

        return valid_questions

    except Exception as e:

        st.error(f"AI Error: {e}")

        return []

# =========================================================
# 🧠 AI CHAT
# =========================================================

def ask_ai(user_question):

    try:

        response = client.chat.completions.create(

            model="llama3-8b-8192",

            messages=[

                {
                    "role": "system",

                    "content": """
                    You are Chanakya AI.

                    Explain in simple Gujarati.
                    """
                },

                {
                    "role": "user",
                    "content": user_question
                }
            ],

            temperature=0.7,

            max_tokens=400
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Error: {e}"

# =========================================================
# 🏆 RANK SYSTEM
# =========================================================

def get_rank(score):

    if score >= 200:
        return "👑 MASTER"

    elif score >= 120:
        return "🔥 PRO"

    elif score >= 60:
        return "⚡ PLAYER"

    return "🎮 BEGINNER"

# =========================================================
# 🎯 SESSION STATES
# =========================================================

if "mode" not in st.session_state:
    st.session_state.mode = "setup"

if "questions" not in st.session_state:
    st.session_state.questions = []

if "index" not in st.session_state:
    st.session_state.index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "player" not in st.session_state:
    st.session_state.player = "Aayush"

if "ai_open" not in st.session_state:
    st.session_state.ai_open = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =========================================================
# 🎮 TITLE
# =========================================================

st.markdown(
    "<h1>🎮 CHANAKYA AI GAME</h1>",
    unsafe_allow_html=True
)

# =========================================================
# 🎮 SETUP PAGE
# =========================================================

if st.session_state.mode == "setup":

    st.markdown(
        "<div class='main-card'>",
        unsafe_allow_html=True
    )

    st.subheader("⚙️ GAME LOBBY")

    st.session_state.player = st.text_input(
        "✍️ Enter Name",
        value=st.session_state.player
    )

    std = st.selectbox(
        "🎯 Select Standard",
        list(DB.keys())
    )

    subject = st.selectbox(
        "📚 Select Subject",
        list(DB[std].keys())
    )

    chapter = st.selectbox(
        "📖 Select Chapter",
        DB[std][subject]
    )

    total_questions = st.selectbox(
        "📊 Questions",
        [10, 20, 30]
    )

    if st.button("🚀 START GAME"):

        with st.spinner("🧠 AI generating questions..."):

            questions = generate_questions(
                std,
                subject,
                chapter,
                total_questions
            )

        if len(questions) > 0:

            random.shuffle(questions)

            st.session_state.questions = questions

            st.session_state.index = 0

            st.session_state.score = 0

            st.session_state.mode = "play"

            st.rerun()

        else:

            st.error("Failed to generate questions.")

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# =========================================================
# 🎮 PLAY PAGE
# =========================================================

elif st.session_state.mode == "play":

    st.markdown(
        "<div class='main-card'>",
        unsafe_allow_html=True
    )

    st.write(
        f"👤 Player: {st.session_state.player}"
    )

    st.write(
        f"🏆 Rank: {get_rank(st.session_state.score)}"
    )

    st.write(
        f"🎯 Score: {st.session_state.score}"
    )

    total = len(st.session_state.questions)

    index = st.session_state.index

    st.progress(index / total)

    if index < total:

        q = st.session_state.questions[index]

        st.subheader(
            f"Q{index+1}. {q['question']}"
        )

        answer = st.radio(
            "Choose Answer:",
            q["options"],
            key=f"question_{index}"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button("✅ Submit"):

                if answer == q["answer"]:

                    st.success("🎯 Correct!")

                    st.session_state.score += 10

                else:

                    st.error(
                        f"❌ Wrong!\n\nCorrect: {q['answer']}"
                    )

                    st.session_state.score -= 5

                st.session_state.index += 1

                st.rerun()

        with col2:

            if st.button("🧠 Explain"):

                explanation = ask_ai(
                    f"""
                    Explain this in Gujarati:

                    Question:
                    {q['question']}

                    Answer:
                    {q['answer']}
                    """
                )

                st.info(explanation)

    else:

        st.balloons()

        st.success(
            f"🏆 Game Completed {st.session_state.player}"
        )

        st.write(
            f"🔥 Final Score: {st.session_state.score}"
        )

        st.write(
            f"👑 Final Rank: {get_rank(st.session_state.score)}"
        )

        if st.button("🔄 Play Again"):

            st.session_state.mode = "setup"

            st.rerun()

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# =========================================================
# 🧠 AI SIDEBAR
# =========================================================

st.write("---")

if st.button("🧠 OPEN / CLOSE AI"):

    st.session_state.ai_open = (
        not st.session_state.ai_open
    )

    st.rerun()

if st.session_state.ai_open:

    st.markdown(
        "<div class='main-card'>",
        unsafe_allow_html=True
    )

    st.subheader("🧠 Chanakya AI")

    for msg in st.session_state.chat_history[-10:]:

        with st.chat_message(msg["role"]):

            st.write(msg["content"])

    user_input = st.chat_input(
        "Ask anything..."
    )

    if user_input:

        st.session_state.chat_history.append({

            "role": "user",
            "content": user_input
        })

        ai_reply = ask_ai(user_input)

        st.session_state.chat_history.append({

            "role": "assistant",
            "content": ai_reply
        })

        st.rerun()

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )
