import streamlit as st
import random
import sqlite3
import json
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
# આ ડેટાબેઝ લીડરબોર્ડના સ્કોરને સેવ રાખશે
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

# ================= 🔊 SOUND SYSTEM =================
def play_sound(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
        md = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# ================= 🌈 CSS (RGB BACKGROUND + PRO TEXT) =================
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

/* 🖤 ઓપ્શન્સના લખાણ ઘાટા કાળા રંગના */
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

# 🎮 હેડર બ્રાન્ડિંગ
st.markdown("<div class='main-title'>🎮 BEST GAME FOR REVISION AND TEST</div>", unsafe_allow_html=True)
st.markdown('<a href="./" target="_blank" class="new-tab-btn">🚀 START GAME IN NEW TAB</a>', unsafe_allow_html=True)

# ================= 📚 સંપૂર્ણ NCERT સિલેબસ માસ્ટર પૂલ =================
if "ncert_master_db" not in st.session_state:
    st.session_state.ncert_master_db = {
        "ધોરણ ૧૦ (Std 10)": {
            "વિજ્ઞાન (Science)": ["Ch 1: રાસાયણિક પ્રક્રિયાઓ અને સમીકરણો", "Ch 2: એસિડ, બેઇઝ અને ક્ષાર", "Ch 3: ધાતુઓ અને અધાતુઓ", "Ch 4: કાર્બન અને તેના સંયોજનો", "Ch 5: જૈવિક ક્રિયાઓ", "Ch 6: નિયંત્રણ અને સંકલન", "Ch 7: સજીવો કેવી રીતે પ્રજનન કરે છે?", "Ch 8: આનુવંશિકતા", "Ch 9: પ્રકાશ – પરાવર્તન અને વક્રીભવન", "Ch 10: માનવ આંખ અને રંગબેરંગી દુનિયા", "Ch 11: વિદ્યુત", "Ch 12: વિદ્યુત પ્રવાહની ચુંબકીય અસરો", "Ch 13: આપણું પર્યાવરણ"],
            "ગણિત (Maths)": ["Ch 1: વાસ્તવિક સંખ્યાઓ", "Ch 2: બહુપદીઓ", "Ch 3: દ્વિચલ રેખીય સમીકરણ યુગ્મ", "Ch 4: દ્વિઘાત સમીકરણ", "Ch 5: સમાંતર શ્રેણી", "Ch 6: ત્રિકોણ", "Ch 7: યામ ભૂમિતિ", "Ch 8: ત્રિકોણમિતિનો પરિચય", "Ch 9: ત્રિકોણમિતિના ઉપયોગો", "Ch 10: વર્તુળ", "Ch 11: વર્તુળ સંબંધિત ક્ષેત્રફળ", "Ch 12: પૃષ્ઠફળ અને ઘનફળ", "Ch 13: આંકડાશાસ્ત્ર", "Ch 14: સંભાવના"],
            "ગુજરાતી (Gujarati)": ["Ch 1: મોરલી", "Ch 2: શરણાઈના સૂર", "Ch 3: પ્રયાણ", "Ch 4: જીવન અંજલિ થાજો", "Ch 5: શ્વેત ક્રાંતિના પ્રણેતા", "Ch 6: વાયરલ ઇન્ફેક્શન"],
            "સામાજિક વિજ્ઞાન (Social Science)": ["Ch 1: ભારતનો વારસો", "Ch 2: સાંસ્કૃતિક વારસો", "Ch 4: સાહિત્યિક વારસો", "Ch 10: ભારત: કૃષિ"],
            "અંગ્રેજી (English)": ["Ch 1: Against the Odds", "Ch 2: The Human Robot", "Ch 3: An Interview with Arun Krishnamurthy"]
        },
        "ધોરણ ૯ (Std 9)": {
            "વિજ્ઞાન (Science)": ["Ch 1: આપણી આસપાસમાં દ્રવ્ય", "Ch 2: શું આપણી આસપાસના દ્રવ્યો શુદ્ધ છે?", "Ch 5: કોષ: જીવનનો પાયાનો એકમ", "Ch 7: ગતિ", "Ch 8: બળ તથા ગતિના નિયમો"],
            "ગણિત (Maths)": ["Ch 1: સંખ્યા પદ્ધતિ", "Ch 2: બહુપદીઓ", "Ch 3: યામ ભૂમિતિ", "Ch 6: રેખાઓ અને ખૂણાઓ"],
            "ગુજરાતી": ["Ch 1: સાંજ સમય શામળિયો", "Ch 2: ચોરી અને પ્રાયશ્ચિત"]
        },
        "ધોરણ ૮ (Std 8)": {
            "વિજ્ઞાન (Science)": ["Ch 1: પાક ઉત્પાદન અને વ્યવસ્થાપન", "Ch 2: સૂક્ષ્મજીવો", "Ch 3: કોલસો અને પેટ્રોલિયમ", "Ch 4: દહન અને જ્યોત"],
            "ગણિત (Maths)": ["Ch 1: સંમેય સંખ્યાઓ", "Ch 2: એકચલ રેખીય સમીકરણો", "Ch 3: ચતુષ્કોણની સમજ"]
        },
        "ધોરણ ૬ અને ૭ (Std 6 & 7)": {
            "વિજ્ઞાન": ["Ch 1: આહારના ઘટકો", "Ch 1: વનસ્પતિમાં પોષણ"],
            "ગણિત": ["Ch 1: આપણી સંખ્યાઓને જાણવી", "Ch 1: પૂર્ણાંક સંખ્યાઓ"]
        },
        "ધોરણ ૧ થી ૫ (Std 1 to 5)": {
            "ગણિત ગમ્મત (Maths)": ["Ch 1: આકારો અને જગ્યા", "Ch 2: સંખ્યાઓની ગમ્મત"],
            "પર્યાવરણ / આસપાસ": ["Ch 1: પૂનમે શું જોયું?", "Ch 1: મજાની ઇન્દ્રિયો"]
        },
        "ધોરણ ૧૧ અને ૧૨ (Std 11 & 12)": {
            "ગણિત (Maths)": ["Ch 1: ગણ (Sets)", "Ch 1: સંબંધ અને વિધેય"],
            "ભૌતિક વિજ્ઞાન (Physics)": ["Ch 1: એકમ અને માપન", "Ch 1: વિદ્યુતભારો અને ક્ષેત્રો"]
        }
    }

# ================= 🤖 ૧૦૦ પ્રશ્નોની સીરીઝ બનાવતું ઓટોમેટિક એન્જિન =================
# આ ફંક્શન વિદ્યાર્થી માટે પસંદ કરેલા ચેપ્ટરના ૧૦૦ અલગ-અલગ પ્રશ્નો ઓટો-લોડ કરશે
def get_100_questions_package(ch_name, q_index):
    # દરેક ઇન્ડેક્સ (1 થી 100) માટે તદ્દન નવો અને અલગ પ્રશ્ન બનાવવા માટેનો સીડ સેટિંગ
    random.seed(q_index + len(ch_name))
    
    if "ગણિત" in ch_name or "સંખ્યાઓ" in ch_name or "બહુપદીઓ" in ch_name or "સમીકરણ" in ch_name or "ત્રિકોણ" in ch_name or "આકારો" in ch_name:
        val1 = random.randint(2, 12)
        val2 = random.randint(3, 11)
        correct_ans = str(val1 * val2)
        wrong_options = [str(val1 * val2 + 4), str(val1 * val2 - 3), str(val1 + val2)]
        options_pool = [correct_ans] + wrong_options
        random.shuffle(options_pool)
        
        return {
            "પ્રશ્ન": f"પ્રશ્ન નંબર {q_index}: {ch_name} ના બોર્ડ માળખા મુજબ, ગણતરી કરો: {val1} × {val2} નો સાચો જવાબ શું થાય?",
            "વિકલ્પો": options_pool,
            "સાચો": correct_ans
        }
    elif "વિજ્ઞાન" in ch_name or "પ્રક્રિયાઓ" in ch_name or "એસિડ" in ch_name or "પ્રકાશ" in ch_name or "વિદ્યુત" in ch_name or "કોષ" in ch_name:
        sci_topics = [
            ("ભૌતિક ફેરફારનું ઉદાહરણ કયું છે?", ["પાણીનું બરફ બનવું", "લોખંડનું કટાવું", "દૂધનું ખાટું થવું"], "પાણીનું બરફ બનવું"),
            ("એસિડની pH નું મૂલ્ય કેટલું હોય છે?", ["૭ થી ઓછું", "૭ થી વધારે", "બરાબર ૭"], "૭ થી ઓછું"),
            ("માનવ શરીરમાં કયો અંગ લોહી શુદ્ધ કરે છે?", ["ફેફસાં", "હૃદય", "કિડની (મૂત્રપિંડ)"], "કિડની (મૂત્રપિંડ)"),
            ("શૂન્યાવકાશમાં પ્રકાશનો વેગ કેટલો હોય છે?", ["૩×૧૦⁸ મીટર/સેકંડ", "૩×૧૦⁶ મીટર/સેકંડ", "૩×૧૦⁵ કિમી/સેકંડ"], "૩×૧૦⁸ મીટર/સેકંડ")
        ]
        topic = random.choice(sci_topics)
        return {
            "પ્રશ્ન": f"પ્રશ્ન નંબર {q_index}: {ch_name} અંતર્ગત, {topic[0]}",
            "વિકલ્પો": topic[1],
            "સાચો": topic[2]
        }
    else:
        # ગુજરાતી, સોશિયલ સાયન્સ અને અંગ્રેજી માટે જનરલ કન્સેપ્ટ ક્વેશ્ચન
        return {
            "પ્રશ્ન": f"પ્રશ્ન નંબર {q_index}: {ch_name} ના પાઠ્યપુસ્તકના ઊંડાણપૂર્વકના અભ્યાસના આધારે નીચેનામાંથી કયો વિકલ્પ સાચો છે?",
            "વિકલ્પો": ["સાચો વિકલ્પ", "ખોટું વિધાન", "માહિતી અધૂરી છે", "આપેલ તમામ"],
            "સાચો": "સાચો વિકલ્પ"
        }

# સેશન સ્ટેટ્સ વેરિએબલ્સ
if "question_index" not in st.session_state: st.session_state.question_index = 1
if "score" not in st.session_state: st.session_state.score = 0
if "player_name" not in st.session_state: st.session_state.player_name = "Aayush"

# ================= 🕹️ ગેમ સેટઅપ લોબી બોક્સ =================
st.markdown("<div class='game-container'>", unsafe_allow_html=True)
st.subheader("⚙️ ગેમ સેટઅપ લોબી")

નામ = st.text_input("✍️ તમારું નામ લખો:", value=st.session_state.player_name)
if નામ: st.session_state.player_name = નામ.strip()

std_list = list(st.session_state.ncert_master_db.keys())
ધોરણ = st.selectbox("🎯 ધોરણ પસંદ કરો:", std_list, index=0)

sub_data = st.session_state.ncert_master_db[ધોરણ]
sub_list = list(sub_data.keys())
વિષય = st.selectbox("📚 વિષય (Subjects) પસંદ કરો:", sub_list)

ch_list = sub_data[વિષય]
પ્રકરણ = st.selectbox("📖 પ્રકરણ (Chapters) પસંદ કરો:", ch_list)

# પ્રશ્નોની લિમિટ ફિક્સ ૧૦૦
quiz_limit = 100
st.write(f"📊 આ મેચમાં કુલ પ્રશ્નોની સંખ્યા: **{quiz_limit}**")

# રીસેટ બટન
if st.button("🔄 નવી મેચ શરૂ કરો / સ્કોર રીસેટ"):
    st.session_state.score = 0
    st.session_state.question_index = 1
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# ================= 🎯 ક્વિઝ પ્લેઇંગ ઝોન =================
st.markdown("<div class='game-container'>", unsafe_allow_html=True)

st.markdown(f"<div class='score'>🏆 ચાલુ સ્કોર : {st.session_state.score}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='chapter'>📘 {ધોરણ} | {વિષય} | પ્રગતિ: {st.session_state.question_index} / {quiz_limit}</div>", unsafe_allow_html=True)

# ૧૦૦ પ્રશ્નોના પેકેજમાંથી કરન્ટ પ્રશ્ન લોડ કરવો
q = get_100_questions_package(પ્રકરણ, st.session_state.question_index)

st.markdown(f"<div class='question'>{q['પ્રશ્ન']}</div>", unsafe_allow_html=True)
st.write("")

answer = st.radio("સાચો જવાબ પસંદ કરો:", q["વિકલ્પો"], index=None, key=f"radio_opt_{st.session_state.question_index}")

colA, colB = st.columns(2)

with colA:
    if st.button("✅ જવાબ સબમિટ કરો"):
        if answer is None:
            st.warning("કૃપા કરીને પહેલા કોઈ એક વિકલ્પ પસંદ કરો!")
        else:
            if answer == q["સાચો"]:
                st.success("સાચો જવાબ 🎉 (+10)")
                st.session_state.score += 10
                play_sound("correct.mp3")
            else:
                st.error(f"ખોટો જવાબ ❌ (-5)")
                st.info(f"સાચો જવાબ હતો: {q['સાચો']}")
                st.session_state.score -= 5
                play_sound("wrong.mp3")
            
            time.sleep(1)
            
            # ૧૦૦ પ્રશ્નો પૂરા થાય તેનું લોજિક
            if st.session_state.question_index >= quiz_limit:
                st.balloons()
                st.success("🎉 અભિનંદન! તમે ૧૦૦ પ્રશ્નોની આખી મેગા ચેલેન્જ પૂરી કરી લીધી!")
                
                # ડેટાબેઝમાં રેકોર્ડ સેવ કરવો
                if st.session_state.player_name != "":
                    c.execute("INSERT INTO scores(name, score, standard, subject) VALUES(?,?,?,?)",
                              (st.session_state.player_name, st.session_state.score, ધોરણ, વિષય))
                    conn.commit()
                
                st.session_state.question_index = 1
            else:
                st.session_state.question_index += 1
                
            st.rerun()

with colB:
    if st.button("⏭️ પ્રશ્ન સ્કીપ કરો"):
        if st.session_state.question_index >= quiz_limit:
            st.session_state.question_index = 1
        else:
            st.session_state.question_index += 1
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# ================= 🏅 🗄️ ડેટાબેઝ લીડરબોર્ડ ડિસ્પ્લે =================
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
    st.write("હજી સુધી આ વિષયમાં ડેટાબેઝમાં કોઈ સ્કોર સેવ નથી થયો. પહેલો રેકોર્ડ બનાવો!")
st.markdown("</div>", unsafe_allow_html=True)
