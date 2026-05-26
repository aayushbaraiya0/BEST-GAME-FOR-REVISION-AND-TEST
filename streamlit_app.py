import streamlit as st
import sqlite3

# ================= 🗄️ ડેટાબેઝ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, score INTEGER)")
conn.commit()

# ================= 📚 સંપૂર્ણ ૧ થી ૧૨ ધોરણનો ડેટાબેઝ =================
# દરેક ધોરણ, તેના વિષયો અને પ્રકરણો
ncert_master = {
    f"ધોરણ {std}": {
        "ગણિત": [f"પ્રકરણ {i}" for i in range(1, 15)],
        "વિજ્ઞાન": [f"પ્રકરણ {i}" for i in range(1, 15)],
        "સામાજિક વિજ્ઞાન": [f"પ્રકરણ {i}" for i in range(1, 20)],
        "ગુજરાતી": [f"પ્રકરણ {i}" for i in range(1, 15)],
        "અંગ્રેજી": [f"પ્રકરણ {i}" for i in range(1, 15)]
    } for std in range(1, 13)
}

# ધોરણ ૧૦ માટે ખાસ નામ સાથેના પ્રકરણો (તમે અહીં બાકીના ધોરણોના નામ પણ ઉમેરી શકો)
ncert_master["ધોરણ 10"]["ગણિત"] = ["વાસ્તવિક સંખ્યાઓ", "બહુપદીઓ", "દ્વિચલ સુરેખ સમીકરણો", "દ્વિઘાત સમીકરણો", "સમાંતર શ્રેણી", "ત્રિકોણ", "યામ ભૂમિતિ", "ત્રિકોણમિતિનો પરિચય", "ત્રિકોણમિતિના ઉપયોગો", "વર્તુળ"]

# ================= 🎨 ડિઝાઈન (RGB + કાળી બોર્ડર) =================
st.set_page_config(page_title="BEST GAME FOR REVISION", layout="centered")
st.markdown("""
<style>
.stApp { background: linear-gradient(124deg, #ff2400, #e81d1d, #e8b71d, #1de840, #1ddde8, #2b1de8, #dd00ff); background-size: 1600% 1600%; animation: bg 14s infinite; }
.main-box { background: rgba(0,0,0,0.85); padding: 25px; border-radius: 15px; border: 3px solid #000000; color: white; margin-bottom: 20px; }
.leader-box { border: 3px solid #000000; padding: 20px; border-radius: 15px; background: rgba(0,0,0,0.9); color: white; margin-top: 20px; }
div.stButton > button { background-color: #333333 !important; color: white !important; border: 2px solid #000000 !important; font-weight: bold !important; width: 100%; }
@keyframes bg { 0%{background-position:0% 82%} 50%{background-position:100% 19%} 100%{background-position:0% 82%} }
</style>
""", unsafe_allow_html=True)

# ================= 🕹️ ગેમ લોજિક =================
st.title("🎮 BEST GAME FOR REVISION")

name = st.text_input("✍️ તમારું નામ:", "આયુષ")
std = st.selectbox("🎯 ધોરણ:", list(ncert_master.keys()))
sub = st.selectbox("📚 વિષય:", list(ncert_master[std].keys()))
ch = st.selectbox("📖 પ્રકરણ:", ncert_master[std][sub])
q_amt = st.selectbox("🔢 કેટલા વિકલ્પ રમવા છે?", [10, 20, 30, 50, 100])

if "score" not in st.session_state: st.session_state.score = 0
st.write(f"### 🏆 ચાલુ સ્કોર: {st.session_state.score}")

st.markdown("<div class='main-box'>", unsafe_allow_html=True)
st.write(f"### 📖 પ્રકરણ: {ch}")
st.write(f"### ❓ પ્રશ્ન: {ch} માંથી એક સવાલ આવશે...")
ans = st.radio("તમારો જવાબ પસંદ કરો:", ["વિકલ્પ ૧", "વિકલ્પ ૨", "વિકલ્પ ૩", "વિકલ્પ ૪"])
if st.button("સબમિટ કરો"):
    st.session_state.score += 10
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='leader-box'>", unsafe_allow_html=True)
st.subheader("🏅 લીડરબોર્ડ")
for i, row in enumerate(c.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 5").fetchall(), 1):
    st.write(f"### {i}. 🌟 {row[0]} - {row[1]} પોઈન્ટ્સ")
st.markdown("</div>", unsafe_allow_html=True)
