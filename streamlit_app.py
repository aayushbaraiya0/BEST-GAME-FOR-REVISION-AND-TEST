import streamlit as st
import random
import sqlite3
import os
import base64
import time

# ================= 🎮 પેજ સેટઅપ =================
st.set_page_config(
    page_title="રિવિઝન અને ટેસ્ટ માટેની શ્રેષ્ઠ રમત",
    page_icon="🎮",
    layout="centered"
)

# ================= 🗄️ ડેટાબેઝ સિસ્ટમ =================
conn = sqlite3.connect("leaderboard.db", check_same_thread=False)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    score INTEGER,
    standard TEXT,
    subject TEXT
)
""")
conn.commit()

# ================= 🔊 ૧૦૦% સુપર લાઉડ ઓડિયો એન્જિન =================
def play_sound(sound_type):
    if sound_type == "correct":
        js_code = """
        <script>
        (function() {
            var ctx = new (window.AudioContext || window.webkitAudioContext)();
            if (ctx.state === 'suspended') { ctx.resume(); }
            var osc = ctx.createOscillator();
            var gain = ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(587.33, ctx.currentTime);
            gain.gain.setValueAtTime(0.2, ctx.currentTime);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + 0.3);
        })();
        </script>
        """
        st.markdown(js_code, unsafe_allow_html=True)
    elif sound_type == "wrong":
        js_code = """
        <script>
        (function() {
            var ctx = new (window.AudioContext || window.webkitAudioContext)();
            if (ctx.state === 'suspended') { ctx.resume(); }
            var osc = ctx.createOscillator();
            var gain = ctx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(130.81, ctx.currentTime);
            gain.gain.setValueAtTime(0.2, ctx.currentTime);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + 0.4);
        })();
        </script>
        """
        st.markdown(js_code, unsafe_allow_html=True)
    elif sound_type == "click":
        js_code = """
        <script>
        (function() {
            var ctx = new (window.AudioContext || window.webkitAudioContext)();
            if (ctx.state === 'suspended') { ctx.resume(); }
            var osc = ctx.createOscillator();
            var gain = ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(440, ctx.currentTime);
            gain.gain.setValueAtTime(0.1, ctx.currentTime);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + 0.06);
        })();
        </script>
        """
        st.markdown(js_code, unsafe_allow_html=True)

# ================= 🌈 એડવાન્સ એનિમેશન અને ડિઝાઇન (CSS) =================
st.markdown("""
<style>
/* 🌈 પૃષ્ઠભૂમિ RGB એનિમેશન */
.stApp {
    background: linear-gradient(124deg, #ff2400, #e81d1d, #e8b71d, #1de840, #1ddde8, #2b1de8, #dd00ff, #dd00ff);
    background-size: 1600% 1600%;
    animation: RGB-Animation 14s ease infinite;
    color: white;
}
@keyframes RGB-Animation {
    0%{background-position:0% 82%}
    50%{background-position:100% 19%}
    100%{background-position:0% 82%}
}

.main-title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: #00ffff;
    text-shadow: 0px 0px 15px cyan;
    margin-bottom: 20px;
}

.game-container {
    background: rgba(10, 10, 15, 0.94) !important;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #00ffff;
    box-shadow: 0px 4px 25px rgba(0, 0, 0, 0.7);
    margin-bottom: 15px;
}

.question {
    font-size: 24px;
    font-weight: bold;
    color: white;
    margin-top: 10px;
}

.score {
    font-size: 22px;
    color: #00ff99;
    font-weight: bold;
    text-align: center;
}

/* 🎯 સાચા જવાબ માટે ઝબકતું લીલું એનિમેશન બોક્સ */
.correct-box {
    background-color: rgba(0, 255, 100, 0.25) !important;
    border: 3px solid #00ff66 !important;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 0px 20px #00ff66;
    animation: success-glow 0.6s ease-in-out infinite alternate;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
}
@keyframes success-glow {
    from { box-shadow: 0px 0px 10px #00ff66; }
    to { box-shadow: 0px 0px 30px #00ff66; }
}

/* ❌ ખોટા જવાબ માટે ધ્રુજતું લાલ એનિમેશન બોક્સ */
.wrong-box {
    background-color: rgba(255, 0, 50, 0.25) !important;
    border: 3px solid #ff3333 !important;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 0px 20px #ff3333;
    animation: shake-anim 0.15s ease-in-out infinite;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
}
@keyframes shake-anim {
    0% { transform: translateX(0); }
    25% { transform: translateX(-6px); }
    75% { transform: translateX(6px); }
    100% { transform: translateX(0); }
}

div[data-testid="stRadio"] label p {
    color: #000000 !important;
    font-weight: bold !important;
    font-size: 16px !important;
}

input {
    color: #000000 !important;
    font-weight: bold !important;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #00ffff, #00ff99) !important;
    color: black !important;
    border: none !important;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    height: 40px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🎮 રિવિઝન અને ટેસ્ટ માટેની શ્રેષ્ઠ રમત</div>", unsafe_allow_html=True)
st.markdown('<a href="./" target="_blank" style="display:block; text-align:center; width:100%; background:linear-gradient(90deg, #ff007f, #ffaa00); color:white; font-size:18px; font-weight:bold; padding:12px; border-radius:8px; text-decoration:none; box-shadow:0 0 15px rgba(255,0,127,0.4); margin-bottom:15px;">🚀 રમતને નવા ટેબમાં શરૂ કરો</a>', unsafe_allow_html=True)

# ================= 📚 સંપૂર્ણ NCERT ૧ થી ૧૨ નો માસ્ટર સિલેબસ ડેટાબેઝ =================
if "ncert_master_db" not in st.session_state:
    st.session_state.ncert_master_db = {
        "ધોરણ ૧": ["ગણિત ગમ્મત", "ગુજરાતી", "અંગ્રેજી", "હિન્દી"],
        "ધોરણ ૨": ["ગણિત ગમ્મત", "ગુજરાતી", "અંગ્રેજી", "હિન્દી"],
        "ધોરણ ૩": ["ગણિત ગમ્મત", "આસપાસ (પર્યાવરણ)", "ગુજરાતી", "અંગ્રેજી", "હિન્દી"],
        "ધોરણ ૪": ["ગણિત ગમ્મત", "આસપાસ (પર્યાવરણ)", "ગુજરાતી", "અંગ્રેજી", "હિન્દી"],
        "ધોરણ ૫": ["ગણિત ગમ્મત", "આસપાસ (પર્યાવરણ)", "ગુજરાતી", "અંગ્રેજી", "હિન્દી"],
        "ધોરણ ૬": ["વિજ્ઞાન", "ગણિત", "સામાજિક વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી", "હિન્દી", "સંસ્કૃત"],
        "ધોરણ ૭": ["વિજ્ઞાન", "ગણિત", "સામાજિક વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી", "હિન્દી", "સંસ્કૃત"],
        "ધોરણ ૮": ["વિજ્ઞાન", "ગણિત", "સામાજિક વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી", "હિન્દી", "સંસ્કૃત"],
        "ધોરણ ૯": ["વિજ્ઞાન", "ગણિત", "સામાજિક વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી", "હિન્દી", "સંસ્કૃત", "કમ્પ્યુટર પરિચય"],
        "ધોરણ ૧૦": ["સામાજિક વિજ્ઞાન", "વિજ્ઞાન", "ગણિત", "ગુજરાતી", "અંગ્રેજી", "હિન્દી", "સંસ્કૃત", "કમ્પ્યુટર પરિચય"],
        "ધોરણ ૧૧": ["ગણિત", "ભૌતિક વિજ્ઞાન", "রসાયણ વિજ્ઞાન", "જીવ વિજ્ઞાન", "સામાજિક વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી", "કમ્પ્યુટર પરિચય"],
        "ધોરણ ૧૨": ["ગણિત", "ભૌતિક વિજ્ઞાન", "રસાયણ વિજ્ઞાન", "જીવ વિજ્ઞાન", "સામાજિક વિજ્ઞાન", "ગુજરાતી", "અંગ્રેજી", "કમ્પ્યુટર પરિચય"]
    }

ss_chapters = [
    "પ્રકરણ ૧: ભારતનો વારસો", "પ્રકરણ ૨: ભારતનો સાંસ્કૃતિક વારસો: પરંપરાઓ", "પ્રકરણ ૩: ભારતનો સાંસ્કૃતિક વારસો: શિલ્પ અને સ્ถาપત્ય",
    "પ્રકરણ ૪: ભારતનો સાહિત્યિક વારસો", "પ્રકરણ ૫: ભારતનો વિજ્ઞાન અને ટેકનોલોજીનો વારસો", "પ્રકરણ ૬: ભારતના સાંસ્કૃતિક વારસાના સ્થળો",
    "પ્રકરણ ૭: આપણા વારસાનું જતન", "પ્રકરણ ૮: કુદરતી સંસાધનો", "પ્રકરણ ૯: વન અને વન્યજીવ સંસાધન", "પ્રકરણ ૧૦: ભારત: કૃષિ",
    "પ્રકરણ ૧૧: જળ સંસાધનો", "પ્રકરણ ૧૨: ખનિજ અને શક્તિના સંસાધનો", "પ્રકરણ ૧૩: ઉત્પાદન ઉદ્યોગો", "પ્રકરણ ૧૪: પરિવહન, સંદેશાવ્યવહાર અને વ્યાપાર",
    "પ્રકરણ ૧૫: આર્થિક વિકાસ", "પ્રકરણ ૧૬: આર્થિક ઉદારીકરણ અને વૈશ્વિકીકરણ", "પ્રકરણ ૧૭: આર્થિક સમસ્યાઓ અને પડકારો",
    "પ્રકરણ ૧૮: ભાવવધારો અને ગ્રાહક જાગૃતિ", "પ્રકરણ ૧૯: માનવ વિકાસ", "પ્રકરણ ૨૦: ભારતની સામાજિક સમસ્યાઓ", "પ્રકરણ ૨૧: સામાજિક પરિવર્તન"
]

sci_chapters = [
    "પ્રકરણ ૧: રાસાયણિક પ્રક્રિયાઓ અને સમીકરણો", "પ્રકરણ ૨: એસિડ, બેઇઝ અને ક્ષાર", "પ્રકરણ ૩: ધાતુઓ અને અધાતુઓ",
    "પ્રકરણ ૪: કાર્બન અને તેના સંયોજનો", "પ્રકરણ ૫: જૈવિક ક્રિયાઓ", "પ્રકરણ ૬: નિયંત્રણ અને સંકલન",
    "પ્રકરણ ૭: સજીવો કેવી રીતે પ્રજનન કરે છે?", "પ્રકરણ ૮: આનુવંશિકતા", "પ્રકરણ ૯: પ્રકાશ – પરાવર્તન અને વક્રીભવન",
    "પ્રકરણ ૧૦: માનવ આંખ અને રંગબેરંગી દુનિયા", "પ્રકરણ ૧૧: વિદ્યુત", "પ્રકરણ ૧૨: વિદ્યુત પ્રવાહની ચુંબકીય અસરો",
    "પ્રકરણ ૧૩: આપણું પર્યાવરણ"
]

math_chapters = [
    "પ્રકરણ ૧: વાસ્તવિક સંખ્યાઓ", "પ્રકરણ ૨: બહુપદીઓ", "પ્રકરણ ૩: દ્વિચલ રેખીય સમીકરણ યુગ્મ",
    "પ્રકરણ ૪: દ્વિઘાત સમીકરણ", "પ્રકરણ ૫: સમાંતર શ્રેણી", "પ્રકરણ ૬: ત્રિકોણ",
    "પ્રકરણ ૭: યામ ભૂમિતિ", "પ્રકરણ ૮: ત્રિકોણમિતિનો પરિચય", "પ્રકરણ ૯: ત્રિકોણમિતિના ઉપયોગો",
    "પ્રકરણ ૧૦: વર્તુળ", "પ્રકરણ ૧૧: વર્તુળ સંબંધિત ક્ષેત્રફળ", "પ્રકરણ ૧૨: પૃષ્ઠફળ અને ઘનફળ",
    "પ્રકરણ ૧૩: આંકડાશાસ્ત્ર", "પ્રકરણ ૧૪: સંભાવના"
]

# ================= 🤖 ૧૦૦% સિક્યોર પ્રશ્ન એન્જિન =================
def get_dynamic_question(ch_name, sub_name, q_index):
    random.seed(q_index + len(ch_name) + (111 if "સામાજિક" in sub_name else 222))
    
    if "ગણિત" in sub_name:
        val1 = random.randint(3, 12)
        val2 = random.randint(4, 11)
        correct_ans = str(val1 * val2)
        ops = [correct_ans, str(val1 * val2 + 4), str(val1 * val2 - 3), str(val1 + val2)]
        random.shuffle(ops)
        return {
            "પ્રશ્ન": f"ગણતરી કરો: {val1} × {val2} નો સાચો જવાબ નીચેનામાંથી કયો થાય?",
            "વિકલ્પો": ops,
            "સાચો": correct_ans
        }
    elif "સામાજિક" in sub_name:
        ss_pool = [
            {"પ્રશ્ન": "તાજમહાલ સ્ถาપત્ય કલા કયા મોગલ શાસકે બંધાવ્યો હતો?", "વિકલ્પો": ["અકબર", "શાહજહાં", "બાબર", "જહાંગીર"], "સાચો": "શાહજહાં"},
            {"પ્રશ્ન": "नीચેનામાંથી કયો પાક ખરીફ પાકનું મુખ્ય ઉદાહરણ છે?", "વિકલ્પો": ["ડાંગર (ચોખા)", "ઘઉં", "રાઈ", "ચણા"], "સાચો": "ડાંગર (ચોખા)"},
            {"પ્રશ્ન": "ભારત દેશ આર્થિક દૃષ્ટિએ કેવો દેશ ગણાય છે?", "વિકલ્પો": ["વિકસિત", "વિકાસશીલ", "પછાત", "સંપૂર્ણ ગરીબ"], "સાચો": "વિકાસશીલ"},
            {"પ્રશ્ન": "લોથલ સંસ્કૃતિનું પ્રખ્યાત બંદર કયા જિલ્લામાં આવેલું છે?", "વિકલ્પો": ["અમદાવાદ", "રાજકોટ", "ભાવનગર", "સુરત"], "સાચો": "અમદાવાદ"},
            {"પ્રશ્ન": "વિશ્વ ગ્રાહક અધિકાર દિન દર વર્ષે કઈ તારીખે ઉજવવામાં આવે છે?", "વિકલ્પો": ["૧૫ માર્ચ", "૨૪ ડિસેમ્બર", "૧૦ જાન્યુઆરી", "૫ ઓગસ્ટ"], "સાચો": "૧૫ માર્ચ"}
        ]
        return ss_pool[q_index % len(ss_pool)]
    else:
        sci_pool = [
            {"પ્રશ્ન": "એસિડ સ્વાદે કેવા હોય છે?", "વિકલ્પો": ["ખાટા", "તૂરા", "કડવા", "મીઠા"], "સાચો": "ખાટા"},
            {"પ્રશ્ન": "ભૂરા લિટમસ પત્રને લાલ કોણ બનાવે છે?", "વિકલ્પો": ["એસિડ", "બેઇઝ", "ક્ષાર", "નિસ્યંદિત પાણી"], "સાચો": "એસિડ"},
            {"પ્રશ્ન": "પાણીનું રાસાયણિક સૂત્ર નીચેનામાંથી કયું છે?", "વિકલ્પો": ["H2O", "CO2", "O2", "NaCl"], "સાચો": "H2O"},
            {"પ્રશ્ન": "શૂન્યાવકાશમાં પ્રકાશનો વેગ કેટલો હોય છે?", "વિકલ્પો": ["૩×૧ો⁸ મીટર/સેકંડ", "૩×૧૦⁶ મીટર/સેકંડ", "૩×૧૦⁵ મીટર/સેકંડ", "૧.૫×૧૦⁸ મીટર/સેકંડ"], "સાચો": "૩×૧૦⁸ મીટર/સેકંડ"},
            {"પ્રશ્ન": "આપણા શરીરમાં પિત્તરસનો સ્ત્રાવ કયા અંગમાંથી થાય છે?", "વિકલ્પો": ["યકૃત (લીવર)", "સ્વાદુપિંડ", "જઠર", "નાનું આંતરડું"], "સાચો": "યકૃત (લીવર)"}
        ]
        return sci_pool[q_index % len(sci_pool)]

# સેશન સ્ટેટ્સ કંટ્રોલ
if "question_index" not in st.session_state: st.session_state.question_index = 1
if "score" not in st.session_state: st.session_state.score = 0
if "player_name" not in st.session_state: st.session_state.player_name = "આયુષ"
if "game_finished" not in st.session_state: st.session_state.game_finished = False
if "animation_trigger" not in st.session_state: st.session_state.animation_trigger = None

# ================= 🕹️ ગેમ સેટઅપ લોબી બોક્સ =================
st.markdown("<div class='game-container'>", unsafe_allow_html=True)
st.subheader("⚙️ રમત સેટઅપ લોબી")

નામ = st.text_input("✍️ તમારું નામ લખો:", value=st.session_state.player_name)
if નામ: st.session_state.player_name = નામ.strip()

std_list = list(st.session_state.ncert_master_db.keys())
default_std_index = std_list.index("ધોરણ ૧૦") if "ધોરણ ૧૦" in std_list else 0
ધોરણ = st.selectbox("🎯 ધોરણ પસંદ કરો:", std_list, index=default_std_index)

sub_list = st.session_state.ncert_master_db[ધોરણ]
વિષય = st.selectbox("📚 વિષય પસંદ કરો:", sub_list)

ch_list = []
if "સામાજિક" in વિષય:
    ch_list = ss_chapters
elif "વિજ્ઞાન" in વિષય:
    ch_list = sci_chapters
elif "ગણિત" in વિષય:
    ch_list = math_chapters
else:
    for i in range(1, 16):
        ch_list.append(f"પ્રકરણ {i}: પાઠ્યપુસ્તક પ્રકરણ {i}")

પ્રકરણ = st.selectbox("📖 પ્રકરણ પસંદ કરો:", ch_list)
quiz_limit = st.selectbox("📊 કેટલા પ્રશ્નો રમવા છે?", [10, 20, 30, 40, 50, 100], index=0)

current_game_id = f"{ધોરણ}_{વિષય}_{પ્રકરણ}_{quiz_limit}"
if "last_game_id" not in st.session_state or st.session_state.last_game_id != current_game_id:
    st.session_state.last_game_id = current_game_id
    st.session_state.score = 0
    st.session_state.question_index = 1
    st.session_state.game_finished = False
    st.session_state.animation_trigger = None

if st.button("🎮 નવી મેચ શરૂ કરો"):
    play_sound("click")
    st.session_state.score = 0
    st.session_state.question_index = 1
    st.session_state.game_finished = False
    st.session_state.animation_trigger = None
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# ================= 🎯 ક્વિઝ રમવાનો ઝોન =================
st.markdown("<div class='game-container'>", unsafe_allow_html=True)

if st.session_state.game_finished:
    st.balloons()
    st.success(f"🎉 અદ્ભુત! તમે કુલ {quiz_limit} પ્રશ્નોની આખી ચેલેન્જ પૂરી કરી લીધી!")
    st.markdown(f"### 🎯 તમારો અંતિમ સ્કોર: **{st.session_state.score}**")
    
    if st.button("🔄 ફરીથી રમો"):
        play_sound("click")
        st.session_state.score = 0
        st.session_state.question_index = 1
        st.session_state.game_finished = False
        st.session_state.animation_trigger = None
        st.rerun()
else:
    st.markdown(f"<div class='score'>🏆 ચાલુ સ્કોર : {st.session_state.score}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:16px; color:#00ffff; font-weight:bold;'>📘 {ધોરણ} | {વિષય} | પ્રશ્ન ક્રમાંક: {st.session_state.question_index} / {quiz_limit}</div>", unsafe_allow_html=True)

    # 🚨 એનિમેશન ડિસ્પ્લે લોજિક (જવાબ આપ્યા પછી ઝબકશે)
    if st.session_state.animation_trigger == "correct":
        st.markdown("<div class='correct-box'>🎉 અદભુત! સાચો જવાબ છે! (+૧૦ પોઈન્ટ્સ)</div>", unsafe_allow_html=True)
        st.session_state.animation_trigger = None
        time.sleep(1.2)
        st.rerun()
    elif st.session_state.animation_trigger == "wrong":
        st.markdown("<div class='wrong-box'>❌ અરેરે! ખોટો જવાબ છે! (-૫ પોઈન્ટ્સ)</div>", unsafe_allow_html=True)
        st.session_state.animation_trigger = None
        time.sleep(1.2)
        st.rerun()

    q = get_dynamic_question(પ્રકરણ, વિષય, st.session_state.question_index)

    st.markdown(f"<div class='question'>પ્રશ્ન {st.session_state.question_index}: {q['પ્રશ્ન']}</div>", unsafe_allow_html=True)
    st.write("")

    answer = st.radio("સાચો જવાબ પસંદ કરો:", q["વિકલ્પો"], index=None, key=f"radio_choice_{st.session_state.question_index}")

    colA, colB = st.columns(2)

    with colA:
        if st.button("✅ જવાબ સબમિટ કરો"):
            play_sound("click")
            if answer is None or answer == "":
                st.warning("કૃપા કરીને પહેલા કોઈ એક વિકલ્પ પસંદ કરો!")
            else:
                if answer == q["સાચો"]:
                    st.session_state.score += 10
                    play_sound("correct")
                    st.session_state.animation_trigger = "correct"
                else:
                    st.session_state.score -= 5
                    play_sound("wrong")
                    st.session_state.animation_trigger = "wrong"
                
                if st.session_state.question_index >= quiz_limit:
                    if st.session_state.player_name != "":
                        c.execute("INSERT INTO scores(name, score, standard, subject) VALUES(?,?,?,?)",
                                  (st.session_state.player_name, st.session_state.score, ધોરણ, વિષય))
                        conn.commit()
                    st.session_state.game_finished = True
                else:
                    st.session_state.question_index += 1
                    
                st.rerun()

    with colB:
        if st.button("⏭️ પ્રશ્ન સ્કીપ કરો"):
            play_sound("click")
            if st.session_state.question_index >= quiz_limit:
                if st.session_state.player_name != "":
                    c.execute("INSERT INTO scores(name, score, standard, subject) VALUES(?,?,?,?)",
                                  (st.session_state.player_name, st.session_state.score, ધોરણ, વિષય))
                    conn.commit()
                st.session_state.game_finished = True
            else:
                st.session_state.question_index += 1
            st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# ================= 🏅 લીડરબોર્ડ =================
st.markdown("<div class='game-container'>", unsafe_allow_html=True)
st.subheader("🏅 અસલી ડેટાબેઝ લીડરબોર્ડ (ટોપ ૫ રેકોર્ડ)")

leaderboard = c.execute(
    "SELECT name, score FROM scores WHERE standard=? AND subject=? ORDER BY score DESC LIMIT 5",
    (ધોરણ, વિષય)
).fetchall()

if leaderboard:
    for i, row in enumerate(leaderboard, start=1):
        st.write(f"🌟 {i}. **{row[0]}** - {row[1]} પોઈન્ટ્સ")
else:
    st.write("હજી સુધી આ વિષયમાં ડેટાબેઝમાં કોઈ સ્કોર સેવ નથી થયો!")
st.markdown("</div>", unsafe_allow_html=True)
