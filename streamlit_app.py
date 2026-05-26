import streamlit as st
import random
import sqlite3
import time

# ================= 🗄️ ડેટાબેઝ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER, standard TEXT, subject TEXT, chapter TEXT)")
conn.commit()

# ================= 📚 સંપૂર્ણ વિષય અને પ્રકરણ ડેટા =================
# બધા જ વિષયો અને તેના ચોક્કસ પ્રકરણો અહીં છે
data_structure = {
    "ધોરણ ૧૦": {
        "સામાજિક વિજ્ઞાન": [f"પ્રકરણ {i}" for i in range(1, 22)],
        "વિજ્ઞાન": [f"પ્રકરણ {i}" for i in range(1, 14)],
        "ગણિત": [f"પ્રકરણ {i}" for i in range(1, 15)],
        "ગુજરાતી": ["કાવ્ય ૧", "પાઠ ૨", "કાવ્ય ૩", "પાઠ ૪"],
        "અંગ્રેજી": ["Unit 1", "Unit 2", "Unit 3"]
    }
}

# ================= 🤖 પ્રશ્ન એન્જિન (વિષય અને પ્રકરણ સાથે) =================
def get_q(ch, sub):
    # અહીં દરેક વિષય માટેના પ્રશ્નોનું પૂલ છે
    questions = {
        "વિજ્ઞાન": [
            {"પ્રશ્ન": f"{ch} માંથી: એસિડ સ્વાદે કેવા હોય છે?", "વિકલ્પો": ["ખાટા", "તૂરા", "કડવા", "મીઠા"], "સાચો": "ખાટા"},
            {"પ્રશ્ન": f"{ch} માંથી: ભૂરા લિટમસ પત્રને લાલ કોણ બનાવે છે?", "વિકલ્પો": ["એસિડ", "બેઇઝ", "ક્ષાર", "પાણી"], "સાચો": "એસિડ"}
        ],
        "સામાજિક વિજ્ઞાન": [
            {"પ્રશ્ન": f"{ch} માંથી: તાજમહાલ કોણે બંધાવ્યો?", "વિકલ્પો": ["અકબર", "શાહજહાં", "બાબર", "હુમાયુ"], "સાચો": "શાહજહાં"},
            {"પ્રશ્ન": f"{ch} માંથી: ભારતનો કયો પાક ખરીફ પાક છે?", "વિકલ્પો": ["ડાંગર", "ઘઉં", "ચણા", "રાઈ"], "સાચો": "ડાંગર"}
        ],
        "ગણિત": [
            {"પ્રશ્ન": f"{ch} માંથી: વર્તુળનો પરિઘ શોધવાનું સૂત્ર?", "વિકલ્પો": ["2πr", "πr²", "2r", "πd"], "સાચો": "2πr"},
            {"પ્રશ્ન": f"{ch} માંથી: પાયથાગોરસ પ્રમેય કયા ત્રિકોણ માટે છે?", "વિકલ્પો": ["કાટકોણ", "લઘુકોણ", "ગુરુકોણ", "સમબાજુ"], "સાચો": "કાટકોણ"}
        ]
    }
    
    # વિષય મુજબ પ્રશ્નો મેળવો, જો ન મળે તો ડિફોલ્ટ પ્રશ્ન આપો
    sub_key = next((k for k in questions.keys() if k in sub), "વિજ્ઞાન")
    return random.choice(questions[sub_key])

# ================= 🕹️ ગેમ લોજિક =================
st.title("🎮 રિવિઝન ટેસ્ટ")

std = st.selectbox("ધોરણ પસંદ કરો:", list(data_structure.keys()))
sub = st.selectbox("વિષય પસંદ કરો:", list(data_structure[std].keys()))
ch = st.selectbox("પ્રકરણ પસંદ કરો:", data_structure[std][sub])
quiz_limit = st.selectbox("કેટલા પ્રશ્નો?", [10, 20])

if "q_idx" not in st.session_state: st.session_state.q_idx = 1
if "score" not in st.session_state: st.session_state.score = 0

q = get_dynamic_question(ch, sub, st.session_state.q_idx)
st.write(f"### {q['પ્રશ્ન']}")

# 🚨 સાચો સ્પેલિંગ 'વિકલ્પો' વાપર્યો છે
ans = st.radio("વિકલ્પો:", q["વિકલ્પો"], key=f"r_{st.session_state.q_idx}")

if st.button("સબમિટ કરો"):
    if ans == q["સાચો"]:
        st.success("સાચો જવાબ! +10")
        st.session_state.score += 10
    else:
        st.error(f"ખોટો જવાબ! સાચો: {q['સાચો']}")
        st.session_state.score -= 5
    st.session_state.q_idx += 1
    st.rerun()

st.write(f"### સ્કોર: {st.session_state.score}")
