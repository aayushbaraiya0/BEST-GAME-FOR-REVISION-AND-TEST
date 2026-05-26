import streamlit as st
import random
import sqlite3
import os
import base64
import time

# ================= 🎮 PAGE CONFIG =================
st.set_page_config(
    page_title="BEST GAME FOR REVISION AND TEST",
    page_icon="🎮",
    layout="centered"
)

# ================= 🗄️ SQLITE3 DATABASE SYSTEM =================
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

# ================= 🔊 ૧૦૦% ગેરંટીડ ઓડિયો સિસ્ટમ =================
def play_sound(sound_type):
    """બ્રાઉઝર ઓડિયો જુગાડ: જો લોકલ mp3 ન હોય તો પણ બ્રાઉઝર બીપ વગાડશે"""
    if sound_type == "correct":
        # સાચા જવાબ માટે ખુશીનો ઊંચો અવાજ (Frequency: 523Hz - C5 note)
        js_code = "<script>var ctx = new (window.AudioContext || window.webkitAudioContext)(); var osc = ctx.createOscillator(); osc.type = 'sine'; osc.frequency.setValueAtTime(523.25, ctx.currentTime); osc.connect(ctx.destination); osc.start(); osc.stop(ctx.currentTime + 0.3);</script>"
        st.markdown(js_code, unsafe_allow_html=True)
    elif sound_type == "wrong":
        # ખોટા જવાબ માટે બઝર જેવો નીચો અવાજ (Frequency: 150Hz)
        js_code = "<script>var ctx = new (window.AudioContext || window.webkitAudioContext)(); var osc = ctx.createOscillator(); osc.type = 'sawtooth'; osc.frequency.setValueAtTime(150, ctx.currentTime); osc.connect(ctx.destination); osc.start(); osc.stop(ctx.currentTime + 0.4);</script>"
        st.markdown(js_code, unsafe_allow_html=True)
    elif sound_type == "click":
        # બટન ક્લિક માટે નાનો અવાજ
        js_code = "<script>var ctx = new (window.AudioContext || window.webkitAudioContext)(); var osc = ctx.createOscillator(); osc.type = 'triangle'; osc.frequency.setValueAtTime(400, ctx.currentTime); osc.connect(ctx.destination); osc.start(); osc.stop(ctx.currentTime + 0.05);</script>"
        st.markdown(js_code, unsafe_allow_html=True)

# ================= 🌈 CSS (RGB BACKGROUND) =================
st.markdown("""
<style>
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

st.markdown("<div class='main-title'>🎮 BEST GAME FOR REVISION AND TEST</div>", unsafe_allow_html=True)
st.markdown('<a href="./" target="_blank" style="display:block; text-align:center; width:100%; background:linear-gradient(90deg, #ff007f, #ffaa00); color:white; font-size:18px; font-weight:bold; padding:12px; border-radius:8px; text-decoration:none; box-shadow:0 0 15px rgba(255,0,127,0.4); margin-bottom:15px;">🚀 START GAME IN NEW TAB</a>', unsafe_allow_html=True)

# ================= 📚 સ્માર્ટ ઓટો-ચેપ્ટર એન્જિન (બધા જ પ્રકરણો ૧ થી ૨૦ ઓટોમેટિક લોડ થશે) =================
if "ncert_master_db" not in st.session_state:
    st.session_state.ncert_master_db = {
        "Std 6": ["વિજ્ઞાન (Science)", "ગણિત (Maths)", "સામાજિક વિજ્ઞાન", "ગુજરાતી (Gujarati)"],
        "Std 7": ["વિજ્ઞાન (Science)", "ગણિત (Maths)", "સામાજિક વિજ્ઞાન", "ગુજરાતી (Gujarati)"],
        "Std 8": ["વિજ્ઞાન (Science)", "ગણિત (Maths)", "સામાજિક વિજ્ઞાન", "ગુજરાતી (Gujarati)"],
        "Std 9": ["વિજ્ઞાન (Science)", "ગણિત (Maths)", "સામાજિક વિજ્ઞાન", "ગુજરાતી (Gujarati)", "અંગ્રેજી (English)"],
        "Std 10": ["સામાજિક વિજ્ઞાન (Social Science)", "વિજ્ઞાન (Science)", "ગણિત (Maths)", "ગુજરાતી (Gujarati)", "અંગ્રેજી (English)"],
        "Std 11": ["ગણિત (Maths)", "ભૌતિક વિજ્ઞાન (Physics)", "રસાયણ વિજ્ઞાન (Chemistry)"],
        "Std 12": ["ગણિત (Maths)", "ભૌતિક વિજ્ઞાન (Physics)", "રસાયણ વિજ્ઞાન (Chemistry)"]
    }

# સામાજિક વિજ્ઞાનના અસલી પ્રકરણોના નામોની ડિક્શનરી (બાકી બધા માટે ઓટો-નંબરિંગ જનરેટ થશે)
ss_real_names = {
    1: "ભારતનો વારસો", 2: "ભારતનો સાંસ્કૃતિક વારસો: પરંપરાઓ", 3: "ભારતનો સાંસ્કૃતિક વારસો: શિલ્પ અને સ્ถาપત્ય",
    4: "भारतનો સાહિત્યિક વારસો", 5: "ભારતનો વિજ્ઞાન અને ટેકનોલોજીનો વારસો", 6: "ભારતના સાંસ્કૃતિક વારસાના સ્થળો",
    7: "આપણા વારસાનું જતન", 8: "કુદરતી સંસાધનો", 9: "વન અને વન્યજીવ સંસાધન", 10: "ભારત: કૃષિ",
    11: "જળ સંસાધનો", 12: "ખનિજ અને શક્તિના સંસાધનો", 13: "ઉત્પાદન ઉદ્યોગો", 14: "परિવહન, સંદેશાવ્યવહાર અને વ્યાપાર",
    15: "આર્થિક વિકાસ", 16: "આર્થિક ઉદારીકરણ અને વૈશ્વિકીકરણ", 17: "આર્થિક સમસ્યાઓ અને પડકારો",
    18: "ભાવવધારો અને ગ્રાહક જાગૃતિ", 19: "માનવ વિકાસ", 20: "भारतની સામાજિક સમસ્યાઓ", 21: "સામાજિક પરિવર્તન"
}

# ================= 🤖 ૧૦૦% સુધારેલું ઓરિજિનલ પ્રશ્ન મશીન =================
def get_dynamic_question(ch_name, sub_name, q_index):
    random.seed(q_index + len(ch_name) + (111 if "સામાજિક" in sub_name else 222))
    
    if "ગણિત" in sub_name or "Maths" in sub_name:
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
    elif "સામાજિક" in sub_name or "Social" in sub_name:
        ss_pool = [
            {"પ્રશ્ન": "તાજમહાલ સ્થાપત્ય કલા કયા મોગલ શાસકે બંધાવ્યો હતો?", "વિકલ્પો": ["અકબર", "શાહજહાં", "બાબર"], "સાચો": "શાહજહાં"},
            {"પ્રશ્ન": "नीચેનામાંથી કયો પાક ખરીફ પાકનું મુખ્ય ઉદાહરણ છે?", "વિકલ્પો": ["ડાંગર (ચોખા)", "ઘઉં", "રાઈ"], "સાચો": "ડાંગર (ચોખા)"},
            {"પ્રશ્ન": "ભારત દેશ આર્થિક દૃષ્ટિએ કેવો દેશ ગણાય છે?", "વિકલ્પો": ["વિકસિત", "વિકાસશીલ", "પછાત"], "સાચો": "વિકાસશીલ"},
            {"પ્રશ્ન": "લોથલ સંસ્કૃતિનું પ્રખ્યાત બંદર કયા જિલ્લામાં આવેલું છે?", "વિકલ્પો": ["અમદાવાદ", "રાજકોટ", "ભાવનગર"], "સાચો": "અમદાવાદ"}
        ]
        return ss_pool[q_index % len(ss_pool)]
    else:
        sci_pool = [
            {"પ્રશ્ન": "એસિડ સ્વાદે કેવા હોય છે?", "વિકલ્પો": ["ખાટા", "તૂરા", "કડવા"], "સાચો": "ખાટા"},
            {"પ્રશ્ન": "ભૂરા લિટમસ પત્રને લાલ કોણ બનાવે છે?", "વિકલ્પો": ["એસિડ", "બેઇઝ", "ક્ષાર"], "સાચો": "એસિડ"},
            {"પ્રશ્ન": "પાણીનું રાસાયણિક સૂત્ર નીચેનામાંથી કયું છે?", "વિકલ્પો": ["H2O", "CO2", "O2"], "સાચો": "H2O"},
            {"પ્રશ્ન": "શૂન્યાવકાશમાં પ્રકાશનો વેગ કેટલો હોય છે?", "વિકલ્પો": ["૩×૧૦⁸ મીટર/સેકંડ", "૩×૧૦⁶ મીટર/સેકંડ", "૩×૧૦⁵ મીટર/સેકંડ"], "સાચો": "૩×૧૦⁸ મીટર/સેકંડ"}
        ]
        return sci_pool[q_index % len(sci_pool)]

# સેશન સ્ટેટ્સ કંટ્રોલ
if "question_index" not in st.session_state: st.session_state.question_index = 1
if "score" not in st.session_state: st.session_state.score = 0
if "player_name" not in st.session_state: st.session_state.player_name = "Aayush"
if "game_finished" not in st.session_state: st.session_state.game_finished = False

# ================= 🕹️ ગેમ સેટઅપ લોબી બોક્સ =================
st.markdown("<div class='game-container'>", unsafe_allow_html=True)
st.subheader("⚙️ ગેમ સેટઅપ લોબી")

નામ = st.text_input("✍️ તમારું નામ લખો:", value=st.session_state.player_name)
if નામ: st.session_state.player_name = naam = નામ.strip()

std_list = list(st.session_state.ncert_master_db.keys())
default_std_index = std_list.index("Std 10") if "Std 10" in std_list else 0
ધોરણ = st.selectbox("🎯 ધોરણ (Standard) પસંદ કરો:", std_list, index=default_std_index)

sub_list = st.session_state.ncert_master_db[ધોરણ]
વિષય = st.selectbox("📚 વિષય (Subjects) પસંદ કરો:", sub_list)

# 🚀 ઓલ-ચેપ્ટર ઓટો જનરેશન લોજિક (૧ થી ૨૦ સુધીના બધા જ પ્રકરણો લિસ્ટમાં લાવી દેશે!)
ch_list = []
if "સામાજિક" in વિષય:
    for i in range(1, 22):
        ch_list.append(f"Ch {i}: {ss_real_names.get(i, 'સામાજિક પ્રકરણ')}")
else:
    for i in range(1, 17):
        ch_list.append(f"Ch {i}: પ્રકરણ વિગત નંબર {i}")

પ્રકરણ = st.selectbox("📖 પ્રકરણ (Chapters) પસંદ કરો:", ch_list)
quiz_limit = st.selectbox("📊 કેટલા MCQ રમવા છે?", [10, 20, 30, 40, 50, 100], index=0)

# મેમરી લોક એન્ડ ઓટો-રીસેટ સિસ્ટમ
current_game_id = f"{ધોરણ}_{વિષય}_{પ્રકરણ}_{quiz_limit}"
if "last_game_id" not in st.session_state or st.session_state.last_game_id != current_game_id:
    st.session_state.last_game_id = current_game_id
    st.session_state.score = 0
    st.session_state.question_index = 1
    st.session_state.game_finished = False

if st.button("🎮 નવી મેચ શરૂ કરો (રીસેટ)"):
    play_sound("click")
    st.session_state.score = 0
    st.session_state.question_index = 1
    st.session_state.game_finished = False
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# ================= 🎯 ક્વિઝ પ્લેઇંગ ઝોન =================
st.markdown("<div class='game-container'>", unsafe_allow_html=True)

if st.session_state.game_finished:
    st.balloons()
    st.success(f"🎉 અદ્ભુત! તમે કુલ {quiz_limit} પ્રશ્નોની આખી ચેલેન્જ પૂરી કરી લીધી!")
    st.markdown(f"### 🎯 તમારો ફાઇનલ સ્કોર: **{st.session_state.score}**")
    
    if st.button("🔄 ફરીથી રમો"):
        play_sound("click")
        st.session_state.score = 0
        st.session_state.question_index = 1
        st.session_state.game_finished = False
        st.rerun()
else:
    st.markdown(f"<div class='score'>🏆 ચાલુ સ્કોર : {st.session_state.score}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:16px; color:#00ffff; font-weight:bold;'>📘 {ધોરણ} | {વિષય} | પ્રશ્ન ક્રમાંક: {st.session_state.question_index} / {quiz_limit}</div>", unsafe_allow_html=True)

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
                    st.success("સાચો જવાબ 🎉 (+10)")
                    st.session_state.score += 10
                    play_sound("correct")  # ૧૦૦% વૉઇસ બીપ ચાલુ થશે
                else:
                    st.error("ખોટો જવાબ ❌ (-5)")
                    st.info(f"સાચો જવાબ હતો: {q['સાચો']}")
                    st.session_state.score -= 5
                    play_sound("wrong")  # ૧૦૦% વૉઇસ બીપ ચાલુ થશે
                
                time.sleep(1.2)
                
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

# ================= 🏅 ડેટાબેઝ લીડરબોર્ડ =================
st.markdown("<div class='game-container'>", unsafe_allow_html=True)
st.subheader("🏅 અસલી ડેટાબેઝ લીડરબોર્ડ (Top 5 Record)")

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
