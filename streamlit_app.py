import streamlit as st
import sqlite3

# ================= 🗄️ ડેટાબેઝ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, score INTEGER)")
conn.commit()

# ================= 🎨 ડિઝાઈન (RGB + કાળી બોર્ડર) =================
st.set_page_config(page_title="REVISION GAME", layout="centered")
st.markdown("""
<style>
.stApp { background: linear-gradient(124deg, #ff2400, #e81d1d, #e8b71d, #1de840, #1ddde8, #2b1de8, #dd00ff); background-size: 1600% 1600%; animation: bg 14s infinite; }
.main-box { background: rgba(0,0,0,0.8); padding: 20px; border-radius: 15px; border: 3px solid #000000; color: white; margin-bottom: 20px; }
.leader-box { border: 3px solid #000000; padding: 20px; border-radius: 15px; background: rgba(0,0,0,0.9); color: white; margin-top: 20px; }
div.stButton > button { background-color: #333333 !important; color: white !important; border: 2px solid #000000 !important; font-weight: bold !important; width: 100%; }
@keyframes bg { 0%{background-position:0% 82%} 50%{background-position:100% 19%} 100%{background-position:0% 82%} }
</style>
""", unsafe_allow_html=True)

# ================= 🕹️ ગેમ લોજિક =================
st.title("🎮 BEST GAME FOR REVISION")

# ઇનપુટ
name = st.text_input("✍️ તમારું નામ:", "આયુષ")
std = st.selectbox("🎯 ધોરણ:", ["ધોરણ 10"])
sub = st.selectbox("📚 વિષય:", ["સામાજિક વિજ્ઞાન", "વિજ્ઞાન", "ગણિત", "ગુજરાતી", "અંગ્રેજી"])
ch = st.selectbox("📖 પ્રકરણ:", ["પ્રકરણ ૧", "પ્રકરણ ૨", "પ્રકરણ ૩", "પ્રકરણ ૪", "પ્રકરણ ૫"])
q_amt = st.selectbox("🔢 કેટલા વિકલ્પ (MCQ) રમવા છે?", [10, 20, 30, 50, 100])

if "score" not in st.session_state: st.session_state.score = 0
st.write(f"### 🏆 ચાલુ સ્કોર: {st.session_state.score}")

# પ્રશ્ન અને વિકલ્પ એરિયા
st.markdown("<div class='main-box'>", unsafe_allow_html=True)
st.write(f"### 📖 પ્રકરણ: {ch}")
st.write("### ❓ પ્રશ્ન: પ્રકાશના પરાવર્તનના નિયમો જણાવો?")
ans = st.radio("તમારો જવાબ પસંદ કરો:", ["આપાતકોણ = પરાવર્તન કોણ", "આપાતકોણ > પરાવર્તન કોણ", "આપાતકોણ < પરાવર્તન કોણ", "કોઈ નહીં"])
if st.button("સબમિટ કરો"):
    st.session_state.score += 10
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# લીડરબોર્ડ (મોટા બોક્સની અંદર)
st.markdown("<div class='leader-box'>", unsafe_allow_html=True)
st.subheader("🏅 લીડરબોર્ડ")
top_scores = c.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 5").fetchall()
for i, row in enumerate(top_scores, 1):
    st.write(f"### {i}. 🌟 {row[0]} - {row[1]} પોઈન્ટ્સ")
st.markdown("</div>", unsafe_allow_html=True)
