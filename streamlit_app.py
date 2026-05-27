import streamlit as st
import sqlite3

# ================= 🗄️ ડેટાબેઝ સિસ્ટમ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, score INTEGER)")
conn.commit()

# ================= 📚 સંપૂર્ણ ૧ થી ૧૨ ધોરણનો NCERT ડેટા =================
ncert_master = {
    f"ધોરણ {std}": {
        "ગણિત": [f"પ્રકરણ {i}" for i in range(1, 16)],
        "વિજ્ઞાન": [f"પ્રકરણ {i}" for i in range(1, 16)],
        "સામાજિક વિજ્ઞાન": [f"પ્રકરણ {i}" for i in range(1, 22)],
        "ગુજરાતી": [f"પ્રકરણ {i}" for i in range(1, 16)],
        "અંગ્રેજી": [f"પ્રકરણ {i}" for i in range(1, 16)]
    } for std in range(1, 13)
}
# ધોરણ ૧૦ ના વિજ્ઞાનના સાચા નામ
ncert_master["ધોરણ 10"]["વિજ્ઞાન"] = ["રાસાયણિક પ્રક્રિયાઓ", "એસિડ, બેઇઝ અને ક્ષાર", "ધાતુઓ અને અધાતુઓ", "કાર્બન અને તેના સંયોજનો", "જૈવિક ક્રિયાઓ", "નિયંત્રણ અને સંકલન"]

# ================= 🎨 RGB + કાળી બોર્ડર ડિઝાઈન (CSS) =================
st.set_page_config(page_title="BEST GAME FOR REVISION", layout="centered")
st.markdown("""
<style>
.stApp { background: linear-gradient(124deg, #ff2400, #e81d1d, #e8b71d, #1de840, #1ddde8, #2b1de8, #dd00ff); background-size: 1600% 1600%; animation: bg 14s infinite; }
.setup-box { background: rgba(0,0,0,0.8); padding: 20px; border-radius: 15px; border: 3px solid #000000; color: white; margin-bottom: 10px; }
.quiz-box { background: rgba(255,255,255,0.1); padding: 25px; border-radius: 15px; border: 4px solid #000000; color: white; margin-top: 20px; }
.leader-box { border: 3px solid #000000; padding: 20px; border-radius: 15px; background: rgba(0,0,0,0.9); color: white; margin-top: 30px; }
.score-text { font-size: 30px; font-weight: bold; text-align: center; color: #00ff99; text-shadow: 2px 2px #000; }

/* ડાર્ક બટન */
div.stButton > button { background-color: #222222 !important; color: white !important; border: 3px solid #000000 !important; font-weight: bold !important; width: 100%; height: 50px; font-size: 20px; }
@keyframes bg { 0%{background-position:0% 82%} 50%{background-position:100% 19%} 100%{background-position:0% 82%} }
</style>
""", unsafe_allow_html=True)

# ================= 🕹️ ગેમ લોજિક અને સેશન સ્ટેટ =================
if "game_started" not in st.session_state: st.session_state.game_started = False
if "score" not in st.session_state: st.session_state.score = 0

st.title("🎮 BEST GAME FOR REVISION")

# ૧. સેટઅપ બોક્સ (નામ, ધોરણ, વિષય વગેરે)
st.markdown("<div class='setup-box'>", unsafe_allow_html=True)
name = st.text_input("✍️ તમારું નામ લખો:", "આયુષ")
std = st.selectbox("🎯 ધોરણ પસંદ કરો:", list(ncert_master.keys()), index=9) # Default ધોરણ 10
sub = st.selectbox("📚 વિષય પસંદ કરો:", list(ncert_master[std].keys()))
ch = st.selectbox("📖 પ્રકરણ પસંદ કરો:", ncert_master[std][sub])
q_amt = st.selectbox("🔢 કેટલા પ્રશ્નો (MCQ) રમવા છે?", [10, 20, 30, 50, 100])

st.markdown(f"<div class='score-text'>🏆 ચાલુ સ્કોર: {st.session_state.score}</div>", unsafe_allow_html=True)

# 'સ્ટાર્ટ ગેમ' બટન
if st.button("🚀 સ્ટાર્ટ ગેમ"):
    st.session_state.game_started = True

st.markdown("</div>", unsafe_allow_html=True)

# ૨. સવાલ પૂછવાનું મેનુ (જ્યારે ગેમ સ્ટાર્ટ થાય ત્યારે જ દેખાશે)
if st.session_state.game_started:
    st.markdown("<div class='quiz-box'>", unsafe_allow_html=True)
    st.write(f"### ❓ પ્રશ્ન: {ch} ({sub}) માંથી...")
    st.write("નીચેનામાંથી સાચો વિકલ્પ પસંદ કરો:")
    
    ans = st.radio("વિકલ્પો:", ["વિકલ્પ A", "વિકલ્પ B", "વિકલ્પ C", "વિકલ્પ D"], index=None)
    
    if st.button("✅ જવાબ સબમિટ કરો"):
        if ans:
            st.session_state.score += 10
            # સ્કોર ડેટાબેઝમાં સેવ કરવો (જો જરૂર હોય)
            c.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, st.session_state.score))
            conn.commit()
            st.success("ખૂબ સરસ! આગળનો પ્રશ્ન તૈયાર થઈ રહ્યો છે...")
            time_wait = 1
            st.rerun()
        else:
            st.warning("કૃપા કરીને એક વિકલ્પ પસંદ કરો!")
    st.markdown("</div>", unsafe_allow_html=True)

# ૩. લીડરબોર્ડ બોક્સ (૧ થી ૫ નંબર સાથે)
st.markdown("<div class='leader-box'>", unsafe_allow_html=True)
st.subheader("🏅 લીડરબોર્ડ (Top 5)")
top_scores = c.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 5").fetchall()

if top_scores:
    for i, row in enumerate(top_scores, 1):
        st.write(f"### {i}. 🌟 {row[0]} — {row[1]} પોઈન્ટ્સ")
else:
    st.write("હજી સુધી કોઈ સ્કોર નોંધાયો નથી. પ્રથમ બનો!")
st.markdown("</div>", unsafe_allow_html=True)
