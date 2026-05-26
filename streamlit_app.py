import streamlit as st
import random
import sqlite3
import time

# ================= 🗄️ ડેટાબેઝ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER, standard TEXT, subject TEXT, chapter TEXT)")
conn.commit()

# ================= 🌈 ડિઝાઈન (ડાર્ક બટન સાથે) =================
st.set_page_config(page_title="BEST GAME FOR REVISION AND TEST", layout="centered")
st.markdown("""
<style>
.stApp { background: linear-gradient(124deg, #ff2400, #e81d1d, #e8b71d, #1de840, #1ddde8, #2b1de8, #dd00ff); background-size: 1600% 1600%; animation: bg 14s infinite; color: white; }
.box { background: rgba(0,0,0,0.7); padding: 20px; border-radius: 15px; border: 3px solid #000000; margin-bottom: 15px; color: white; }
.score-box { border: 3px solid #000000; padding: 10px; border-radius: 10px; text-align: center; background: rgba(0,255,153,0.2); font-size: 24px; font-weight: bold; margin-bottom: 10px; }
.leader-box { border: 3px solid #000000; padding: 15px; border-radius: 10px; background: rgba(255,170,0,0.1); }

/* ડાર્ક બટન કોડ (Hover પર પણ રંગ નહીં બદલાય) */
div.stButton > button {
    background-color: #333333 !important; 
    color: white !important;
    border: 2px solid #000000 !important;
    font-weight: bold !important;
}
div.stButton > button:hover {
    background-color: #333333 !important; 
    color: white !important;
    border: 2px solid #000000 !important;
}

@keyframes bg { 0%{background-position:0% 82%} 50%{background-position:100% 19%} 100%{background-position:0% 82%} }
</style>
""", unsafe_allow_html=True)

# ================= 🕹️ ગેમ લોજિક =================
st.title("🎮 BEST GAME FOR REVISION AND TEST")

st.markdown("<div class='box'>", unsafe_allow_html=True)
name = st.text_input("✍️ તમારું નામ:", "આયુષ")
std = st.selectbox("🎯 ધોરણ:", [f"ધોરણ {i}" for i in range(1, 13)])
sub = st.selectbox("📚 વિષય:", ["ગણિત", "વિજ્ઞાન", "સામાજિક વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી"])
ch = st.selectbox("📖 પ્રકરણ:", [f"પ્રકરણ {i}" for i in range(1, 16)])
st.markdown("</div>", unsafe_allow_html=True)

if "score" not in st.session_state: st.session_state.score = 0

st.markdown(f"<div class='score-box'>🏆 ચાલુ સ્કોર: {st.session_state.score}</div>", unsafe_allow_html=True)

st.markdown("<div class='box'>", unsafe_allow_html=True)
st.write(f"### ❓ પ્રશ્ન: {ch} ({sub}) માંથી સવાલ...")
ans = st.radio("તમારો જવાબ પસંદ કરો:", ["વિકલ્પ ૧", "વિકલ્પ ૨", "વિકલ્પ ૩", "વિકલ્પ ૪"])

if st.button("સબમિટ કરો"):
    st.session_state.score += 10
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='leader-box'>", unsafe_allow_html=True)
st.subheader("🏅 લીડરબોર્ડ")
for row in c.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 5").fetchall():
    st.write(f"🌟 {row[0]} - {row[1]} પોઈન્ટ્સ")
st.markdown("</div>", unsafe_allow_html=True)
