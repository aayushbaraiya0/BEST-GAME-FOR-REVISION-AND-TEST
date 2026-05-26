import streamlit as st
import random
import sqlite3
import time

# ================= 🗄️ ડેટાબેઝ સિસ્ટમ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, score INTEGER, standard TEXT, subject TEXT, chapter TEXT)")
conn.commit()

# ================= 🔊 ૧૦૦% સુપર લાઉડ ઓડિયો એન્જિન =================
def play_sound(sound_type):
    js_code = f"""
    <script>
    (function() {{
        var ctx = new (window.AudioContext || window.webkitAudioContext)();
        if (ctx.state === 'suspended') {{ ctx.resume(); }}
        var osc = ctx.createOscillator();
        var gain = ctx.createGain();
        osc.type = '{"sine" if sound_type=="correct" else "sawtooth" if sound_type=="wrong" else "triangle"}';
        osc.frequency.setValueAtTime({587 if sound_type=="correct" else 130 if sound_type=="wrong" else 440}, ctx.currentTime);
        gain.gain.setValueAtTime(0.2, ctx.currentTime);
        osc.connect(gain); gain.connect(ctx.destination);
        osc.start(); osc.stop(ctx.currentTime + 0.3);
    }})();
    </script>
    """
    st.markdown(js_code, unsafe_allow_html=True)

# ================= 🌈 ડિઝાઈન (CSS) =================
st.set_page_config(page_title="BEST GAME FOR REVISION AND TEST", layout="centered")
st.markdown("""
<style>
.stApp { background: linear-gradient(124deg, #ff2400, #e81d1d, #e8b71d, #1de840, #1ddde8, #2b1de8, #dd00ff); background-size: 1600% 1600%; animation: bg 14s infinite; color: white; }
.game-container { background: rgba(0,0,0,0.85); padding: 25px; border-radius: 20px; border: 2px solid #00ffff; }
.correct-box { border: 3px solid #00ff66; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; background: rgba(0,255,100,0.2); }
.wrong-box { border: 3px solid #ff3333; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; background: rgba(255,50,50,0.2); }
@keyframes bg { 0%{background-position:0% 82%} 50%{background-position:100% 19%} 100%{background-position:0% 82%} }
</style>
""", unsafe_allow_html=True)

# ================= 📚 ૧-૧૨ ધોરણનો માસ્ટર ડેટાબેઝ =================
ncert_master = {
    f"ધોરણ {i}": ["ગણિત", "વિજ્ઞાન", "સામાજિક વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી"] for i in range(1, 13)
}

# ================= 🤖 પ્રશ્ન એન્જિન =================
def get_dynamic_question(ch, sub):
    questions = {
        "વિજ્ઞાન": [
            {"પ્રશ્ન": f"{ch} ({sub}) માંથી: એસિડ સ્વાદે કેવા હોય છે?", "વિકલ્પો": ["ખાટા", "તૂરા", "કડવા", "મીઠા"], "સાચો": "ખાટા"},
            {"પ્રશ્ન": f"{ch} ({sub}) માંથી: પાણીનું રાસાયણિક સૂત્ર?", "વિકલ્પો": ["H2O", "CO2", "NaCl", "O2"], "સાચો": "H2O"}
        ],
        "સામાજિક વિજ્ઞાન": [
            {"પ્રશ્ન": f"{ch} ({sub}) માંથી: તાજમહાલ કોણે બંધાવ્યો?", "વિકલ્પો": ["અકબર", "શાહજહાં", "બાબર", "હુમાયુ"], "સાચો": "શાહજહાં"},
            {"પ્રશ્ન": f"{ch} ({sub}) માંથી: લોથલ કયા જિલ્લામાં છે?", "વિકલ્પો": ["અમદાવાદ", "રાજકોટ", "ભાવનગર", "સુરત"], "સાચો": "અમદાવાદ"}
        ],
        "ગણિત": [
            {"પ્રશ્ન": f"{ch} ({sub}) માંથી: વર્તુળનો પરિઘ શું છે?", "વિકલ્પો": ["2πr", "πr²", "2r", "πd"], "સાચો": "2πr"}
        ]
    }
    # જો વિષય ન મળે તો ડિફોલ્ટ
    return random.choice(questions.get(sub, [{"પ્રશ્ન": f"{ch} માંથી સવાલ:", "વિકલ્પો": ["A", "B", "C", "D"], "સાચો": "A"}]))

# ================= 🕹️ ગેમ લોજિક =================
st.title("🎮 BEST GAME FOR REVISION AND TEST")
st.markdown("<div class='game-container'>", unsafe_allow_html=True)

name = st.text_input("તમારું નામ:", "આયુષ")
std = st.selectbox("ધોરણ પસંદ કરો:", list(ncert_master.keys()))
sub = st.selectbox("વિષય પસંદ કરો:", ncert_master[std])
ch = st.selectbox("પ્રકરણ પસંદ કરો:", [f"પ્રકરણ {i}" for i in range(1, 16)])

if "score" not in st.session_state: st.session_state.score = 0
if "q_num" not in st.session_state: st.session_state.q_num = 1

q = get_dynamic_question(ch, sub)
st.write(f"### પ્રશ્ન {st.session_state.q_num}: {q['પ્રશ્ન']}")
ans = st.radio("વિકલ્પો:", q["વિકલ્પો"], key=f"r_{st.session_state.q_num}")

if st.button("સબમિટ કરો"):
    play_sound("click")
    if ans == q["સાચો"]:
        st.markdown("<div class='correct-box'>સાચો જવાબ! 🎉 (+૧૦)</div>", unsafe_allow_html=True)
        play_sound("correct")
        st.session_state.score += 10
    else:
        st.markdown("<div class='wrong-box'>ખોટો! સાચો જવાબ: "+q['સાચો']+"</div>", unsafe_allow_html=True)
        play_sound("wrong")
        st.session_state.score -= 5
    st.session_state.q_num += 1
    time.sleep(1)
    st.rerun()

st.write(f"### 🏆 સ્કોર: {st.session_state.score}")
st.markdown("</div>", unsafe_allow_html=True)

# ================= 🏅 લીડરબોર્ડ =================
st.subheader("🏅 લીડરબોર્ડ")
for row in c.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 5").fetchall():
    st.write(f"🌟 {row[0]} - {row[1]} પોઈન્ટ્સ")
