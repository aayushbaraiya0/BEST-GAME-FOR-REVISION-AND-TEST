import streamlit as st
import random
import json
import os
import base64
import time

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="ગુજરાતી એક્ઝામ ગેમ",
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
</style>
""", unsafe_allow_html=True)

# 🎮 મેઈન ટાઇટલ હેડર
st.markdown("<div class='main-title'>🎮 BEST GAME FOR REVISION AND TEST</div>", unsafe_allow_html=True)

# 📚 ૧ થી ૧૨ ધોરણના તમામ વિષયો અને અસલી ચેપ્ટર્સનો પૂલ
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = {
        "Std 1": {"ગણિત ગમ્મત": ["Ch 1: આકારો અને જગ્યા"], "ગુજરાતી (કલરવ)": ["Ch 1: શાળા તત્પરતા ૧"]},
        "Std 2": {"ગણિત ગમ્મત": ["Ch 1: શું લાંબું છે, શું ગોળ છે?"], "ગુજરાતી": ["Ch 1: શરણાઈ, ઢોલક અને રંગ"]},
        "Std 3": {"ગણિત": ["Ch 1: ક્યાંથી જોવું?"], "આસપાસ (પર્યાવરણ)": ["Ch 1: પૂનમે શું જોયું?"]},
        "Std 4": {"ગણિત": ["Ch 1: ઈંટોની ઈમારત"], "ગુજરાતી": ["Ch 1: ખિસ્સામાં પહલવાન"]},
        "Std 5": {"ગણિત": ["Ch 1: રાષ્ટ્રીય ફળ કેરી"], "ગુજરાતી": ["Ch 1: મજાની ઇન્દ્રિયો"]},
        "Std 6": {
            "ગણિત (Maths)": ["Ch 1: આપણી સંખ્યાઓને જાણવી"],
            "વિજ્ઞાન (Science)": ["Ch 1: આહારના ઘટકો"],
            "ગુજરાતી": ["Ch 1: રેલવે સ્ટેશન"]
        },
        "Std 7": {"ગણિત": ["Ch 1: પૂર્ણાંક સંખ્યાઓ"], "વિજ્ઞાન": ["Ch 1: વનસ્પતિમાં પોષણ"]},
        "Std 8": {"ગણિત": ["Ch 1: સંમેય સંખ્યાઓ"], "વિજ્ઞાન": ["Ch 1: પાક ઉત્પાદન અને વ્યવસ્થાપન"]},
        "Std 9": {
            "ગણિત (Maths)": ["Ch 1: સંખ્યા પદ્ધતિ"],
            "વિજ્ઞાન (Science)": ["Ch 1: આપણી આસપાસમાં દ્રવ્ય"]
        },
        "Std 10": {
            "ગણિત (Maths)": ["Ch 1: વાસ્તવિક સંખ્યાઓ", "Ch 2: બહુપદીઓ", "Ch 5: સમાંતર શ્રેણી"],
            "વિજ્ઞાન (Science)": ["Ch 1: રાસાયણિક પ્રક્રિયાઓ", "Ch 2: એસિડ, બેઇઝ અને ક્ષાર", "Ch 10: પ્રકાશ-પરાવર્તન"],
            "ગુજરાતી (Gujarati)": ["Ch 1: મોરલી", "Ch 2: શરણાઈના સૂર"],
            "અંગ્રેજી (English)": ["Ch 1: Against the Odds"]
        },
        "Std 11": {"ગણિત": ["Ch 1: ગણ"], "ભૌતિક વિજ્ઞાન": ["Ch 1: એકમ અને માપન"]},
        "Std 12": {"ગણિત": ["Ch 1: સંબંધ અને વિધેય"], "ભૌતિક વિજ્ઞાન": ["Ch 1: વિદ્યુત ક્ષેત્રો"]}
    }

# 📝 સાચા બોર્ડ લેવલના પ્રશ્નોનો લોડર
quiz_questions = {
    "Ch 1: વાસ્તવિક સંખ્યાઓ": [
        {"પ્રશ્ન": "૨ અને ૩ નો લઘુત્તમ સમાપવર્તક (LCM) કેટલો થાય?", "වિકલ્પો": ["૩", "૬", "૯", "૧૨"], "સાચો": "૬"},
        {"પ્રશ્ન": "૫ નો સાચો વર્ગ કેટલો થાય?", "વિકલ્પો": ["૧૦", "૧૫", "૨૫", "૨૦"], "સાચો": "૨૫"}
    ],
    "Ch 2: બહુપદીઓ": [
        {"પ્રશ્ન": "દ્વિઘાત બહુપદી x² + 7x + 10 ના શૂન્યોનો સરવાળો કેટલો થાય?", "වિકલ્પો": ["૭", "-૭", "૧૦", "-૧૦"], "સાચો": "-૭"}
    ],
    "Ch 10: પ્રકાશ-પરાવર્તન": [
        {"પ્રશ્ન": "શૂન્યાવકાશમાં પ્રકાશની અસલી ગતિ કેટલી હોય છે?", "વિકલ્પો": ["૩×૧૦⁸ મીટર/સેકંડ", "૩×૧૦⁶ મીટર/સેકંડ", "૩×૧૦⁴ મીટર/સેકંડ"], "સાચો": "૩×૧૦⁸ મીટર/સેકંડ"}
    ],
    "Ch 1: મોરલી": [
        {"પ્રશ્ન": "'મોરલી' પદના રચયિતાનું નામ જણાવો:", "વિકલ્પો": ["નરસિંહ મહેતા", "મીરાંબાઈ", "દયારામ"], "સાચો": "મીરાંબાઈ"}
    ]
}

# અનંત પ્રશ્નો આપમેળે હવામાંથી બનાવતું સ્માર્ટ એન્જિન (ગ્લિચ ફ્રી)
def generate_dynamic_question(ch_name):
    if "ગણિત" in ch_name or "સંખ્યાઓ" in ch_name or "બહુપદીઓ" in ch_name:
        a = random.randint(2, 9)
        b = random.randint(2, 10)
        return {
            "પ્રશ્ન": f"[MATH RUN] {ch_name} કન્સેપ્ટ મુજબ, {a} × {b} નો સાચો જવાબ શું થાય?",
            "વિકલ્પો": [str(a*b), str(a*b+4), str(a*b-2), str(a+b)],
            "સાચો": str(a*b)
        }
    else:
        return {
            "પ્રશ્ન": f"[REVISION RUN] {ch_name} ના આપેલા આ વિકલ્પોમાંથી સૌથી સાચું વિધાન કયું છે?",
            "વિકલ્પો": ["સાચો વિકલ્પ", "ખોટો વિકલ્પ", "અધૂરી માહિતી"],
            "સાચો": "સાચો વિકલ્પ"
        }

# ================= સેશન સ્ટેટ્સ કંટ્રોલ =================
if "question_index" not in st.session_state: st.session_state.question_index = 0
if "score" not in st.session_state: st.session_state.score = 0
if "player_name" not in st.session_state: st.session_state.player_name = "Aayush"

# ================= 🕹️ સિંગલ સ્લિમ ગેમ કન્ટેનર ઝોન =================
st.markdown("<div class='game-container'>", unsafe_allow_html=True)

# ✍️ લોબી સેટઅપ ઇનપુટ્સ
નામ = st.text_input("✍️ તમારું નામ લખો:", value=st.session_state.player_name)
if નામ: st.session_state.player_name = નામ.strip()

std_list = list(st.session_state.quiz_data.keys())
ધોરણ = st.selectbox("🎯 ધોરણ પસંદ કરો (Std 1 to 12):", std_list, index=std_list.index("Std 10") if "Std 10" in std_list else 0)

# ડાયનેમિક સબ્જેક્ટ લોડર
sub_data = st.session_state.quiz_data[ધોરણ]
sub_list = list(sub_data.keys()) if isinstance(sub_data, dict) else ["સામાન્ય જ્ઞાન"]
વિષય = st.selectbox("📚 વિષય પસંદ કરો:", sub_list)

# ડાયનેમિક ચેપ્ટર લોડર
ch_list = sub_data[વિષય] if isinstance(sub_data, dict) and વિષય in sub_data else [f"Ch 1: ઓલ-ઈન-વન મેગા લૂપ"]
પ્રકરણ = st.selectbox("📖 પ્રકરણ પસંદ કરો:", ch_list)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ક્વિઝ એન્જિન રન ----------------
st.markdown("<div class='game-container'>", unsafe_allow_html=True)

st.markdown(f"<div class='score'>🏆 સ્કોર : {st.session_state.score}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='chapter'>📘 પ્રકરણ: {પ્રकरण}</div>", unsafe_allow_html=True)

# પ્રશ્નો મેળવવા
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

# 🖤 ઓપ્શન્સ બોક્સ (આ હવે પર્ફેક્ટ કાળા અક્ષરોમાં દેખાશે)
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
