import streamlit as st
import random
import sqlite3
import time

# ================= 🗄️ ડેટાબેઝ સિસ્ટમ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER, standard TEXT, subject TEXT, chapter TEXT)")
conn.commit()

# ================= 🌈 ડિઝાઈન (RGB એનિમેશન) =================
st.set_page_config(page_title="રિવિઝન ક્વિઝ", layout="centered")
st.markdown("""
<style>
.stApp { background: linear-gradient(124deg, #ff2400, #e81d1d, #e8b71d, #1de840, #1ddde8, #2b1de8, #dd00ff); background-size: 1600% 1600%; animation: bg 14s infinite; color: white; }
.game-container { background: rgba(0,0,0,0.85); padding: 25px; border-radius: 20px; border: 2px solid #00ffff; }
@keyframes bg { 0%{background-position:0% 82%} 50%{background-position:100% 19%} 100%{background-position:0% 82%} }
</style>
""", unsafe_allow_html=True)

# ================= 📚 માસ્ટર ડેટાબેઝ =================
ncert_master = {
    f"ધોરણ {i}": ["ગણિત", "વિજ્ઞાન", "સામાજિક વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી"] for i in range(1, 13)
}

# ================= 🕹️ ગેમ લોજિક =================
st.markdown("<div class='game-container'>", unsafe_allow_html=True)
st.title("🎮 રિવિઝન ટેસ્ટ")

name = st.text_input("તમારું નામ:", "આયુષ")
std = st.selectbox("ધોરણ પસંદ કરો:", list(ncert_master.keys()))
sub = st.selectbox("વિષય પસંદ કરો:", ncert_master[std])
ch = st.selectbox("પ્રકરણ પસંદ કરો:", [f"પ્રકરણ {i}" for i in range(1, 16)])

if "score" not in st.session_state: st.session_state.score = 0

if st.button("સબમિટ"):
    # અહીં પ્રશ્ન લોજિક (તમારું જૂનું ફંક્શન)
    st.success("સાચો જવાબ! 🎉")
    st.session_state.score += 10
    
st.write(f"### 🏆 સ્કોર: {st.session_state.score}")
st.markdown("</div>", unsafe_allow_html=True)

# ================= 🏅 લીડરબોર્ડ =================
st.subheader("🏅 લીડરબોર્ડ")
scores = c.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 5").fetchall()
for s in scores:
    st.write(f"🌟 {s[0]} - {s[1]} પોઈન્ટ્સ")
