```python
import streamlit as st
import random
import sqlite3
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ગુજરાતી એક્ઝામ ગેમ",
    page_icon="🎮",
    layout="centered"
)

# ---------------- DATABASE ----------------
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    score INTEGER,
    standard TEXT,
    subject TEXT
)
""")

conn.commit()

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#050816,#0b1633,#111c44);
    color:white;
}

.title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#00ffe7;
    text-shadow:0px 0px 20px #00ffe7;
    margin-bottom:20px;
}

.box{
    background:rgba(255,255,255,0.07);
    padding:20px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.1);
    margin-bottom:20px;
}

.question{
    font-size:28px;
    font-weight:bold;
    color:#ffffff;
}

.chapter{
    color:#00ffe7;
    font-size:18px;
}

.score{
    text-align:center;
    font-size:25px;
    font-weight:bold;
    color:#00ff99;
}

.stButton>button{
    width:100%;
    border-radius:15px;
    height:55px;
    border:none;
    font-size:18px;
    font-weight:bold;
    background:linear-gradient(45deg,#00ffe7,#00aaff);
    color:black;
}

.stButton>button:hover{
    transform:scale(1.03);
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">🎮 ગુજરાતી એક્ઝામ ગેમ 🎮</div>', unsafe_allow_html=True)

# ---------------- QUESTIONS ----------------
questions_data = {
    "ધોરણ 10": {
        "વિજ્ઞાન": [
            {
                "chapter": "રાસાયણિક પ્રતિક્રિયા",
                "question": "મેગ્નેશિયમ રિબન હવામાં બળે ત્યારે શું બને છે?",
                "options": [
                    "મેગ્નેશિયમ ઓક્સાઇડ",
                    "હાઇડ્રોજન",
                    "ક્લોરીન",
                    "કશું નહિ"
                ],
                "answer": "મેગ્નેશિયમ ઓક્સાઇડ"
            },
            {
                "chapter": "જીવન પ્રક્રિયા",
                "question": "પ્રકાશ સંશ્લેષણ માટે જવાબદાર રંગદ્રવ્ય કયું છે?",
                "options": [
                    "હીમોગ્લોબિન",
                    "ક્લોરોફિલ",
                    "મેલાનિન",
                    "કેરોટિન"
                ],
                "answer": "ક્લોરોફિલ"
            }
        ],

        "ગણિત": [
            {
                "chapter": "ત્રિકોણમિતિ",
                "question": "sin²θ + cos²θ = ?",
                "options": [
                    "0",
                    "1",
                    "2",
                    "θ"
                ],
                "answer": "1"
            },
            {
                "chapter": "વૃત્ત",
                "question": "વૃત્તનું ક્ષેત્રફળ શું છે?",
                "options": [
                    "πr²",
                    "2πr",
                    "πd",
                    "r²"
                ],
                "answer": "πr²"
            }
        ]
    }
}

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎯 મેનુ")

player_name = st.sidebar.text_input("તમારું નામ લખો")

standard = st.sidebar.selectbox(
    "ધોરણ પસંદ કરો",
    list(questions_data.keys())
)

subject = st.sidebar.selectbox(
    "વિષય પસંદ કરો",
    list(questions_data[standard].keys())
)

# ---------------- LOAD QUESTIONS ----------------
questions = questions_data[standard][subject]

# ---------------- SESSION ----------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "random_questions" not in st.session_state:
    st.session_state.random_questions = random.sample(
        questions,
        len(questions)
    )

# ---------------- SCORE ----------------
st.markdown(
    f'<div class="score">🏆 સ્કોર : {st.session_state.score}</div>',
    unsafe_allow_html=True
)

# ---------------- END GAME ----------------
if st.session_state.question_index >= len(st.session_state.random_questions):

    st.success("🎉 ગેમ પૂર્ણ થઈ ગઈ!")
    st.balloons()

    if player_name != "":
        c.execute(
            "INSERT INTO scores(name, score, standard, subject) VALUES(?,?,?,?)",
            (
                player_name,
                st.session_state.score,
                standard,
                subject
            )
        )
        conn.commit()

    st.subheader("🏅 લીડરબોર્ડ")

    leaderboard = c.execute(
        "SELECT name, score FROM scores ORDER BY score DESC LIMIT 10"
    ).fetchall()

    for i, row in enumerate(leaderboard, start=1):
        st.write(f"{i}. {row[0]} - {row[1]}")

    if st.button("🔄 ફરીથી રમો"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.random_questions = random.sample(
            questions,
            len(questions)
        )
        st.rerun()

# ---------------- QUESTIONS ----------------
else:

    q = st.session_state.random_questions[
        st.session_state.question_index
    ]

    st.markdown(
        f'''
        <div class="box">
            <div class="chapter">📘 પ્રકરણ : {q['chapter']}</div>
            <br>
            <div class="question">{q['question']}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    selected = st.radio(
        "જવાબ પસંદ કરો",
        q["options"]
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("✅ જવાબ સબમિટ કરો"):

            if selected == q["answer"]:

                st.session_state.score += 1

                st.success("🎉 સાચો જવાબ!")

            else:

                st.error(f"❌ ખોટો જવાબ! સાચો જવાબ : {q['answer']}")

            time.sleep(1)

            st.session_state.question_index += 1

            st.rerun()

    with col2:

        if st.button("⏭ પ્રશ્ન છોડો"):

            st.session_state.question_index += 1

            st.rerun()

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("⚡ ગુજરાતી બોર્ડ એક્ઝામ માટે બનાવેલ ગેમ")
```

# requireme

```txt
streamlit
```
