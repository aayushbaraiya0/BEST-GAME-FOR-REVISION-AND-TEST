# =========================================================
# 🎮 GSEB ONLINE MULTIPLAYER QUIZ GAME
# =========================================================
# RUN:
# pip install streamlit
# streamlit run app.py
# =========================================================

import streamlit as st
import random
import time

# =========================================================
# 🎮 PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="GSEB Multiplayer Quiz",
    page_icon="🎮",
    layout="wide"
)

# =========================================================
# 🌈 RGB UI
# =========================================================

st.markdown("""
<style>

.stApp{
background:linear-gradient(-45deg,#ff0000,#ff00ff,#00ffff,#0011ff,#00ff99,#ff8800);
background-size:400% 400%;
animation:rgb 12s ease infinite;
}

@keyframes rgb{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.mainbox{
background:rgba(0,0,0,0.85);
padding:25px;
border-radius:25px;
border:2px solid cyan;
box-shadow:0 0 25px cyan;
}

.quizbox{
background:rgba(0,0,0,0.9);
padding:20px;
border-radius:25px;
border:2px solid #ff00ff;
margin-top:20px;
box-shadow:0 0 25px #ff00ff;
}

.scorebox{
background:black;
padding:20px;
border-radius:20px;
border:2px solid lime;
text-align:center;
box-shadow:0 0 20px lime;
}

h1,h2,h3,h4{
color:white !important;
text-shadow:0 0 10px cyan;
}

.stButton>button{
width:100%;
height:55px;
font-size:20px;
font-weight:bold;
border-radius:15px;
background:black;
color:cyan;
border:2px solid cyan;
transition:0.3s;
}

.stButton>button:hover{
background:cyan;
color:black;
transform:scale(1.03);
box-shadow:0 0 20px cyan;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# 📚 DATABASE
# =========================================================

database = {

    "Std 10": {

        "ગણિત": {

            "Ch 1: વાસ્તવિક સંખ્યાઓ": [],
            "Ch 2: બહુપદીઓ": [],
            "Ch 3: દ્વિચલ સુરેખ સમીકરણો": [],
            "Ch 4: દ્વિઘાત સમીકરણો": [],
            "Ch 5: સમાંતર શ્રેણી": []

        },

        "વિજ્ઞાન": {

            "Ch 1: રાસાયણિક પ્રક્રિયાઓ અને સમીકરણો": [],
            "Ch 2: ઍસિડ, બેઇઝ અને ક્ષાર": [],
            "Ch 3: ધાતુઓ અને અધાતુઓ": [],
            "Ch 4: કાર્બન અને તેના સંયોજનો": []

        },

        "ગુજરાતી": {

            "Ch 1: વૈષ્ણવજન": [],
            "Ch 2: રેસનો ઘોડો": [],
            "Ch 3: શીલવંત સાધુને": []

        },

        "સામાજિક વિજ્ઞાન": {

            "Ch 1: ભારતનો વારસો": [],
            "Ch 2: ભારતનો સાંસ્કૃતિક વારસો": [],
            "Ch 3: ભારતનો સાહિત્યિક વારસો": []

        }

    }

}

# =========================================================
# 🎲 RANDOM QUESTION GENERATOR
# =========================================================

def generate_question(subject, chapter):

    maths = [

        {
            "question": f"{chapter} મુજબ √144 = ?",
            "options": ["12","14","16","10"],
            "answer": "12"
        },

        {
            "question": f"{chapter} મુજબ sin90° = ?",
            "options": ["1","0","-1","1/2"],
            "answer": "1"
        }

    ]

    science = [

        {
            "question": f"{chapter} માં H2O શું છે?",
            "options": ["પાણી","ઓક્સિજન","મીઠું","એસિડ"],
            "answer": "પાણી"
        },

        {
            "question": f"{chapter} માં CO2 શું છે?",
            "options": [
                "કાર્બન ડાયોક્સાઇડ",
                "ઓક્સિજન",
                "હાઈડ્રોજન",
                "નાઇટ્રોજન"
            ],
            "answer": "કાર્બન ડાયોક્સાઇડ"
        }

    ]

    gujarati = [

        {
            "question": f"{chapter} ગુજરાતી વિષયનો ભાગ છે?",
            "options": ["હા","ના","કદાચ","ખબર નથી"],
            "answer": "હા"
        }

    ]

    ss = [

        {
            "question": f"{chapter} મુજબ ભારતની રાજધાની કઈ?",
            "options": [
                "અમદાવાદ",
                "મુંબઈ",
                "નવી દિલ્હી",
                "ચેન્નઈ"
            ],
            "answer": "નવી દિલ્હી"
        }

    ]

    if subject == "ગણિત":
        return random.choice(maths)

    elif subject == "વિજ્ઞાન":
        return random.choice(science)

    elif subject == "ગુજરાતી":
        return random.choice(gujarati)

    else:
        return random.choice(ss)

# =========================================================
# 🧠 SESSION
# =========================================================

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "questions" not in st.session_state:
    st.session_state.questions = []

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "p1_score" not in st.session_state:
    st.session_state.p1_score = 0

if "p2_score" not in st.session_state:
    st.session_state.p2_score = 0

if "turn" not in st.session_state:
    st.session_state.turn = 1

# =========================================================
# 🎮 TITLE
# =========================================================

st.markdown("""
<h1 style='text-align:center;font-size:60px;'>
🎮 GSEB ONLINE MULTIPLAYER QUIZ
</h1>
""", unsafe_allow_html=True)

# =========================================================
# 👥 MAIN MENU
# =========================================================

st.markdown("<div class='mainbox'>", unsafe_allow_html=True)

player1 = st.text_input(
    "👤 PLAYER 1 NAME"
)

player2 = st.text_input(
    "👤 PLAYER 2 NAME"
)

std = st.selectbox(
    "🏫 SELECT STD",
    list(database.keys())
)

subject = st.selectbox(
    "📚 SELECT SUBJECT",
    list(database[std].keys())
)

chapters = st.multiselect(
    "📖 SELECT CHAPTERS",
    list(database[std][subject].keys())
)

mcq_amount = st.selectbox(
    "📝 MCQ AMOUNT",
    [10,20,50,100]
)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# 🏆 SCOREBOARD
# =========================================================

c1,c2 = st.columns(2)

with c1:

    st.markdown(f"""
    <div class='scorebox'>
    <h2>👤 {player1}</h2>
    <h1>{st.session_state.p1_score}</h1>
    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown(f"""
    <div class='scorebox'>
    <h2>👤 {player2}</h2>
    <h1>{st.session_state.p2_score}</h1>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 🚀 START QUIZ
# =========================================================

if st.button("🚀 START MULTIPLAYER QUIZ"):

    st.session_state.questions = []

    for i in range(mcq_amount):

        random_chapter = random.choice(chapters)

        q = generate_question(
            subject,
            random_chapter
        )

        st.session_state.questions.append(q)

    random.shuffle(st.session_state.questions)

    st.session_state.quiz_started = True
    st.session_state.q_index = 0

    st.session_state.p1_score = 0
    st.session_state.p2_score = 0

    st.session_state.turn = 1

    st.rerun()

# =========================================================
# 🎯 QUIZ SYSTEM
# =========================================================

if st.session_state.quiz_started:

    idx = st.session_state.q_index
    total = len(st.session_state.questions)

    st.progress(idx / total)

    if idx < total:

        q = st.session_state.questions[idx]

        current_player = (
            player1
            if st.session_state.turn == 1
            else player2
        )

        st.markdown(f"""
        <div class='quizbox'>
        <h2>🎯 QUESTION {idx+1}/{total}</h2>
        <h2>⚔️ TURN : {current_player}</h2>
        <h3>{q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)

        answer = st.radio(
            "SELECT ANSWER",
            q["options"],
            index=None,
            key=f"q_{idx}"
        )

        if answer:

            time.sleep(0.5)

            # =================================================
            # ✅ CORRECT
            # =================================================

            if answer == q["answer"]:

                st.success("✅ CORRECT +10")

                if st.session_state.turn == 1:

                    st.session_state.p1_score += 10
                    st.session_state.turn = 2

                else:

                    st.session_state.p2_score += 10
                    st.session_state.turn = 1

            # =================================================
            # ❌ WRONG
            # =================================================

            else:

                st.error(
                    f"❌ WRONG | Correct : {q['answer']}"
                )

                if st.session_state.turn == 1:

                    st.session_state.p1_score -= 5
                    st.session_state.turn = 2

                else:

                    st.session_state.p2_score -= 5
                    st.session_state.turn = 1

            st.session_state.q_index += 1

            st.rerun()

    # =====================================================
    # 🏆 FINAL RESULT
    # =====================================================

    else:

        st.balloons()

        st.markdown("""
        <div class='quizbox'>
        <h1>🏆 MATCH FINISHED</h1>
        </div>
        """, unsafe_allow_html=True)

        if st.session_state.p1_score > st.session_state.p2_score:

            st.success(
                f"🏆 WINNER : {player1}"
            )

        elif st.session_state.p2_score > st.session_state.p1_score:

            st.success(
                f"🏆 WINNER : {player2}"
            )

        else:

            st.warning("🤝 MATCH DRAW")

        if st.button("🔄 PLAY AGAIN"):

            st.session_state.quiz_started = False
            st.session_state.questions = []
            st.session_state.q_index = 0

            st.rerun()
