import streamlit as st
import sqlite3

# ================= 🗄️ ડેટાબેઝ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)")
conn.commit()

# ================= 🎨 ડિઝાઈન અને CSS =================
st.set_page_config(page_title="BEST GAME", layout="centered")
st.markdown("""
<style>
.main-box { background: rgba(0,0,0,0.7); padding: 20px; border-radius: 15px; border: 3px solid #000000; color: white; margin-bottom: 20px; }
.score-box { border: 3px solid #000000; padding: 10px; border-radius: 10px; text-align: center; background: rgba(0,255,153,0.2); font-size: 24px; font-weight: bold; margin-bottom: 15px; }
div.stButton > button { background-color: #333333 !important; color: white !important; border: 2px solid #000000 !important; font-weight: bold !important; width: 100%; }
</style>
""", unsafe_allow_html=True)

# ================= 📚 માસ્ટર ડેટાબેઝ ૧ થી ૧૨ =================
master_db = {
    f"ધોરણ {i}": ["ગણિત", "વિજ્ઞાન", "સામાજિક વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી", "હિન્દી", "સંસ્કૃત", "પર્યાવરણ", "કમ્પ્યુટર"] 
    for i in range(1, 13)
}

# ================= 🕹️ ગેમ લોજિક =================
st.title("🎮 BEST GAME FOR REVISION")

# ઇનપુટ
name = st.text_input("✍️ તમારું નામ:", "આયુષ")
std = st.selectbox("🎯 ધોરણ:", list(master_db.keys()))
sub = st.selectbox("📚 વિષય:", master_db[std])
ch = st.selectbox("📖 પ્રકરણ:", [f"પ્રકરણ {i}" for i in range(1, 21)])

if "score" not in st.session_state: st.session_state.score = 0

# સ્કોર
st.markdown(f"<div class='score-box'>🏆 ચાલુ સ્કોર: {st.session_state.score}</div>", unsafe_allow_html=True)

# પ્રશ્ન એરિયા
st.markdown("<div class='main-box'>", unsafe_allow_html=True)
st.write(f"### 📖 પ્રકરણ: {ch}")
st.write(f"### ❓ પ્રશ્ન: {sub} માંથી તમારા માટે ખાસ સવાલ...")
ans = st.radio("તમારો જવાબ પસંદ કરો:", ["વિકલ્પ ૧", "વિકલ્પ ૨", "વિકલ્પ ૩", "વિકલ્પ ૪"])
if st.button("સબમિટ કરો"):
    st.session_state.score += 10
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# લીડરબોર્ડ (બોર્ડર વગર)
st.subheader("🏅 લીડરબોર્ડ")
for row in c.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 5").fetchall():
    st.write(f"🌟 {row[0]} - {row[1]} પોઈન્ટ્સ")
