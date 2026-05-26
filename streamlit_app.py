import streamlit as st
import random
import sqlite3
import time

# ================= 🗄️ ડેટાબેઝ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER, standard TEXT, subject TEXT, chapter TEXT)")
conn.commit()

# ================= 🔊 ઑડિયો અને 🌈 એનિમેશન CSS =================
st.set_page_config(page_title="BEST GAME FOR REVISION AND TEST", layout="centered")
st.markdown("""
<style>
.stApp { background: linear-gradient(124deg, #ff2400, #e81d1d, #e8b71d, #1de840, #1ddde8, #2b1de8, #dd00ff); background-size: 1600% 1600%; animation: bg 14s infinite; color: white; }
.game-container { background: rgba(0,0,0,0.85); padding: 25px; border-radius: 20px; border: 2px solid #00ffff; }
/* એનિમેશન ક્લાસ */
.correct-box { animation: pulse 0.5s infinite; border: 3px solid #00ff66; padding: 15px; border-radius: 10px; text-align: center; background: rgba(0,255,100,0.2); }
.wrong-box { animation: shake 0.3s infinite; border: 3px solid #ff3333; padding: 15px; border-radius: 10px; text-align: center; background: rgba(255,50,50,0.2); }
@keyframes pulse { 0% {transform: scale(1);} 50% {transform: scale(1.05);} 100% {transform: scale(1);} }
@keyframes shake { 0%, 100% {transform: translateX(0);} 25% {transform: translateX(-5px);} 75% {transform: translateX(5px);} }
@keyframes bg { 0%{background-position:0% 82%} 50%{background-position:100% 19%} 100%{background-position:0% 82%} }
</style>
""", unsafe_allow_html=True)

def play_sound(t):
    st.markdown(f"""<script>var ctx=new AudioContext(); var osc=ctx.createOscillator(); osc.type='{'sine' if t=='c' else 'sawtooth'}'; osc.frequency.setValueAtTime({587 if t=='c' else 150}, ctx.currentTime); osc.connect(ctx.destination); osc.start(); osc.stop(ctx.currentTime+0.3);</script>""", unsafe_allow_html=True)

# ================= 📚 માસ્ટર ડેટાબેઝ =================
ncert_db = {f"ધોરણ {i}": ["ગણિત", "વિજ્ઞાન", "સામાજિક વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી"] for i in range(1, 13)}

# ================= 🕹️ ગેમ લોજિક =================
st.title("🎮 BEST GAME FOR REVISION AND TEST")
st.markdown("<div class='game-container'>", unsafe_allow_html=True)

name = st.text_input("તમારું નામ:", "આયુષ")
std = st.selectbox("ધોરણ:", list(ncert_db.keys()))
sub = st.selectbox("વિષય:", ncert_db[std])
ch = st.selectbox("પ્રકરણ:", [f"પ્રકરણ {i}" for i in range(1, 16)])

if "score" not in st.session_state: st.session_state.score = 0

# ઉદાહરણ પ્રશ્ન (તમે તમારો પ્રશ્ન ડેટા અહીં ઉમેરી શકો)
if st.button("સબમિટ કરો"):
    # સાચો જવાબ ચેક કરો
    is_correct = random.choice([True, False]) # અત્યારે ટેસ્ટ માટે રેન્ડમ
    if is_correct:
        st.markdown("<div class='correct-box'>સાચો જવાબ! 🎉</div>", unsafe_allow_html=True)
        play_sound('c')
        st.session_state.score += 10
    else:
        st.markdown("<div class='wrong-box'>ખોટો જવાબ! ❌</div>", unsafe_allow_html=True)
        play_sound('w')
        st.session_state.score -= 5
    st.rerun()

st.write(f"### 🏆 સ્કોર: {st.session_state.score}")
st.markdown("</div>", unsafe_allow_html=True)

# ================= 🏅 લીડરબોર્ડ =================
st.subheader("🏅 લીડરબોર્ડ")
for row in c.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 5").fetchall():
    st.write(f"🌟 {row[0]} - {row[1]} પોઈન્ટ્સ")
