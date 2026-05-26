# =========================================================
# 🎮 CHANAKYA AI GAME - FULL NCERT EDITION
# =========================================================

import streamlit as st
import random
from groq import Groq
import base64

# =========================================================
# 🎮 PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="🎮 Chanakya AI Game",
    page_icon="🎮",
    layout="centered"
)

# =========================================================
# 🔐 GROQ API
# =========================================================

# CREATE:
# .streamlit/secrets.toml
#
# ADD:
# GROQ_API_KEY="your_groq_api_key"

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# =========================================================
# 🔊 SOUND SYSTEM
# =========================================================

def autoplay_audio(file_path):

    with open(file_path, "rb") as f:

        data = f.read()

    b64 = base64.b64encode(data).decode()

    md = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.markdown(md, unsafe_allow_html=True)

# =========================================================
# 🌈 RGB GAMING CSS
# =========================================================

st.markdown("""
<style>

.stApp {

    background: linear-gradient(
        124deg,
        #ff0000,
        #ff7300,
        #fffb00,
        #48ff00,
        #00ffd5,
        #002bff,
        #7a00ff,
        #ff00ab
    );

    background-size: 1800% 1800%;

    animation: rgb 15s ease infinite;
}

@keyframes rgb {

    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

h1 {

    color: cyan !important;

    text-align: center;

    text-shadow: 0 0 20px cyan;
}

.question-card {

    background: rgba(0,0,0,0.8);

    padding: 20px;

    border-radius: 15px;

    border: 2px solid cyan;

    box-shadow: 0 0 20px cyan;

    margin-bottom: 15px;
}

.ai-box {

    background: rgba(0,0,0,0.85);

    border: 2px dashed cyan;

    border-radius: 15px;

    padding: 15px;
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

    box-shadow: 0 0 20px cyan;
}

label,p,span {

    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# 🎵 BACKGROUND MUSIC
# =========================================================

if "music_started" not in st.session_state:

    st.session_state.music_started = True

    autoplay_audio("sounds/bgmusic.mp3")

# =========================================================
# 🧠 CHANAKYA AI
# =========================================================

def ask_chanakya_ai(question):

    try:

        response = client.chat.completions.create(

            model="llama3-70b-8192",

            messages=[

                {
                    "role": "system",

                    "content": """
                    You are Chanakya AI.

                    You teach students from Std 6 to Std 10.

                    Explain in Gujarati.

                    Make answers simple and motivating.
                    """
                },

                {
                    "role": "user",
                    "content": question
                }
            ],

            temperature=0.7,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"⚠️ AI Error: {e}"

# =========================================================
# 📚 FULL NCERT DATABASE
# =========================================================

if "base_db" not in st.session_state:

    st.session_state.base_db = {

        "Std 6": {

            "ગણિત (Maths)": [

                "Knowing Our Numbers",
                "Whole Numbers",
                "Playing with Numbers",
                "Basic Geometrical Ideas",
                "Understanding Elementary Shapes",
                "Integers",
                "Fractions",
                "Decimals",
                "Data Handling",
                "Mensuration",
                "Algebra",
                "Ratio and Proportion",
                "Symmetry",
                "Practical Geometry"
            ],

            "વિજ્ઞાન (Science)": [

                "Food",
                "Components of Food",
                "Fibre to Fabric",
                "Sorting Materials",
                "Separation of Substances",
                "Changes Around Us",
                "Getting to Know Plants",
                "Body Movements",
                "Living Organisms",
                "Motion and Measurement",
                "Light",
                "Electricity",
                "Fun with Magnets",
                "Water",
                "Air Around Us",
                "Garbage In Garbage Out"
            ]
        },

        "Std 7": {

            "ગણિત (Maths)": [

                "Integers",
                "Fractions and Decimals",
                "Data Handling",
                "Simple Equations",
                "Lines and Angles",
                "The Triangle",
                "Congruence of Triangles",
                "Comparing Quantities",
                "Rational Numbers",
                "Practical Geometry",
                "Perimeter and Area",
                "Algebraic Expressions",
                "Exponents and Powers",
                "Symmetry",
                "Visualising Solid Shapes"
            ],

            "વિજ્ઞાન (Science)": [

                "Nutrition in Plants",
                "Nutrition in Animals",
                "Heat",
                "Acids Bases and Salts",
                "Physical and Chemical Changes",
                "Respiration",
                "Transportation",
                "Motion and Time",
                "Electric Current",
                "Light"
            ]
        },

        "Std 8": {

            "ગણિત (Maths)": [

                "Rational Numbers",
                "Linear Equations",
                "Understanding Quadrilaterals",
                "Practical Geometry",
                "Data Handling",
                "Squares and Square Roots",
                "Cubes and Cube Roots",
                "Comparing Quantities",
                "Algebraic Expressions",
                "Mensuration",
                "Exponents",
                "Factorisation",
                "Graphs"
            ],

            "વિજ્ઞાન (Science)": [

                "Crop Production",
                "Microorganisms",
                "Synthetic Fibres",
                "Metals and Non Metals",
                "Coal and Petroleum",
                "Combustion",
                "Cell",
                "Reproduction",
                "Force and Pressure",
                "Friction",
                "Sound",
                "Light"
            ]
        },

        "Std 9": {

            "ગણિત (Maths)": [

                "Number Systems",
                "Polynomials",
                "Coordinate Geometry",
                "Linear Equations",
                "Euclid Geometry",
                "Lines and Angles",
                "Triangles",
                "Quadrilaterals",
                "Circles",
                "Herons Formula",
                "Surface Areas and Volumes",
                "Statistics",
                "Probability"
            ],

            "વિજ્ઞાન (Science)": [

                "Matter Around Us",
                "Pure Substances",
                "Atoms and Molecules",
                "Structure of Atom",
                "Cell",
                "Tissues",
                "Motion",
                "Force and Laws",
                "Gravitation",
                "Work and Energy",
                "Sound",
                "Natural Resources"
            ]
        },

        "Std 10": {

            "ગણિત (Maths)": [

                "Real Numbers",
                "Polynomials",
                "Pair of Linear Equations",
                "Quadratic Equations",
                "Arithmetic Progressions",
                "Triangles",
                "Coordinate Geometry",
                "Introduction to Trigonometry",
                "Applications of Trigonometry",
                "Circles",
                "Areas Related to Circles",
                "Surface Areas and Volumes",
                "Statistics",
                "Probability"
            ],

            "વિજ્ઞાન (Science)": [

                "Chemical Reactions",
                "Acids Bases and Salts",
                "Metals and Non Metals",
                "Carbon and Compounds",
                "Periodic Classification",
                "Life Processes",
                "Control and Coordination",
                "Reproduction",
                "Heredity",
                "Light Reflection",
                "Human Eye",
                "Electricity",
                "Magnetic Effects",
                "Energy Sources",
                "Environment"
            ]
        }
    }

# =========================================================
# 🤖 AI QUESTION GENERATOR
# =========================================================

def generate_ai_question(std, subject, chapter):

    prompt = f"""
    Generate 1 Gujarati MCQ question.

    Standard: {std}
    Subject: {subject}
    Chapter: {chapter}

    Return EXACTLY like this:

    QUESTION: ...
    OPTION1: ...
    OPTION2: ...
    OPTION3: ...
    OPTION4: ...
    ANSWER: ...
    """

    try:

        response = client.chat.completions.create(

            model="llama3-70b-8192",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.8,
            max_tokens=300
        )

        text = response.choices[0].message.content

        lines = text.split("\n")

        question = ""
        options = []
        answer = ""

        for line in lines:

            if line.startswith("QUESTION:"):

                question = line.replace(
                    "QUESTION:",
                    ""
                ).strip()

            elif line.startswith("OPTION"):

                options.append(
                    line.split(":",1)[1].strip()
                )

            elif line.startswith("ANSWER:"):

                answer = line.replace(
                    "ANSWER:",
                    ""
                ).strip()

        if len(options) < 4:

            return None

        return {

            "question": question,
            "options": options,
            "answer": answer
        }

    except:

        return None

# =========================================================
# 🏆 RANK SYSTEM
# =========================================================

def get_rank(score):

    if score >= 500:
        return "👑 MASTER"

    elif score >= 300:
        return "🔥 PRO"

    elif score >= 150:
        return "⚡ PLAYER"

    return "🎮 BEGINNER"

# =========================================================
# 🎯 SESSION STATE
# =========================================================

if "player_name" not in st.session_state:
    st.session_state.player_name = "Aayush"

if "score" not in st.session_state:
    st.session_state.score = 100

if "game_mode" not in st.session_state:
    st.session_state.game_mode = "SETUP"

if "questions" not in st.session_state:
    st.session_state.questions = []

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "ai_open" not in st.session_state:
    st.session_state.ai_open = False

# =========================================================
# 🎮 TITLE
# =========================================================

st.markdown(
    "<h1>🎮 CHANAKYA AI GAME 🎮</h1>",
    unsafe_allow_html=True
)

# =========================================================
# 🎮 GAME SETUP
# =========================================================

if st.session_state.game_mode == "SETUP":

    st.subheader("⚙️ GAME LOBBY")

    st.session_state.player_name = st.text_input(
        "✍️ નામ લખો:",
        value=st.session_state.player_name
    )

    std = st.selectbox(
        "🎯 ધોરણ",
        list(st.session_state.base_db.keys())
    )

    subject = st.selectbox(
        "📚 વિષય",
        list(st.session_state.base_db[std].keys())
    )

    chapter = st.selectbox(
        "📖 પ્રકરણ",
        st.session_state.base_db[std][subject]
    )

    total_questions = st.selectbox(
        "📊 પ્રશ્નો",
        [10,20,50]
    )

    if st.button("🚀 START GAME"):

        questions = []

        with st.spinner("🧠 AI પ્રશ્નો બનાવી રહ્યું છે..."):

            while len(questions) < total_questions:

                q = generate_ai_question(
                    std,
                    subject,
                    chapter
                )

                if q is not None:

                    questions.append(q)

        random.shuffle(questions)

        st.session_state.questions = questions

        st.session_state.question_index = 0

        st.session_state.score = 100

        st.session_state.game_mode = "PLAY"

        st.rerun()

# =========================================================
# 🎮 PLAY MODE
# =========================================================

elif st.session_state.game_mode == "PLAY":

    st.subheader(
        f"🕹️ PLAYER: {st.session_state.player_name}"
    )

    st.info(
        f"🏆 Rank: {get_rank(st.session_state.score)}"
    )

    st.markdown(
        f"### 🎯 Score: {st.session_state.score}"
    )

    index = st.session_state.question_index

    total = len(st.session_state.questions)

    st.progress((index + 1) / total)

    if st.session_state.score <= 0:

        autoplay_audio("sounds/gameover.mp3")

        st.error("💀 GAME OVER")

        if st.button("🔄 Restart"):

            st.session_state.game_mode = "SETUP"

            st.rerun()

    elif index < total:

        q = st.session_state.questions[index]

        st.markdown(f"""
        <div class="question-card">
        <h3>{q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)

        user_answer = st.radio(
            "સાચો જવાબ પસંદ કરો:",
            q["options"],
            key=f"q_{index}"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button("✅ Submit"):

                if user_answer == q["answer"]:

                    autoplay_audio("sounds/correct.mp3")

                    st.success("🎯 સાચો જવાબ! +10")

                    st.session_state.score += 10

                else:

                    autoplay_audio("sounds/wrong.mp3")

                    st.error(
                        f"❌ ખોટો જવાબ!\n\nસાચો જવાબ: {q['answer']}"
                    )

                    st.session_state.score -= 50

                st.session_state.question_index += 1

                st.rerun()

        with col2:

            if st.button("🧠 Explain"):

                explanation = ask_chanakya_ai(f"""

                પ્રશ્ન:
                {q['question']}

                સાચો જવાબ:
                {q['answer']}

                ગુજરાતીમાં સમજાવો.
                """)

                st.info(explanation)

    else:

        autoplay_audio("sounds/win.mp3")

        st.balloons()

        st.success(
            f"🏆 CONGRATULATIONS {st.session_state.player_name}"
        )

        if st.button("🏁 PLAY AGAIN"):

            st.session_state.game_mode = "SETUP"

            st.rerun()

# =========================================================
# 🧠 AI CHAT
# =========================================================

st.write("---")

if st.button("🧠 OPEN / CLOSE AI"):

    st.session_state.ai_open = not st.session_state.ai_open

    st.rerun()

if st.session_state.ai_open:

    st.markdown(
        "<div class='ai-box'>",
        unsafe_allow_html=True
    )

    st.subheader("🧠 CHANAKYA AI")

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

    for chat in st.session_state.chat_history:

        with st.chat_message(chat["role"]):

            st.write(chat["message"])

    user_msg = st.chat_input("અહીં પ્રશ્ન પૂછો...")

    if user_msg:

        st.session_state.chat_history.append({

            "role": "user",
            "message": user_msg
        })

        reply = ask_chanakya_ai(user_msg)

        st.session_state.chat_history.append({

            "role": "assistant",
            "message": reply
        })

        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
