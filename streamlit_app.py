import streamlit as st
import sqlite3

# ================= 🗄️ ડેટાબેઝ સિસ્ટમ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, score INTEGER)")
conn.commit()

# ================= 📚 સંપૂર્ણ NCERT ડેટાબેઝ (ધોરણ ૧ થી ૧૨) =================
ncert_master = {
    "ધોરણ 10": {
        "ગણિત": ["વાસ્તવિક સંખ્યાઓ", "બહુપદીઓ", "દ્વિચલ સુરેખ સમીકરણો", "દ્વિઘાત સમીકરણો", "સમાંતર શ્રેણી", "ત્રિકોણ", "યામ ભૂમિતિ", "ત્રિકોણમિતિનો પરિચય", "વર્તુળ", "આંકડાશાસ્ત્ર", "સંભાવના"],
        "વિજ્ઞાન": ["રાસાયણિક પ્રક્રિયાઓ", "એસિડ, બેઇઝ અને ક્ષાર", "ધાતુઓ અને અધાતુઓ", "કાર્બન અને તેના સંયોજનો", "જૈવિક ક્રિયાઓ", "પ્રકાશ-પરાવર્તન અને વક્રીભવન"],
        "સામાજિક વિજ્ઞાન": ["ભારતનો વારસો", "ભારતનો સાંસ્કૃતિક વારસો", "ભારતનો સાહિત્યિક વારસો", "ભારતનો વિજ્ઞાનનો વારસો", "ભારતના સાંસ્કૃતિક વારસાના સ્થળો"],
        "ગુજરાતી": ["મોરના ઈંડા", "રેસનો ઘોડો", "શીલવંત સાધુને", "ભૂખથીયે ભૂંડી ભીખ"],
        "અંગ્રેજી": ["Against the Odds", "The Human Robot", "An Interview with Arun Krishnamurthy"],
        "હિન્દી": ["पद", "डायरी का एक पन्ना", "तताँरा-वामीरो कथा"],
        "સંસ્કૃત": ["સમવદધ્વમ્", "કૂટનીતિ", "નાટ્યશાસ્ત્ર"]
    },
    "ધોરણ 9": {
        "ગણિત": ["સંખ્યા પદ્ધતિ", "બહુપદીઓ", "યામ ભૂમિતિ", "દ્વિચલ સુરેખ સમીકરણો", "યુક્લિડની ભૂમિતિનો પરિચય", "રેખાઓ અને ખૂણાઓ"],
        "વિજ્ઞાન": ["આપણી આસપાસમાં દ્રવ્ય", "શું આપણી આસપાસના દ્રવ્યો શુદ્ધ છે", "પરમાણુઓ અને અણુઓ", "સજીવનો પાયાનો એકમ"]
    }
    # અહીં તમે ધોરણ 1 થી 8 પણ આ જ રીતે વિસ્તૃત ઉમેરી શકો છો
}

# ================= 🎨 ડિઝાઈન (RGB + બોર્ડર) =================
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

name = st.text_input("✍️ તમારું નામ:", "")
std = st.selectbox("🎯 ધોરણ:", list(ncert_master.keys()))
sub = st.selectbox("📚 વિષય:", list(ncert_master[std].keys()))
ch = st.selectbox("📖 પ્રકરણ:", ncert_master[std][sub])
q_amt = st.selectbox("🔢 કેટલા વિકલ્પ રમવા છે?", [10, 20, 30, 50, 100])

if "score" not in st.session_state: st.session_state.score = 0
st.write(f"### 🏆 ચાલુ સ્કોર: {st.session_state.score}")

st.markdown("<div class='main-box'>", unsafe_allow_html=True)
st.write(f"### 📖 પ્રકરણ: {ch}")
st.write("### ❓ પ્રશ્ન: અહીં તમારો સવાલ આવશે...")
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
