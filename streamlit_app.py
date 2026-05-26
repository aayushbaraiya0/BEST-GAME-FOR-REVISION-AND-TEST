import streamlit as st
import sqlite3

# ================= 🗄️ ડેટાબેઝ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, score INTEGER)")
conn.commit()

# ================= 🎨 ડિઝાઈન =================
st.set_page_config(page_title="REVISION GAME", layout="centered")
st.markdown("""
<style>
.main-box { background: rgba(0,0,0,0.8); padding: 20px; border-radius: 15px; border: 3px solid #000000; color: white; margin-bottom: 20px; }
.leader-box { border: 3px solid #000000; padding: 20px; border-radius: 15px; background: rgba(0,0,0,0.9); color: white; margin-top: 20px; }
div.stButton > button { background-color: #333333 !important; color: white !important; border: 2px solid #000000 !important; font-weight: bold !important; width: 100%; }
</style>
""", unsafe_allow_html=True)

# ================= 📚 ડેટા સ્ટ્રક્ચર (ધોરણ ૧૦ NCERT) =================
subjects_std10 = ["સામાજિક વિજ્ઞાન", "વિજ્ઞાન", "ગણિત", "ગુજરાતી", "અંગ્રેજી", "હિન્દી", "સંસ્કૃત"]

# ================= 🕹️ ગેમ લોજિક =================
st.title("🎮 BEST GAME FOR REVISION")

# ઇનપુટ બોક્સ
name = st.text_input("✍️ તમારું નામ:", "આયુષ")
std = st.selectbox("🎯 ધોરણ:", ["ધોરણ 10"])
sub = st.selectbox("📚 વિષય:", subjects_std10)
ch = st.selectbox("📖 પ્રકરણ:", ["પ્રકરણ ૧", "પ્રકરણ ૨", "પ્રકરણ ૩", "પ્રકરણ ૪", "પ્રકરણ ૫"])
q_amount = st.selectbox("🔢 કેટલા વિકલ્પ (MCQ) રમવા છે?", [10, 20, 30, 50, 100])

if "score" not in st.session_state: st.session_state.score = 0

# સ્કોર
st.write(f"### 🏆 ચાલુ સ્કોર: {st.session_state.score}")

# પ્રશ્ન એરિયા
st.markdown("<div class='main-box'>", unsafe_allow_html=True)
st.write(f"### 📖 પ્રકરણ: {ch}")
st.write(f"### ❓ પ્રશ્ન: અહીં તમારો સવાલ દેખાશે...")
ans = st.radio("તમારો જવાબ પસંદ કરો:", ["વિકલ્પ ૧", "વિકલ્પ ૨", "વિકલ્પ ૩", "વિકલ્પ ૪"])
if st.button("સબમિટ કરો"):
    st.session_state.score += 10
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# લીડરબોર્ડ (મોટું બોક્સ અને ૧-૫ નંબર)
st.markdown("<div class='leader-box'>", unsafe_allow_html=True)
st.subheader("🏅 લીડરબોર્ડ (ટોપ ૫)")
top_scores = c.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 5").fetchall()
for i, row in enumerate(top_scores, 1):
    st.write(f"### {i}. 🌟 {row[0]} - {row[1]} પોઈન્ટ્સ")
st.markdown("</div>", unsafe_allow_html=True)
