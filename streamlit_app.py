import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ગુજરાતી એક્ઝામ ગેમ",
    page_icon="🎮",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#020024,#090979,#000428);
    color:white;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#d9d9d9;
    color:black;
}

/* Title */
.main-title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:#00ffe7;
    text-shadow:0px 0px 20px #00ffe7;
    margin-top:20px;
}

/* Score */
.score-box{
    text-align:center;
    font-size:30px;
    color:#00ff66;
    font-weight:bold;
}

/* Question Box */
.question-box{
    background:rgba(255,255,255,0.08);
    padding:30px;
    border-radius:25px;
    border:1px solid rgba(255,255,255,0.1);
    box-shadow:0px 0px 20px rgba(0,255,255,0.3);
    margin-top:20px;
}

/* Buttons */
.stButton>button{
    width:100%;
    background:#00d9ff;
    color:black;
    border:none;
    border-radius:15px;
    padding:12px;
    font-size:18px;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover{
    background:#00ff88;
    transform:scale(1.03);
}

/* Radio */
div[role="radiogroup"] label{
    color:white !important;
    font-size:18px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- DATABASE ----------------

questions_db = {

    "ધોરણ 10": {

        "ગણિત": {

            "પ્રકરણ 1": [
                {
                    "question": "દ્વિઘાત સમીકરણનું સામાન્ય સ્વરૂપ શું છે?",
                    "options": [
                        "ax² + bx + c = 0",
                        "ax + b = 0",
                        "x + y = 0",
                        "a²+b²=c²"
                    ],
                    "answer": "ax² + bx + c = 0"
                },
                {
                    "question": "પાઈનું મૂલ્ય કેટલું છે?",
                    "options": [
                        "3.14",
                        "2.14",
                        "1.14",
                        "4.14"
                    ],
                    "answer": "3.14"
                }
            ],

            "પ્રકરણ 2": [
                {
                    "question": "પાયથાગોરસ સિદ્ધાંત કઈ આકૃતિ માટે છે?",
                    "options": [
                        "સમકોણ ત્રિકોણ",
                        "વર્તુળ",
                        "ચોરસ",
                        "આયત"
                    ],
                    "answer": "સમકોણ ત્રિકોણ"
                }
            ]
        },

        "વિજ્ઞાન": {

            "પ્રકરણ 1": [
                {
                    "question": "ઓહમનો નિયમ કોના સંબંધને દર્શાવે છે?",
                    "options": [
                        "પ્રવાહ અને વિદ્યુત દબાણ",
                        "ભાર અને ગતિ",
                        "દબાણ અને તાપમાન",
                        "પ્રકાશ અને અવાજ"
                    ],
                    "answer": "પ્રવાહ અને વિદ્યુત દબાણ"
                }
            ],

            "પ્રકરણ 2": [
                {
                    "question": "માનવ શરીરમાં હૃદયનું કાર્ય શું છે?",
                    "options": [
                        "રક્ત પંપ કરવું",
                        "શ્વાસ લેવો",
                        "ખોરાક પચાવવો",
                        "વિચાર કરવો"
                    ],
                    "answer": "રક્ત પંપ કરવું"
                }
            ]
        }
    },

    "ધોરણ 9": {

        "ગણિત": {

            "પ્રકરણ 1": [
                {
                    "question": "ત્રિકોણના કોણોનો કુલ સરવાળો કેટલો?",
                    "options": [
                        "180°",
                        "90°",
                        "360°",
                        "270°"
                    ],
                    "answer": "180°"
                }
            ]
        }
    }
}

# ---------------- SESSION ----------------

if "score" not in st.session_state:
    st.session_state.score = 0

if "current_question" not in st.session_state:
    st.session_state.current_question = None

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("## 🎯 મેનુ")

    player_name = st.text_input("તમારું નામ લખો")

    std = st.selectbox(
        "ધોરણ પસંદ કરો",
        list(questions_db.keys())
    )

    subject = st.selectbox(
        "વિષય પસંદ કરો",
        list(questions_db[std].keys())
    )

    chapter = st.selectbox(
        "પ્રકરણ પસંદ કરો",
        list(questions_db[std][subject].keys())
    )

# ---------------- QUESTIONS ----------------

questions = questions_db[std][subject][chapter]

if st.session_state.current_question is None:
    st.session_state.current_question = random.choice(questions)

q = st.session_state.current_question

# ---------------- TITLE ----------------

st.markdown(
    "<div class='main-title'>🎮 ગુજરાતી એક્ઝામ ગેમ 🎮</div>",
    unsafe_allow_html=True
)

st.markdown(
    f"<div class='score-box'>🏆 સ્કોર : {st.session_state.score}</div>",
    unsafe_allow_html=True
)

# ---------------- QUESTION ----------------

st.markdown("<div class='question-box'>", unsafe_allow_html=True)

st.markdown(f"### 📘 {chapter}")

st.markdown(f"# {q['question']}")

answer = st.radio(
    "જવાબ પસંદ કરો",
    q["options"]
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- BUTTONS ----------------

col1, col2 = st.columns(2)

with col1:
    if st.button("✅ જવાબ સબમિટ કરો"):

        if answer == q["answer"]:
            st.success("સાચો જવાબ 🎉")
            st.balloons()
            st.session_state.score += 1
        else:
            st.error(f"ખોટો જવાબ 😢 સાચો જવાબ: {q['answer']}")

with col2:
    if st.button("➡️ પ્રશ્ન બદલો"):
        st.session_state.current_question = random.choice(questions)
        st.rerun()

# ---------------- FOOTER ----------------

st.markdown(
    """
    <br><br>
    <center style='color:gray'>
    Made with ❤️ for Gujarat Students
    </center>
    """,
    unsafe_allow_html=True
)
