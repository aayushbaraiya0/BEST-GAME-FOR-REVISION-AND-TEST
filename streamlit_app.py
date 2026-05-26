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

# ================= 🔊 SFX & MUSIC AUDIO SYSTEM =================
def play_sound(path, loop=False):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
        loop_attr = "loop" if loop else ""
        md = f"""
        <audio autoplay {loop_attr} style="display:none;">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# 🎵 બેકગ્રાઉન્ડ મ્યુઝિક
play_sound("background.mp3", loop=True)

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

.chapter {
    font-size: 16px;
    color: #00ffff;
    font-weight: bold;
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
.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 12px #00ffff;
}

.new-tab-btn {
    display: block;
    text-align: center;
    width: 100%;
    background: linear-gradient(90deg, #ff007f, #ffaa00) !important;
    color: white !important;
    font-size: 18px !important;
    font-weight: bold !important;
    padding: 12px;
    border-radius: 8px;
    text-decoration: none !important;
    box-shadow: 0 0 15px rgba(255, 0, 127, 0.4);
    transition: 0.3s ease;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🎮 BEST GAME FOR REVISION AND TEST</div>", unsafe_allow_html=True)
st.markdown('<a href="./" target="_blank" class="new-tab-btn">🚀 START GAME IN NEW TAB</a>', unsafe_allow_html=True)

# ================= 📚 સંપૂર્ણ NCERT ડેટાબેઝ (૧ થી ૨૧ સામાજિક વિજ્ઞાનના પ્રકરણો સાથે) =================
if "ncert_master_db" not in st.session_state:
    st.session_state.ncert_master_db = {
        "Std 10": {
            "સામાજિક વિજ્ઞાન (Social Science)": [
                "Ch 1: ભારતનો વારસો", "Ch 2: ભારતનો સાંસ્કૃતિક વારસો: પરંપરાઓ", "Ch 3: ભારતનો સાંસ્કૃતિક વારસો: શિલ્પ અને સ્થાપત્ય", 
                "Ch 4: ભારતનો સાહિત્યિક વારસો", "Ch 5: ભારતનો વિજ્ઞાન અને ટેકનોલોજીનો વારસો", "Ch 6: ભારતના સાંસ્કૃતિક વારસાના સ્થળો", 
                "Ch 7: આપણા વારસાનું જતન", "Ch 8: કુદરતી સંસાધનો", "Ch 9: વન અને વન્યજીવ સંસાધન", "Ch 10: ભારત: કૃષિ", 
                "Ch 11: જળ સંસાધનો", "Ch 12: ખનિજ અને શક્તિના સંસાધનો", "Ch 13: ઉત્પાદન ઉદ્યોગો", "Ch 14: પરિવહન, સંદેશાવ્યવહાર અને વ્યાપાર", 
                "Ch 15: આર્થિક विकास", "Ch 16: આર્થિક ઉદારીકરણ અને વૈશ્વિકીકરણ", "Ch 17: આર્થિક સમસ્યાઓ અને પડકારો: ગરીબી અને બેરોજગારી", 
                "Ch 18: ભાવવધારો અને ગ્રાહક જાગૃતિ", "Ch 19: માનવ વિકાસ", "Ch 20: ભારતની સામાજિક સમસ્યાઓ અને પડકારો", "Ch 21: સામાજિક પરિવર્તન"
            ],
            "વિજ્ઞાન (Science)": [
                "Ch 1: રાસાયણિક પ્રક્રિયાઓ અને સમીકરણો", "Ch 2: એસિડ, બેઇઝ અને ક્ષાર", "Ch 3: ધાતુઓ અને અધાતુઓ", "Ch 4: કાર્બન અને તેના સંયોજનો", 
                "Ch 5: જૈવિક ક્રિયાઓ", "Ch 6: નિયંત્રણ અને સંકલન", "Ch 7: સજીવો કેવી રીતે પ્રજનન કરે છે?", "Ch 8: આનુવંશિકતા", 
                "Ch 9: પ્રકાશ – પરાવર્તન અને વક્રીભવન", "Ch 10: માનવ આંખ અને રંગબેરંગી દુનિયા", "Ch 11: વિદ્યુત", "Ch 12: વિદ્યુત પ્રવાહની ચુંબકીય અસરો", "Ch 13: આપણું પર્યાવરણ"
            ],
            "ગણિત (Maths)": [
                "Ch 1: વાસ્તવિક સંખ્યાઓ", "Ch 2: બહુપદીઓ", "Ch 3: દ્વિચલ રેખીય સમીકરણ યુગ્મ", "Ch 4: દ્વિઘાત સમીકરણ", 
                "Ch 5: સમાંતર શ્રેણી", "Ch 6: ત્રિકોણ", "Ch 7: યામ ભૂમિતિ", "Ch 8: ત્રિકોણમિતિનો પરિચય", "Ch 9: ત્રિકોણમિતિના ઉપયોગો", 
                "Ch 10: વર્તુળ", "Ch 11: વર્તુળ સંબંધિત ક્ષેત્રફળ", "Ch 12: પૃષ્ઠફળ અને ઘનફળ", "Ch 13: આંકડાશાસ્ત્ર", "Ch 14: સંભાવના"
            ],
            "ગુજરાતી (Gujarati)": ["Ch 1: મોરલી", "Ch 2: શરણાઈના સૂર", "Ch 3: પ્રયાણ", "Ch 4: જીવન અંજલિ થાજો", "Ch 5: શ્વેત ક્રાંતિના પ્રણેતા", "Ch 6: વાયરલ ઇન્ફેક્શન", "Ch 7: કાળુ અને રાજુ", "Ch 8: દીકરી", "Ch 9: ચોપડાની પીળી મશ", "Ch 10: ડાંગવનો અને..."],
            "અંગ્રેજી (English)": ["Ch 1: Against the Odds", "Ch 2: The Human Robot", "Ch 3: An Interview with Arun Krishnamurthy", "Ch 4: A Wonderful Creation", "Ch 5: Playing with Fire"]
        },
        "Std 9": {
            "વિજ્ઞાન (Science)": ["Ch 1: આપણી આસપાસમાં દ્રવ્ય", "Ch 2: શું આપણી આસપાસના દ્રવ્યો શુદ્ધ છે?", "Ch 5: કોષ: જીવનનો પાયાનો એકમ"],
            "ગણિત (Maths)": ["Ch 1: સંખ્યા પદ્ધતિ", "Ch 2: બહુપદીઓ", "Ch 3: યામ ભૂમિતિ"]
        },
        "Std 1 થી 8": {
            "ગણિત ગમ્મત (Maths)": ["Ch 1: આકારો અને જગ્યા", "Ch 2: સંખ્યાઓની ગમ્મત", "Ch 1: સંમેય સંખ્યાઓ"],
            "પર્યાવરણ / વિજ્ઞાન": ["Ch 1: પૂનમે શું જોયું?", "Ch 1: આહારના ઘટકો"]
        }
    }

# ================= 🤖 ૧૦૦% પાવરફુલ ઓરિજિનલ ક્વેશ્ચન મશીન =================
# 🚨 વધારાના ટેક્સ્ટ પ્રિફિક્સ સાવ હટાવી દીધા છે - ડાયરેક્ટ સવાલ જ આવશે
def get_dynamic_question(ch_name, sub_name, q_index):
    random.seed(q_index + len(ch_name) + int(time.time() * 10) % 1000)
    
    if "ગણિત" in sub_name or "Maths" in sub_name:
        val1 = random.randint(2, 12)
        val2 = random.randint(3, 11)
        correct_ans = str(val1 * val2)
        ops = [correct_ans, str(val1 * val2 + 4), str(val1 * val2 - 3), str(val1 + val2)]
        random.shuffle(ops)
        return {
            "પ્રશ્ન": f"ગણતરી કરો: {val1} × {val2} નો સાચો જવાબ નીચેનામાંથી કયો થાય?",
            "વિકલ્પો": ops,
            "સાચો": correct_ans
        }
    elif "સામાજિક વિજ્ઞાન" in sub_name or "Social Science" in sub_name:
        ss_pool = [
            ("તાજમહાલ સ્થાપત્ય કલા કયા મોગલ શાસકે બંધાવ્યો હતો?", ["અકબર", "શાહજહાં", "બાબર"], "શાહજહાં"),
            ("નીચેનામાંથી કયો પાક ખરીફ પાકનું મુખ્ય ઉદાહરણ છે?", ["ડાંગર (ચોખા)", "ઘઉં", "રાઈ"], "ડાંગર (ચોખા)"),
            ("ભારત દેશ આર્થિક દૃષ્ટિએ કેવો દેશ ગણાય છે?", ["વિકસિત", "વિકાસશીલ", "પછાત"], "વિકાસશીલ"),
            ("લોથલ સંસ્કૃતિનું પ્રખ્યાત બંદર કયા જિલ્લામાં આવેલું છે?", ["અમદાવાદ", "રાજકોટ", "ભાવનગર"], "અમદાવાદ"),
            ("ભારતનો ભવ્ય સાંસ્કૃતિક વારસો શાના માટે જાણીતો છે?", ["વિવિધતા અને સમૃદ્ધિ", "માત્ર યુદ્ધો", "ગરીબી"], "વિવિધતા અને સમૃદ્ધિ")
        ]
        return random.choice(ss_pool)
    elif "વિજ્ઞાન" in sub_name or "Science" in sub_name:
        sci_pool = [
            ("એસિડ સ્વાદે કેવા હોય છે?", ["ખાટા", "તૂરા", "કડવા"], "ખાટા"),
            ("ભૂરા લિટમસ પત્રને લાલ કોણ બનાવે છે?", ["એસિડ", "બેઇઝ", "ક્ષાર"], "એસિડ"),
            ("પાણીનું રાસાયણિક સૂત્ર નીચેનામાંથી કયું છે?", ["H2O", "CO2", "O2"], "H2O"),
            ("શૂન્યાવકાશમાં પ્રકાશનો વેગ કેટલો હોય છે?", ["૩×૧૦⁸ મીટર/સેકંડ", "૩×૧૦⁶ મીટર/સેકંડ", "૩×૧૦⁵ મીટર/સેકંડ"], "૩×૧૦⁸ મીટર/સેકંડ")
        ]
        return random.choice(sci_pool)
    else:
        return {
            "પ્રશ્ન": "પાઠ્યપુસ્તકના ઊંડાણપૂર્વકના અભ્યાસ પ્રમાણે નીચેનામાંથી કયો વિકલ્પ સાચો છે?",
            "વિકલ્પો": ["સાચો વિકલ્પ", "ખોટું વિધાન", "માહિતી અધૂરી છે"],
            "સાચો": "સાચો વિકલ્પ"
        }

# સેશન સ્ટેટ્સ કંટ્રોલ
if "question_index" not in st.session_state: st.session_state.question_index = 1
if "score" not in st.session_state: st.session_state.score = 0
if "player_name" not in st.session_state: st.session_state.player_name = "Aayush"
if "game_finished" not in st.session_state: st.session_state.game_finished = False

# ================= 🕹️ ગેમ સેટઅપ લોબી બોક્સ =================
st.markdown("<div class='game-container'>", unsafe_allow_html=True)
st.subheader("⚙️ ગેમ સેટઅપ લોબી")

નામ = st.text_input("✍️ તમારું નામ લખો:", value=st.session_state.player_name)
if નામ: st.session_state.player_name = નામ.strip()

std_list = list(st.session_state.ncert_master_db.keys())

default_std_index = std_list.index("Std 10") if "Std 10" in std_list else 0
ધોરણ = st.selectbox("🎯 ધોરણ (Standard) પસંદ કરો:", std_list, index=default_std_index)

sub_data = st.session_state.ncert_master_db[ધોરણ]
sub_list = list(sub_data.keys())
વિષય = st.selectbox("📚 વિષય (Subjects) પસંદ કરો:", sub_list)

ch_list = sub_data[વિષય]
પ્રકરણ = st.selectbox("📖 પ્રકરણ (Chapters) પસંદ કરો:", ch_list)

quiz_limit = st.selectbox("📊 કેટલા MCQ રમવા છે?", [10, 20, 30, 40, 50, 100], index=0)

if st.button("🎮 નવી મેચ શરૂ કરો (રીસેટ)"):
    play_sound("click.mp3")
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
        play_sound("click.mp3")
        st.session_state.score = 0
        st.session_state.question_index = 1
        st.session_state.game_finished = False
        st.rerun()
else:
    st.markdown(f"<div class='score'>🏆 ચાલુ સ્કોર : {st.session_state.score}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chapter'>📘 {ધોરણ} | {વિષય} | પ્રશ્ન ક્રમાંક: {st.session_state.question_index} / {quiz_limit}</div>", unsafe_allow_html=True)

    # પ્રશ્ન મેળવવો
    q = get_dynamic_question(પ્રકરણ, વિષય, st.session_state.question_index)

    # 🚨 ડાયરેક્ટ પાઠ્યપુસ્તક જેવો ચોખ્ખો પ્રશ્ન જ દેખાશે
    st.markdown(f"<div class='question'>પ્રશ્ન {st.session_state.question_index}: {q['પ્રશ્ન']}</div>", unsafe_allow_html=True)
    st.write("")

    answer = st.radio("સાચો જવાબ પસંદ કરો:", q["વિકલ્પો"], index=None, key=f"radio_opt_{st.session_state.question_index}_{પ્રકરણ}")

    colA, colB = st.columns(2)

    with colA:
        if st.button("✅ જવાબ સબમિટ કરો"):
            play_sound("click.mp3")
            if answer is None:
                st.warning("કૃપા કરીને પહેલા કોઈ એક વિકલ્પ પસંદ કરો!")
            else:
                if answer == q["સાચો"]:
                    st.success("સાચો જવાબ 🎉 (+10)")
                    st.session_state.score += 10
                    play_sound("correct.mp3")
                else:
                    st.error("ખોટો જવાબ ❌ (-5)")
                    st.info(f"સાચો જવાબ હતો: {q['સાચો']}")
                    st.session_state.score -= 5
                    play_sound("wrong.mp3")
                
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
            play_sound("click.mp3")
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
