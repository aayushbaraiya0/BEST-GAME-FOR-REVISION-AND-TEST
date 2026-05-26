import streamlit as st
import random
import json
import os
import base64
import time

# ================= PAGE CONFIG (અહીં નામ બદલી નાખ્યું છે) =================
st.set_page_config(
    page_title="BEST GAME FOR REVISION AND TEST",
    page_icon="🎮",
    layout="centered"
)

# ================= SOUND SYSTEM =================
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

# ================= CSS (RGB Animation + Black Text Options) =================
st.markdown("""
<style>
/* 🌈 પ્યોર RGB કલર-ચેન્જિંગ બેકગ્રાઉન્ડ એનિમેશન */
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

/* સિંગલ સ્લિમ બોક્સ કન્ટેનર લુક */
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

/* 🖤 રેડિયો ઓપ્શન્સના અક્ષરો એકદમ ઘાટા કાળા (Black) */
div[data-testid="stRadio"] label p {
    color: #000000 !important;
    font-weight: bold !important;
    font-size: 16px !important;
}

/* ઇનપુટ બોક્સના અક્ષરો કાળા કરવા */
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
.new-tab-btn:hover {
    transform: scale(1.02);
    box-shadow: 0 0 25px #ff007f;
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# 🎮 ઓફિશિયલ બ્રાન્ડિંગ હેડર
st.markdown("<div class='main-title'>🎮 BEST GAME FOR REVISION AND TEST</div>", unsafe_allow_html=True)

# 🚀 નવું ટેબ ઓપન કરવા માટેનું બટન
st.markdown('<a href="./" target="_blank" class="new-tab-btn">🚀 START GAME IN NEW TAB</a>', unsafe_allow_html=True)

# ================= 📚 NCERT માસ્ટર ડેટાબેઝ પૂલ (Std 1 to 12) =================
if "ncert_master_db" not in st.session_state:
    st.session_state.ncert_master_db = {
        "ધોરણ ૧૦ (Std 10)": {
            "વિજ્ઞાન (Science)": ["Ch 1: રાસાયણિક પ્રક્રિયાઓ", "Ch 2: એસિડ, બેઇઝ અને ક્ષાર", "Ch 3: ધાતુઓ અને અધાતુઓ", "Ch 4: કાર્બન અને તેના સંયોજનો", "Ch 5: તત્વોનું આવર્તી વર્ગીકરણ", "Ch 6: જૈવિક ક્રિયાઓ", "Ch 7: નિયંત્રણ અને સંકલન", "Ch 8: સજીવો કેવી રીતે પ્રજનન કરે છે?", "Ch 9: આનુવંશિકતા", "Ch 10: પ્રકાશ-પરાવર્તન", "Ch 11: માનવ આંખ અને રંગબેરંગી દુનિયા", "Ch 12: વિદ્યુત", "Ch 13: વિદ્યુત પ્રવાહની ચુંબકીય અસરો", "Ch 14: ઊર્જાના સ્ત્રોતો", "Ch 15: આપણું પર્યાવરણ"],
            "ગણિત (Maths)": ["Ch 1: વાસ્તવિક સંખ્યાઓ", "Ch 2: બહુપદીઓ", "Ch 3: દ્વિચલ રેખીય સમીકરણ", "Ch 4: દ્વિઘાત સમીકરણ", "Ch 5: સમાંતર શ્રેણી", "Ch 6: ત્રિકોણ", "Ch 7: યામ ભૂમિતિ", "Ch 8: ત્રિકોણમિતિનો પરિચય", "Ch 9: ત્રિકોણમિતિના ઉપયોગો", "Ch 10: વર્તુળ", "Ch 11: રચના", "Ch 12: વર્તુળ સંબંધિત ક્ષેત્રફળ", "Ch 13: પૃષ્ઠફળ અને ઘનફળ", "Ch 14: આંકડાશાસ્ત્ર", "Ch 15: સંભાવના"],
            "ગુજરાતી (Gujarati)": ["Ch 1: મોરલી", "Ch 2: શરણાઈના સૂર", "Ch 3: વૈષ્ણવજન", "Ch 4: જીવન અંજલિ થાજો", "Ch 5: શ્વેત ક્રાંતિના પ્રણેતા"],
            "સામાજિક વિજ્ઞાન (Social Science)": ["Ch 1: ભારતનો વારસો", "Ch 2: સાંસ્કૃતિક વારસો", "Ch 4: સાહિત્યિક વારસો", "Ch 10: ભારત: કૃષિ"],
            "અંગ્રેજી (English)": ["Ch 1: Against the Odds", "Ch 2: The Human Robot", "Ch 3: An Interview with Arun Krishnamurthy"]
        },
        "ધોરણ ૯ (Std 9)": {
            "વિજ્ઞાન (Science)": ["Ch 1: આપણી આસપાસમાં દ્રવ્ય", "Ch 2: શું આપણી આસપાસના દ્રવ્યો શુદ્ધ છે?", "Ch 5: કોષ: જીવનનો પાયાનો એકમ", "Ch 8: ગતિ", "Ch 9: બળ તથા ગતિના નિયમો"],
            "ગણિત (Maths)": ["Ch 1: સંખ્યા પદ્ધતિ", "Ch 2: બહુપદીઓ", "Ch 3: યામ ભૂમિતિ", "Ch 6: રેખાઓ અને ખૂણાઓ"],
            "ગુજરાતી": ["Ch 1: છપ્પા", "Ch 2: ચોરી અને પ્રાયશ્ચિત"]
        },
        "ધોરણ ૮ (Std 8)": {
            "વિજ્ઞાન": ["Ch 1: પાક ઉત્પાદન", "Ch 2: સૂક્ષ્મજીવો", "Ch 11: બળ અને દબાણ"],
            "ગણિત": ["Ch 1: સંમેય સંખ્યાઓ", "Ch 2: એકચલ રેખીય સમીકરણ"]
        },
        "ધોરણ ૭ (Std 7)": {
            "વિજ્ઞાન": ["Ch 1: વનસ્પતિમાં પોષણ", "Ch 2: પ્રાણીઓમાં પોષણ"],
            "ગણિત": ["Ch 1: પૂર્ણાંક સંખ્યાઓ"]
        },
        "ધોરણ ૬ (Std 6)": {
            "વિજ્ઞાન (Science)": ["Ch 1: આહારના ઘટકો", "Ch 2: વસ્તુઓના જૂથ બનાવવા"],
            "ગણિત (Maths)": ["Ch 1: આપણી સંખ્યાઓને જાણવી"],
            "ગુજરાતી (Gujarati)": ["Ch 1: રેલવે સ્ટેશન"]
        },
        "ધોરણ ૧ થી ૫ (Std 1 to 5)": {
            "ગણિત ગમ્મત / આસપાસ": ["Ch 1: આકારો અને જગ્યા", "Ch 1: રાષ્ટ્રીય ફળ કેરી", "Ch 1: પૂનમે શું જોયું?", "Ch 1: મજાની ઇન્દ્રિયો"]
        },
        "ધોરણ ૧૧ અને ૧૨ (Std 11 & 12)": {
            "ગણિત (Maths)": ["Ch 1: ગણ (Sets)", "Ch 1: સંબંધ અને વિધેય"],
            "ભૌતિક વિજ્ઞાન (Physics)": ["Ch 1: એકમ અને માપન", "Ch 1: વિદ્યુત ક્ષેત્રો"],
            "રસાયણ વિજ્ઞાન (Chemistry)": ["Ch 1: રસાયણ વિજ્ઞાનની પાયાની વિભાવનાઓ"]
        }
    }

# 📝 બોર્ડ એક્ઝામના મોસ્ટ ઈમ્પોર્ટન્ટ પ્રશ્નો
quiz_questions = {
    "Ch 1: વાસ્તવિક સંખ્યાઓ": [
        {"પ્રશ્ન": "૨ અને ૩ નો લઘુત્તમ સમાપવર્તક (LCM) કેટલો થાય?", "વિકલ્પો": ["૩", "૬", "૯", "૧૨"], "સાચો": "૬"},
        {"પ્રશ્ન": "૫ નો સાચો વર્ગ કેટલો થાય?", "વિકલ્પો": ["૧૦", "૧૫", "૨૫", "૨૦"], "સાચો": "૨૫"}
    ],
    "Ch 2: બહુપદીઓ": [
        {"પ્રશ્ન": "દ્વિઘાત બહુપદી x² + 7x + 10 ના શૂન્યોનો સરવાળો કેટલો થાય?", "વિકલ્પો": ["૭", "-૭", "૧૦", "-૧૦"], "સાચો": "-૭"}
    ],
    "Ch 10: પ્રકાશ-પરાવર્તન": [
        {"પ્રશ્ન": "શૂન્યાવકાશમાં પ્રકાશની અસલી ગતિ કેટલી હોય છે?", "વિકલ્પો": ["૩×૧૦⁸ મીટર/સેકંડ", "૩×૧૦⁶ મીટર/સેકંડ", "૩×૧૦⁴ મીટર/સેકંડ"], "સાચો": "૩×૧૦⁸ મીટર/સેકંડ"}
    ],
    "Ch 1: મોરલી": [
        {"પ્રશ્ન": "'મોરલી' પદના રચયિતાનું નામ જણાવો:", "વિકલ્પો": ["નરસિંહ મહેતા", "મીરાંબાઈ", "દયારામ"], "સાચો": "મીરાંબાઈ"}
    ],
    "Ch 1: Against the Odds": [
        {"પ્રશ્ન": "How many years did the residents of Taj Nagar wait for the railway station?", "વિકલ્પો": ["11 years", "21 years", "25 years"], "સાચો": "21 years"}
    ],
    "Ch 5: કોષ: જીવનનો પાયાનો એકમ": [
        {"પ્રશ્ન": "કોષનું પાવર હાઉસ નીચેનામાંથી કોને કહેવામાં આવે છે?", "વિકલ્પો": ["કેન્દ્રક", "ક્લોરોપ્લાસ્ટ", "કણાભસૂત્ર (Mitochondria)"], "સાચો": "કણાભસૂત્ર (Mitochondria)"}
    ]
}

# 🚀 ઓલ-ઇન-વન NCERT ડાયનેમિક ક્વેશ્ચન એન્જિન
def generate_dynamic_question(ch_name):
    if "ગણિત" in ch_name or "સંખ્યાઓ" in ch_name or "બહુપદીઓ" in ch_name:
        a = random.randint(3, 9)
        b = random.randint(3, 10)
        return {
            "પ્રશ્ન": f"[NCERT MATH RUN] {ch_name} પ્રકરણના નિયમ મુજબ, {a} × {b} નો સાચો જવાબ શું થાય?",
            "વિકલ્પો": [str(a*b), str(a*b+4), str(a*b-2), str(a+b)],
            "સાચો": str(a*b)
        }
    else:
        return {
            "પ્રશ્ન": f"[NCERT REVISION] {ch_name} ના આપેલા આ વિકલ્પોમાંથી પાઠ્યપુસ્તક મુજબ સૌથી સાચો ઓપ્શન કયો છે?",
            "વિકલ્પો": ["સાચો વિકલ્પ", "ખોટો વિધાન", "માહિતી અસ્પષ્ટ છે", "આપેલ તમામ"],
            "સાચો": "સાચો વિકલ્પ"
        }

# સેશન સ્ટેટ્સ કંટ્રોલ
if "question_index" not in st.session_state: st.session_state.question_index = 0
if "score" not in st.session_state: st.session_state.score = 0
if "player_name" not in st.session_state: st.session_state.player_name = "Aayush"

# ================= 🕹️ સિંગલ સ્લિમ ગેમ કન્ટેનર ઝોન =================
st.markdown("<div class='game-container'>", unsafe_allow_html=True)

# લોબી ઇનપુટ્સ
નામ = st.text_input("✍️ તમારું નામ લખો:", value=st.session_state.player_name)
if નામ: st.session_state.player_name = નામ.strip()

std_list = list(st.session_state.ncert_master_db.keys())
ધોરણ = st.selectbox("🎯 ધોરણ પસંદ કરો:", std_list, index=0)

sub_data = st.session_state.ncert_master_db[ધોરણ]
sub_list = list(sub_data.keys()) if isinstance(sub_data, dict) else ["સામાન્ય જ્ઞાન"]
વિષય = st.selectbox("📚 વિષય (Subjects) પસંદ કરો:", sub_list)

ch_list = sub_data[વિષય] if isinstance(sub_data, dict) and વિષય in sub_data else [f"Ch 1: ઓલ-ઈન-વન મેગા લૂપ"]
પ્રકરણ = st.selectbox("📖 પ્રકરણ (Chapters) પસંદ કરો:", ch_list)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ક્વિઝ બોક્સ રન ----------------
st.markdown("<div class='game-container'>", unsafe_allow_html=True)

st.markdown(f"<div class='score'>🏆 સ્કોર : {st.session_state.score}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='chapter'>📘 {ધોરણ} | {વિષય} | {પ્રકરણ}</div>", unsafe_allow_html=True)

# પ્રશ્નો લોડિંગ
if પ્રકરણ in quiz_questions:
    questions = quiz_questions[પ્રકરણ]
else:
    random.seed(st.session_state.question_index)
    questions = [generate_dynamic_question(પ્રકરણ)]

if st.session_state.question_index >= len(questions):
    st.session_state.question_index = 0

q = questions[st.session_state.question_index]

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
                st.success("સાચો જવાબ 🎉")
                st.session_state.score += 10
                play_sound("correct.mp3")
            else:
                st.error("ખોટો જવાબ ❌")
                st.info(f"સાચો જવાબ: {q['સાચો']}")
                st.session_state.score -= 5
                play_sound("wrong.mp3")
            
            time.sleep(1)
            st.session_state.question_index += 1
            st.rerun()

with colB:
    if st.button("⏭️ આગળનો પ્રશ્ન / સ્કીપ"):
        st.session_state.question_index += 1
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
