import streamlit as st
import random
import sqlite3
import time
import base64

# ================= 🎮 પેજ સેટઅપ =================
st.set_page_config(page_title="BEST GAME FOR REVISION AND TEST", page_icon="🎮", layout="centered")

# ================= 🗄️ ડેટાબેઝ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER, standard TEXT, subject TEXT, chapter TEXT)")
conn.commit()

# ================= 🔊 ઑડિયો સિસ્ટમ =================
def play_sound(sound_type):
    js = f"""<script>
    var ctx = new (window.AudioContext || window.webkitAudioContext)();
    var osc = ctx.createOscillator();
    osc.type = '{'sine' if sound_type=='correct' else 'sawtooth'}';
    osc.frequency.setValueAtTime({587 if sound_type=='correct' else 150}, ctx.currentTime);
    osc.connect(ctx.destination); osc.start(); osc.stop(ctx.currentTime + 0.3);
    </script>"""
    st.markdown(js, unsafe_allow_html=True)

# ================= 🌈 ડિઝાઈન (CSS) =================
st.markdown("""<style>.game-container { background: rgba(0,0,0,0.8); padding: 25px; border-radius: 20px; border: 2px solid #00ffff; color: white; }</style>""", unsafe_allow_html=True)

# ================= 📚 માસ્ટર ડેટાબેઝ =================
ncert_db = {
    "ધોરણ ૧-૫": ["ગણિત ગમ્મત", "પર્યાવરણ", "ગુજરાતી", "અંગ્રેજી"],
    "ધોરણ ૬-૮": ["વિજ્ઞાન", "ગણિત", "સામાજિક વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી", "હિન્દી"],
    "ધોરણ ૯-૧૦": ["સામાજિક વિજ્ઞાન", "વિજ્ઞાન", "ગણિત", "ગુજરાતી", "અંગ્રેજી", "હિન્દી", "સંસ્કૃત", "કમ્પ્યુટર"],
    "ધોરણ ૧૧-૧૨": ["ગણિત", "ભૌતિક વિજ્ઞાન", "રસાયણ વિજ્ઞાન", "જીવ વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી"]
}

# ================= 🤖 પ્રશ્ન એન્જિન =================
def get_q(ch, sub, idx):
    # સાચો ફિક્સ: ડિક્શનરીનું માળખું જે એરર ન આપે
    pool = [
        {"પ્રશ્ન": f"{ch} ({sub}) માંથી: તાજમહાલ કોણે બંધાવ્યો?", "વિકલ્પો": ["અકબર", "શાહજહાં", "બાબર", "હુમાયુ"], "સાચો": "શાહજહાં"},
        {"પ્રશ્ન": f"{ch} ({sub}) માંથી: પાણીનું રાસાયણિક સૂત્ર?", "વિકલ્પો": ["H2O", "CO2", "NaCl", "O2"], "સાચો": "H2O"},
        {"પ્રશ્ન": f"{ch} ({sub}) માંથી: ૨+૨ કેટલા થાય?", "વિકલ્પો": ["૩", "૪", "૫", "૬"], "સાચો": "૪"}
    ]
    return pool[idx % len(pool)]

# ================= 🕹️ ગેમ લોજિક =================
st.title("🎮 રિવિઝન ટેસ્ટ")
st.markdown("<div class='game-container'>", unsafe_allow_html=True)

name = st.text_input("તમારું નામ:", "આયુષ")
std = st.selectbox("ધોરણ પસંદ કરો:", list(ncert_db.keys()))
sub = st.selectbox("વિષય પસંદ કરો:", ncert_db[std])
ch = st.selectbox("પ્રકરણ પસંદ કરો:", [f"પ્રકરણ {i}" for i in range(1, 16)])
quiz_limit = st.selectbox("કેટલા MCQ રમવા છે?", [10, 20, 30])

if "score" not in st.session_state: st.session_state.score = 0
if "q_num" not in st.session_state: st.session_state.q_num = 1

q = get_q(ch, sub, st.session_state.q_num)
st.write(f"### પ્રશ્ન {st.session_state.q_num}: {q['પ્રશ્ન']}")
ans = st.radio("વિકલ્પો:", q["વિકલ્પો"], key=f"r_{st.session_state.q_num}")

if st.button("સબમિટ કરો"):
    if ans == q["સાચો"]:
        st.success("સાચો જવાબ! 🎉")
        play_sound("correct")
        st.session_state.score += 10
    else:
        st.error(f"ખોટો! સાચો જવાબ: {q['સાચો']}")
        play_sound("wrong")
        st.session_state.score -= 5
    st.session_state.q_num += 1
    time.sleep(1)
    st.rerun()

st.write(f"### 🏆 સ્કોર: {st.session_state.score}")
st.markdown("</div>", unsafe_allow_html=True)
