import streamlit as st
import random
import sqlite3
import time

# ================= 🗄️ ડેટાબેઝ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER, standard TEXT, subject TEXT, chapter TEXT)")
conn.commit()

# ================= 🌈 ડિઝાઈન =================
st.set_page_config(page_title="રિવિઝન ક્વિઝ", layout="centered")
st.markdown("""<style>.stApp { background: #1a1a1a; color: white; }</style>""", unsafe_allow_html=True)

# ================= 📚 ડેટા સ્ટ્રક્ચર =================
data_structure = {
    "ધોરણ ૧૦": {
        "સામાજિક વિજ્ઞાન": [f"પ્રકરણ {i}" for i in range(1, 22)],
        "વિજ્ઞાન": [f"પ્રકરણ {i}" for i in range(1, 14)],
        "ગણિત": [f"પ્રકરણ {i}" for i in range(1, 15)],
        "ગુજરાતી": ["કાવ્ય ૧", "પાઠ ૨", "કાવ્ય ૩", "પાઠ ૪"],
        "અંગ્રેજી": ["Unit 1", "Unit 2", "Unit 3"]
    }
}

# ================= 🤖 પ્રશ્ન એન્જિન (ફિક્સ કરેલું) =================
# અહીં આપણે 3 પેરામીટર સ્વીકારીએ છીએ
def get_dynamic_question(ch, sub, q_index):
    questions = {
        "વિજ્ઞાન": [
            {"પ્રશ્ન": "એસિડ સ્વાદે કેવા હોય છે?", "વિકલ્પો": ["ખાટા", "તૂરા", "કડવા", "મીઠા"], "સાચો": "ખાટા"},
            {"પ્રશ્ન": "પાણીનું રાસાયણિક સૂત્ર શું છે?", "વિકલ્પો": ["H2O", "CO2", "NaCl", "O2"], "સાચો": "H2O"}
        ],
        "સામાજિક વિજ્ઞાન": [
            {"પ્રશ્ન": "તાજમહાલ કોણે બંધાવ્યો?", "વિકલ્પો": ["અકબર", "શાહજહાં", "બાબર", "હુમાયુ"], "સાચો": "શાહજહાં"},
            {"પ્રશ્ન": "લોથલ કયા જિલ્લામાં છે?", "વિકલ્પો": ["અમદાવાદ", "રાજકોટ", "ભાવનગર", "સુરત"], "સાચો": "અમદાવાદ"}
        ],
        "ગણિત": [
            {"પ્રશ્ન": "વર્તુળનો પરિઘ શોધવાનું સૂત્ર?", "વિકલ્પો": ["2πr", "πr²", "2r", "πd"], "સાચો": "2πr"}
        ]
    }
    
    sub_key = next((k for k in questions.keys() if k in sub), "વિજ્ઞાન")
    return random.choice(questions[sub_key])

# ================= 🕹️ ગેમ લોજિક =================
st.title("🎮 રિવિઝન ટેસ્ટ")

std = st.selectbox("ધોરણ પસંદ કરો:", list(data_structure.keys()))
sub = st.selectbox("વિષય પસંદ કરો:", list(data_structure[std].keys()))
ch = st.selectbox("પ્રકરણ પસંદ કરો:", data_structure[std][sub])

if "score" not in st.session_state: st.session_state.score = 0
if "q_num" not in st.session_state: st.session_state.q_num = 1

# હવે 3 પેરામીટર સાથે ફંક્શન કોલ થશે
q = get_dynamic_question(ch, sub, st.session_state.q_num)

st.write(f"### પ્રશ્ન {st.session_state.q_num}: {q['પ્રશ્ન']}")
ans = st.radio("વિકલ્પો:", q["વિકલ્પો"], key=f"r_{st.session_state.q_num}")

if st.button("સબમિટ કરો"):
    if ans == q["સાચો"]:
        st.success("સાચો જવાબ! 🎉")
        st.session_state.score += 10
    else:
        st.error(f"ખોટો! સાચો જવાબ {q['સાચો']} છે.")
        st.session_state.score -= 5
    st.session_state.q_num += 1
    st.rerun()

st.write(f"### તમારો સ્કોર: {st.session_state.score}")
