import streamlit as st
import random
import json
import os
import base64

# ================= PAGE =================

st.set_page_config(
    page_title="ગુજરાતી એક્ઝામ ગેમ",
    page_icon="🎮",
    layout="wide"
)

# ================= SOUND =================

def play_sound(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()

        md = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """

        st.markdown(md, unsafe_allow_html=True)

# ================= CSS =================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#12002f,#32006b,#001f5c);
    color:white;
}

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#00ffff;
    text-shadow:0px 0px 20px cyan;
    margin-bottom:30px;
}

.box{
    background:rgba(0,0,0,0.55);
    padding:25px;
    border-radius:25px;
    border:2px solid cyan;
    box-shadow:0px 0px 25px cyan;
    margin-bottom:20px;
}

.question-box{
    background:rgba(255,255,255,0.08);
    padding:30px;
    border-radius:20px;
    border:2px solid #00ffff;
    box-shadow:0px 0px 20px #00ffff;
}

.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#00ffff,#00ff99);
    color:black;
    border:none;
    border-radius:15px;
    font-size:20px;
    font-weight:bold;
    padding:15px;
}

.stSelectbox label{
    color:white !important;
    font-size:20px !important;
}

.stTextInput label{
    color:white !important;
    font-size:20px !important;
}

.score{
    text-align:center;
    font-size:35px;
    color:#00ff99;
    font-weight:bold;
}

.question{
    font-size:38px;
    font-weight:bold;
    color:white;
}

.chapter{
    font-size:22px;
    color:#00ffff;
}

</style>
""", unsafe_allow_html=True)

# ================= TITLE =================

st.markdown(
    "<div class='main-title'>🎮 ગુજરાતી એક્ઝામ ક્વિઝ ગેમ 🎮</div>",
    unsafe_allow_html=True
)

# ================= DATA =================

quiz_data = {

    "ધોરણ ૧૦": {

        "ગણિત": {

            "વાસ્તવિક સંખ્યાઓ": [

                {
                    "પ્રશ્ન": "૨ અને ૩ નો લઘુત્તમ સમાપવર્તક કેટલો?",
                    "વિકલ્પો": ["૬", "૯", "૩", "૧૨"],
                    "સાચો": "૬"
                },

                {
                    "પ્રશ્ન": "૫ નો વર્ગ કેટલો?",
                    "વિકલ્પો": ["૧૦", "૧૫", "૨૫", "૨૦"],
                    "સાચો": "૨૫"
                },

                {
                    "પ્રશ્ન": "૪ નો ઘન કેટલો?",
                    "વિકલ્પો": ["૧૬", "૩૨", "૬૪", "૪૮"],
                    "સાચો": "૬૪"
                }

            ],

            "ત્રિકોણ": [

                {
                    "પ્રશ્ન": "ત્રિકોણમાં કેટલા ખૂણા હોય છે?",
                    "વિકલ્પો": ["૨", "૩", "૪", "૫"],
                    "સાચો": "૩"
                },

                {
                    "પ્રશ્ન": "સમબાહુ ત્રિકોણની બધી બાજુ કેવી હોય છે?",
                    "વિકલ્પો": ["અસમાન", "બે સમાન", "બધી સમાન", "કોઈ નહીં"],
                    "સાચો": "બધી સમાન"
                }

            ]

        },

        "વિજ્ઞાન": {

            "વિદ્યુત": [

                {
                    "પ્રશ્ન": "ઓહ્મનો નિયમ કયા સંબંધને દર્શાવે છે?",
                    "વિકલ્પો": [
                        "વિદ્યુત પ્રવાહ અને વિભવ તફાવત",
                        "ભાર અને ગતિ",
                        "ઉષ્ણતા અને દબાણ",
                        "લંબાઈ અને સમય"
                    ],
                    "સાચો": "વિદ્યુત પ્રવાહ અને વિભવ તફાવત"
                },

                {
                    "પ્રશ્ન": "વિદ્યુત પ્રવાહનું એકમ શું છે?",
                    "વિકલ્પો": ["વોલ્ટ", "એમ્પિયર", "ઓહ્મ", "વોટ"],
                    "સાચો": "એમ્પિયર"
                }

            ],

            "પ્રકાશ": [

                {
                    "પ્રશ્ન": "પ્રકાશની ગતિ કેટલી છે?",
                    "વિકલ્પો": [
                        "૩×૧૦⁸ મીટર પ્રતિ સેકંડ",
                        "૩×૧૦⁶ મીટર પ્રતિ સેકંડ",
                        "૩×૧૦⁴ મીટર પ્રતિ સેકંડ",
                        "૩×૧૦² મીટર પ્રતિ સેકંડ"
                    ],
                    "સાચો": "૩×૧૦⁸ મીટર પ્રતિ સેકંડ"
                }

            ]

        }

    }

}

# ================= MENU =================

col1, col2 = st.columns([1,2])

with col1:

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    નામ = st.text_input("તમારું નામ લખો")

    ધોરણ = st.selectbox(
        "ધોરણ પસંદ કરો",
        list(quiz_data.keys())
    )

    વિષય = st.selectbox(
        "વિષય પસંદ કરો",
        list(quiz_data[ધોરણ].keys())
    )

    પ્રકરણ = st.selectbox(
        "પ્રકરણ પસંદ કરો",
        list(quiz_data[ધોરણ][વિષય].keys())
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ================= QUESTIONS =================

questions = quiz_data[ધોરણ][વિષય][પ્રકરણ]

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if st.session_state.question_index >= len(questions):
    st.session_state.question_index = 0

q = questions[st.session_state.question_index]

with col2:

    st.markdown("<div class='question-box'>", unsafe_allow_html=True)

    st.markdown(
        f"<div class='chapter'>📘 પ્રકરણ: {પ્રકરણ}</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='score'>🏆 સ્કોર: {st.session_state.score}</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='question'>{q['પ્રશ્ન']}</div>",
        unsafe_allow_html=True
    )

    answer = st.radio(
        "જવાબ પસંદ કરો",
        q["વિકલ્પો"]
    )

    colA, colB = st.columns(2)

    with colA:

        if st.button("જવાબ સબમિટ કરો"):

            if answer == q["સાચો"]:

                st.success("સાચો જવાબ 🎉")

                st.session_state.score += 1

                play_sound("correct.mp3")

            else:

                st.error(f"ખોટો જવાબ ❌")

                st.info(f"સાચો જવાબ: {q['સાચો']}")

                play_sound("wrong.mp3")

    with colB:

        if st.button("આગળનો પ્રશ્ન"):

            st.session_state.question_index += 1

            if st.session_state.question_index >= len(questions):
                st.session_state.question_index = 0

            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
