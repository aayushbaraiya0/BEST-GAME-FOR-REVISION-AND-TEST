import streamlit as st
import random

# =========================
# પેજ સેટિંગ
# =========================

st.set_page_config(
    page_title="ગુજરાતી એક્ઝામ ગેમ",
    page_icon="🎮",
    layout="wide"
)

# =========================
# CSS UI
# =========================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#1e1b4b,#312e81,#7e22ce);
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#d1d5db;
    border-right:2px solid #444;
}

/* Main container */
.main-box{
    background:#070114;
    border:2px solid cyan;
    border-radius:25px;
    padding:25px;
    box-shadow:0px 0px 20px cyan;
    margin-bottom:20px;
}

/* Title */
.title{
    text-align:center;
    color:white;
    font-size:55px;
    font-weight:bold;
    text-shadow:0px 0px 20px cyan;
}

/* Question box */
.question-box{
    background:#0b1020;
    border:2px solid cyan;
    border-radius:20px;
    padding:25px;
    margin-top:20px;
    box-shadow:0px 0px 15px #06b6d4;
}

/* Small heading */
.small-head{
    color:cyan;
    font-size:24px;
    font-weight:bold;
}

/* Score */
.score{
    color:#22c55e;
    font-size:35px;
    font-weight:bold;
}

/* Button */
.stButton button{
    width:100%;
    background:linear-gradient(90deg,#06b6d4,#2563eb);
    color:white;
    border:none;
    border-radius:15px;
    padding:12px;
    font-size:20px;
    font-weight:bold;
}

.stButton button:hover{
    transform:scale(1.02);
    box-shadow:0px 0px 15px cyan;
}

/* Radio text */
.stRadio label{
    color:white !important;
    font-size:20px !important;
}

/* Selectbox */
.stSelectbox label{
    color:white !important;
    font-size:18px !important;
}

/* Input */
.stTextInput label{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# પ્રશ્ન ડેટા
# =========================

questions = {

    "ધોરણ ૧૦": {

        "ગણિત": {

            "વાસ્તવિક સંખ્યાઓ": [
                {
                    "question": "૨ અને ૫ સિવાય અન્ય અવયવ ધરાવતી હરવાળી સંખ્યા કેવી દશાંશ આપે?",
                    "options": [
                        "અસીમ આવર્ત દશાંશ",
                        "સીમિત દશાંશ",
                        "પૂર્ણાંક",
                        "પ્રાકૃતિક સંખ્યા"
                    ],
                    "answer": "અસીમ આવર્ત દશાંશ"
                }
            ],

            "ત્રિકોણમિતિ": [
                {
                    "question": "sin²θ + cos²θ નું મૂલ્ય શું છે?",
                    "options": [
                        "૧",
                        "૦",
                        "૨",
                        "અનંત"
                    ],
                    "answer": "૧"
                }
            ],

            "વૃત્ત": [
                {
                    "question": "વૃત્તની ત્રિજ્યા ૭ હોય તો વ્યાસ કેટલો?",
                    "options": [
                        "૭",
                        "૧૪",
                        "૨૧",
                        "૨૮"
                    ],
                    "answer": "૧૪"
                }
            ]
        },

        "વિજ્ઞાન": {

            "વિદ્યુત": [
                {
                    "question": "ઓહમનો નિયમ કોના સંબંધને દર્શાવે છે?",
                    "options": [
                        "વિભવાંતર અને વિદ્યુત પ્રવાહ",
                        "ભાર અને ગતિ",
                        "તાપ અને ઊર્જા",
                        "દબાણ અને ઘનફળ"
                    ],
                    "answer": "વિભવાંતર અને વિદ્યુત પ્રવાહ"
                }
            ],

            "પ્રકાશ": [
                {
                    "question": "અવતલ દર્પણ ક્યાં ઉપયોગી છે?",
                    "options": [
                        "વાહનના હેડલાઇટમાં",
                        "પંખામાં",
                        "ઘડિયાળમાં",
                        "દરવાજામાં"
                    ],
                    "answer": "વાહનના હેડલાઇટમાં"
                }
            ]
        }
    }
}

# =========================
# સેશન
# =========================

if "score" not in st.session_state:
    st.session_state.score = 0

if "refresh" not in st.session_state:
    st.session_state.refresh = 0

# =========================
# Sidebar
# =========================

st.sidebar.markdown("## 🎮 રમત મેનુ")

name = st.sidebar.text_input("તમારું નામ લખો")

std = st.sidebar.selectbox(
    "ધોરણ પસંદ કરો",
    list(questions.keys())
)

subject = st.sidebar.selectbox(
    "વિષય પસંદ કરો",
    list(questions[std].keys())
)

chapter = st.sidebar.selectbox(
    "પ્રકરણ પસંદ કરો",
    list(questions[std][subject].keys())
)

# =========================
# પ્રશ્ન પસંદ
# =========================

question_data = random.choice(
    questions[std][subject][chapter]
)

question = question_data["question"]
options = question_data["options"]
answer = question_data["answer"]

# =========================
# UI Layout
# =========================

col1, col2 = st.columns([3,1])

# =========================
# LEFT SIDE
# =========================

with col1:

    st.markdown("""
    <div class="main-box">
    <div class="title">
    🎮 BEST GAME FOR REVISION AND TEST
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="main-box">
    <div class="small-head">
    ⚙️ રમત સેટઅપ
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="question-box">
    <div class="small-head">
    📘 પ્રકરણ : {chapter}
    </div>

    <br>

    <h2 style='color:white;'>
    {question}
    </h2>
    </div>
    """, unsafe_allow_html=True)

    selected = st.radio(
        "જવાબ પસંદ કરો",
        options
    )

    c1, c2 = st.columns(2)

    with c1:
        if st.button("✅ જવાબ સબમિટ કરો"):

            if selected == answer:
                st.success("સાચો જવાબ 🎉")
                st.session_state.score += 1
            else:
                st.error(f"ખોટો જવાબ ❌ સાચો જવાબ : {answer}")

    with c2:
        if st.button("🔄 નવો પ્રશ્ન"):

            st.rerun()

# =========================
# RIGHT SIDE
# =========================

with col2:

    st.markdown(f"""
    <div class="main-box">
    <div class="small-head">
    🏆 સ્કોર સેન્ટર
    </div>

    <br>

    <div class="score">
    {st.session_state.score}
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="main-box">
    <div class="small-head">
    🧠 સ્ટડી મોડ
    </div>

    <br>

    <p style='color:white;font-size:18px;'>
    દરરોજ પ્રેક્ટિસ કરો અને પરીક્ષામાં વધુ ગુણ મેળવો.
    </p>

    </div>
    """, unsafe_allow_html=True)
