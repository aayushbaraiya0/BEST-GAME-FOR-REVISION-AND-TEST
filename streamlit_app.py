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

# 🎵 બેકગ્રાઉન્ડ મ્યુઝિક ચાલુ કરો
play_sound("background.mp3", loop=True)

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

# ================= 📚 સંપૂર્ણ NCERT ૧ થી ૧૨ નો અસલી માસ્ટર સિલેબસ ડેટાબેઝ =================
if "ncert_master_db" not in st.session_state:
    st.session_state.ncert_master_db = {
        "Std 1": {
            "ગણિત ગમ્મત (Maths)": ["Ch 1: આકારો અને જગ્યા", "Ch 2: ૧ થી ૯ સુધીની સંખ્યા", "Ch 3: સરવાળા", "Ch 4: બાદબાકી", "Ch 5: ૧૦ થી ૨૦ સુધીની સંખ્યા", "Ch 6: સમય", "Ch 7: માપન", "Ch 8: ૨૧ થી ૫૦ સુધીની સંખ્યા", "Ch 9: માહિતીનો ઉપયોગ", "Ch 10: પેટર્ન", "Ch 11: સંખ્યાઓ", "Ch 12: નાણું", "Ch 13: કેટલા?"],
            "ગુજરાતી (Gujarati)": ["Ch 1: શાળા તત્પરતા ૧", "Ch 2: શાળા તત્પરતા ૨", "Ch 3: અજબ જેવી વાત છે", "Ch 4: આવરે વરસાદ", "Ch 5: અમે સૌ", "Ch 6: ઝાકળ જેવા પગલાં"]
        },
        "Std 2": {
            "ગણિત ગમ્મત (Maths)": ["Ch 1: શું લાંબું છે, શું ગોળ છે?", "Ch 2: જૂથમાં ગણતરી", "Ch 3: તમે કેટલું ઊંચકી શકો?", "Ch 4: દસ દસની ગણતરી", "Ch 5: પેટર્ન", "Ch 6: પગની છાપ", "Ch 7: જગ અને મગ", "Ch 8: દશક અને એકમ", "Ch 9: મારો મજાનો દિવસ", "Ch 10: અમારા અંકો ઉમેરો", "Ch 11: લીટીઓ જ લીટીઓ", "Ch 12: આપણે આપી શકીએ, લઈ શકીએ", "Ch 13: સૌથી લાંબો ડગલો", "Ch 14: પક્ષીઓ આવે પક્ષીઓ જાય", "Ch 15: કેટલી ચોટલી છે?"],
            "ગુજરાતી (Gujarati)": ["Ch 1: શરણાઈ, ઢોલક અને રંગ", "Ch 2: દાદા ખોવાયા છે", "Ch 3: આટલા બધા રમકડાં", "Ch 4: જંગલ બુક", "Ch 5: મારે તો બસ રમવું છે"]
        },
        "Std 3": {
            "ગણિત ગમ્મત (Maths)": ["Ch 1: ક્યાંથી જોવું?", "Ch 2: સંખ્યાની ગમ્મત", "Ch 3: આપો અને લો", "Ch 4: લાંબું અને ટૂંકું", "Ch 5: આકારો અને ભાત", "Ch 6: આપ-લેની ગમ્મત", "Ch 7: સમય વહી જાય છે", "Ch 8: કોણ ભારે છે?", "Ch 9: કેટલી વખત?", "Ch 10: ભાત(પેટર્ન)ની રમત", "Ch 11: જગ અને મગ", "Ch 12: આપણે સરખા ભાગે વહેંચી શકીશું?", "Ch 13: સ્માર્ટ ચાર્ટ", "Ch 14: રૂપિયા અને પૈસા"],
            "આસપાસ (EVS)": ["Ch 1: પૂનમે શું જોયું?", "Ch 2: વનપરી", "Ch 3: પાણી જ પાણી", "Ch 4: છોટુંનું ઘર", "Ch 5: ઘર એક શાળા", "Ch 6: ખાધા વિના ન ચાલે", "Ch 7: અનોખો સંવાદ", "Ch 8: ફર્ર્ર...", "Ch 9: આવરે વરસાદ", "Ch 10: રસોડાની વાત", "Ch 11: આપણા વાહનો", "Ch 12: આપણા કામ", "Ch 13: આપણી લાગણીઓની ભાગીદારી", "Ch 14: અમારું ખોરાક", "Ch 15: માટીની મજા"]
        },
        "Std 4": {
            "ગણિત ગમ્મત (Maths)": ["Ch 1: ઈંટોની ઇમારત", "Ch 2: લાંબું અને ટૂંકું", "Ch 3: ભોપાલનો પ્રવાસ", "Ch 4: ટીક ટીક ટીક", "Ch 5: દુનિયા જોવાનો રસ્તો", "Ch 6: ભંગાર વેચનાર", "Ch 7: જગ અને મગ", "Ch 8: ગાડું અને પૈડાં", "Ch 9: અડધું અને પા", "Ch 10: પેટર્નની રમત", "Ch 11: ઘડિયા અને ભાગાકાર", "Ch 12: કેટલું ભારે? કેટલું હલકું?", "Ch 13: ખેતર અને તેની ફરતે વાડ", "Ch 14: સ્માર્ટ ચાર્ટ"],
            "આસપાસ (EVS)": ["Ch 1: રોજ નિશાળે જઈએ", "Ch 2: કાનથી કાન", "Ch 3: નંદુ સાથે એક દિવસ", "Ch 4: અમૃતાની વાર્તા", "Ch 5: અનિતા અને મધમાખીઓ", "Ch 6: રિયાની મુસાફરી", "Ch 7: રિયાની ટ્રેન મોડી પડી", "Ch 8: રિયા મામાના ઘરે ગઈ", "Ch 9: બદલાતા કુટુંબો", "Ch 10: કબોટો, કબોટો, કબોટો", "Ch 11: વાડીમાં", "Ch 12: બદલાતો સમય", "Ch 13: નદીની સફર", "Ch 14: રાજુનું ખેતર", "Ch 15: બજારથી ઘર સુધી"]
        },
        "Std 5": {
            "ગણિત ગમ્મત (Maths)": ["Ch 1: રાષ્ટ્રીય ફળ કેરી", "Ch 2: આકાર અને ખૂણા", "Ch 3: કેટલા ચોરસ?", "Ch 4: ભાગ અને પૂર્ણ", "Ch 5: તે સરખું દેખાય છે?", "Ch 6: તું મારો ગુણક, હું તારો અવયવ", "Ch 7: તમે પેટર્ન જોઈ શકો છો?", "Ch 8: નકશા આલેખન", "Ch 9: ખોખાં અને રેખા-ચિત્ર", "Ch 10: દશમો અને સોમો ભાગ", "Ch 11: ક્ષેત્રફળ અને વરેહવાર", "Ch 12: સ્માર્ટ ચાર્ટ્સ", "Ch 13: ગુણાકાર અને ભાગાકારની રીતો", "Ch 14: કેટલું મોટું? કેટલું ભારે?"],
            "આસપાસ (EVS)": ["Ch 1: મજાની ઇન્દ્રિયો", "Ch 2: સાપ અને મદારી", "Ch 3: સ્વાદથી પાચન સુધી", "Ch 4: કેરીઓ બારે માસ", "Ch 5: બીજ, બીજ, બીજ", "Ch 6: જળ એ જ જીવન", "Ch 7: પાણી સાથેના પ્રયોગો", "Ch 8: મચ્છર, રોગો અને સારવાર", "Ch 9: ચઢીએ ઊંચા પહાડ", "Ch 10: દીવાલોની કહાની", "Ch 11: સુનિતા અવકાશમાં", "Ch 12: જો આ ખૂટી જાય તો?", "Ch 13: પહાડી રહેઠાણ", "Ch 14: જ્યારે ધરતી ધ્રુજી ઊઠી"]
        },
        "Std 6": {
            "વિજ્ઞાન (Science)": ["Ch 1: આહારના ઘટકો", "Ch 2: વસ્તુઓના જૂથ બનાવવા", "Ch 3: પદાર્થોનું અલગીકરણ", "Ch 4: વનસ્પતિની જાણકારી મેળવીએ", "Ch 5: શરીરનું હલનચલન", "Ch 6: સજીવો અને તેમની આસપાસ", "Ch 7: ગતિ અને અંતરનું માપન", "Ch 8: પ્રકાશ, પડછાયો અને પરાવર્તન", "Ch 9: વિદ્યુત તથા પરિપથ", "Ch 10: ચુંબક સાથે ગમ્મત", "Ch 11: આપણી આસપાસની हवा"],
            "ગણિત (Maths)": ["Ch 1: આપણી સંખ્યાઓને જાણવી", "Ch 2: પૂર્ણ સંખ્યાઓ", "Ch 3: સંખ્યા સાથે રમત", "Ch 4: ભૂમિતિના પાયાના ખ્યાલો", "Ch 5: પાયાના આકારોની સમજ", "Ch 6: પૂર્ણાંક સંખ્યાઓ", "Ch 7: અપૂર્ણાંક સંખ્યાઓ", "Ch 8: દશાંશ સંખ્યાઓ", "Ch 9: માહિતીનું નિયમન", "Ch 10: ક્ષેત્રમિતિ", "Ch 11: બીજગણિત", "Ch 12: ગુણોત્તર અને પ્રમાણ"],
            "ગુજરાતી (Gujarati)": ["Ch 1: રેલવે સ્ટેશન", "Ch 2: હિંદ માતાને સંબોધન", "Ch 3: દ્વિદલ", "Ch 4: રવિશંકર મહારાજ", "Ch 5: મહેનતની મોસમ", "Ch 6: લેખણ ઝાલી નો રહી", "Ch 7: પગલે પગલે", "Ch 8: બિરબલની યુક્તિ"]
        },
        "Std 7": {
            "વિજ્ઞાન (Science)": ["Ch 1: વનસ્પતિમાં પોષણ", "Ch 2: પ્રાણીઓમાં પોષણ", "Ch 3: ઉષ્મા", "Ch 4: એસિડ, બેઇઝ અને ક્ષાર", "Ch 5: ભૌતિક અને રાસાયણિક ફેરફારો", "Ch 6: સજીવોમાં શ્વસન", "Ch 7: પ્રાણીઓ અને વનસ્પતિઓમાં વહન", "Ch 8: વનસ્પતિમાં પ્રજનન", "Ch 9: ગતિ અને સમય", "Ch 10: વિદ્યુત પ્રવાહ અને તેની અસરો", "Ch 11: પ્રકાશ", "Ch 12: વન: આપણી જીવનદોરી", "Ch 13: પ્રદૂષિત પાણીની વાર્તા"],
            "ગણિત (Maths)": ["Ch 1: પૂર્ણાંક સંખ્યાઓ", "Ch 2: અપૂર્ણાંક અને દશાંશ સંખ્યાઓ", "Ch 3: માહિતીનું નિયમન", "Ch 4: સાદા સમીકરણો", "Ch 5: રેખા અને ખૂણા", "Ch 6: ત્રિકોણ અને તેના ગુણધર્મો", "Ch 7: રાશિઓની તુલના", "Ch 8: સંમેય સંખ્યાઓ", "Ch 9: પરિમિતિ અને ક્ષેત્રફળ", "Ch 10: વૈજ્ઞાનિક પદાવલિ", "Ch 11: ઘાત અને ઘાતાંક", "Ch 12: સંમિતિ"]
        },
        "Std 8": {
            "વિજ્ઞાન (Science)": ["Ch 1: પાક ઉત્પાદન અને વ્યવસ્થાપન", "Ch 2: સૂક્ષ્મજીવો: મિત્ર અને શત્રુ", "Ch 3: કોલસો અને પેટ્રોલિયમ", "Ch 4: દહન અને જ્યોત", "Ch 5: વનસ્પતિઓ અને પ્રાણીઓનું સંરક્ષણ", "Ch 6: પ્રાણીઓમાં પ્રજનન", "Ch 7: તરુણાવસ્થા તરફ", "Ch 8: બળ અને દબાણ", "Ch 9: ઘર્ષણ", "Ch 10: ધ્વનિ", "Ch 11: વિદ્યુત પ્રવાહની રાસાયણિક અસરો", "Ch 12: કેટલીક કુદરતી ઘટનાઓ", "Ch 13: પ્રકાશ"],
            "ગણિત (Maths)": ["Ch 1: સંમેય સંખ્યાઓ", "Ch 2: એકચલ રેખીય સમીકરણો", "Ch 3: ચતુષ્કોણની સમજ", "Ch 4: માહિતીનું નિયમન", "Ch 5: વર્ગ અને વર્ગમૂળ", "Ch 6: ઘન અને ઘનમૂળ", "Ch 7: રાશિઓની તુલના", "Ch 8: બૈજિક પદાવલિઓ અને નિત્યસમ", "Ch 9: ક્ષેત્રમિતિ", "Ch 10: ઘાત અને ઘાતાંक", "Ch 11: સીધો અને વ્યસ્ત પ્રમાણ", "Ch 12: અવયવીકરણ"]
        },
        "Std 9": {
            "વિજ્ઞાન (Science)": ["Ch 1: આપણી આસપાસમાં દ્રવ્ય", "Ch 2: શું આપણી આસપાસના દ્રવ્યો શુદ્ધ છે?", "Ch 3: પરમાણુઓ અને અણુઓ", "Ch 4: પરમાણુનું બંધારણ", "Ch 5: કોષ: જીવનનો પાયાનો એકમ", "Ch 6: પેશીઓ", "Ch 7: ગતિ", "Ch 8: બળ તથા ગતિના નિયમો", "Ch 9: ગુરુત્વાકર્ષણ", "Ch 10: કાર્ય અને ઊર્જા", "Ch 11: ધ્વનિ", "Ch 12: અન્ન સ્ત્રોતોમાં સુધારણા"],
            "ગણિત (Maths)": ["Ch 1: સંખ્યા પદ્ધતિ", "Ch 2: બહુપદીઓ", "Ch 3: યામ ભૂમિતિ", "Ch 4: દ્વિચલ રેખીય સમીકરણો", "Ch 5: યુક્લિડની ભૂમિતિનો પરિચય", "Ch 6: રેખાઓ અને ખૂણાઓ", "Ch 7: ત્રિકોણ", "Ch 8: ચતુષ્કોણ", "Ch 9: વર્તુળ", "Ch 10: હેરોનનું સૂત્ર", "Ch 11: પૃષ્ઠફળ અને ઘનફળ", "Ch 12: આંકડાશાસ્ત્ર"],
            "ગુજરાતી (Gujarati)": ["Ch 1: સાંજ સમય શામળિયો", "Ch 2: ચોરી અને પ્રાયશ્ચિત", "Ch 3: પછે શામળિયોજી બોલિયા", "Ch 4: ગોપાળબાપા", "Ch 5: ગુર્જરીના ગૃહકુંજે"]
        },
        "Std 10": {
            "વિજ્ઞાન (Science)": ["Ch 1: રાસાયણિક પ્રક્રિયાઓ અને સમીકરણો", "Ch 2: એસિડ, બેઇઝ અને ક્ષાર", "Ch 3: ધાતુઓ અને અધાતુઓ", "Ch 4: કાર્બન અને તેના સંયોજનો", "Ch 5: જૈવિક ક્રિયાઓ", "Ch 6: નિયંત્રણ અને સંકલન", "Ch 7: સજીવો કેવી રીતે પ્રજનન કરે છે?", "Ch 8: આનુવંશિકતા", "Ch 9: પ્રકાશ – પરાવર્તન અને વક્રીભવન", "Ch 10: માનવ આંખ અને રંગબેરંગી દુનિયા", "Ch 11: વિદ્યુત", "Ch 12: વિદ્યુત પ્રવાહની ચુંબકીય અસરો", "Ch 13: આપણું પર્યાવરણ"],
            "ગણિત (Maths)": ["Ch 1: વાસ્તવિક સંખ્યાઓ", "Ch 2: બહુપદીઓ", "Ch 3: દ્વિચલ રેખીય સમીકરણ યુગ્મ", "Ch 4: દ્વિઘાત સમીકરણ", "Ch 5: સમાંતર શ્રેણી", "Ch 6: ત્રિકોણ", "Ch 7: યામ ભૂમિતિ", "Ch 8: ત્રિકોણમિતિનો પરિચય", "Ch 9: ત્રિકોણમિતિના ઉપયોગો", "Ch 10: વર્તુળ", "Ch 11: વર્તુળ સંબંધિત ક્ષેત્રફળ", "Ch 12: પૃષ્ઠફળ અને ઘનફળ", "Ch 13: આંકડાશાસ્ત્ર", "Ch 14: સંભાવના"],
            "ગુજરાતી (Gujarati)": ["Ch 1: મોરલી", "Ch 2: શરણાઈના સૂર", "Ch 3: પ્રયાણ", "Ch 4: જીવન અંજલિ થાજો", "Ch 5: શ્વેત ક્રાંતિના પ્રણેતા", "Ch 6: વાયરલ ઇન્ફેક્શન", "Ch 7: કાળુ અને રાજુ", "Ch 8: દીકરી", "Ch 9: ચોપડાની પીળી મશ", "Ch 10: ડાંગવનો અને..."],
            "સામાજિક વિજ્ઞાન (Social Science)": ["Ch 1: ભારતનો વારસો", "Ch 2: ભારતનો સાંસ્કૃતિક વારસો: પરંપરાઓ", "Ch 3: શિલ્પ અને સ્થાપત્ય", "Ch 4: ભારતનો સાહિત્યિક વારસો", "Ch 5: ભારતનો વિજ્ઞાન અને ટેકનોલોજીનો વારસો", "Ch 6: ભારતના સાંસ્કૃતિક વારસાના સ્થળો", "Ch 7: આપણા વારસાનું જતન", "Ch 8: કુદરતી સંસાધનો", "Ch 9: વન અને વન્યજીવ સંસાધન", "Ch 10: ભારત: કૃષિ", "Ch 15: આર્થિક વિકાસ"],
            "અંગ્રેજી (English)": ["Ch 1: Against the Odds", "Ch 2: The Human Robot", "Ch 3: An Interview with Arun Krishnamurthy", "Ch 4: A Wonderful Creation", "Ch 5: Playing with Fire"]
        },
        "Std 11": {
            "ગણિત (Maths)": ["Ch 1: ગણ (Sets)", "Ch 2: સંબંધ અને વિધેય", "Ch 3: ત્રિકોણમિત્તીય વિધેયો", "Ch 4: ગાણિતિક અનુમાનનો સિદ્ધાંત", "Ch 5: સંકર સંખ્યાઓ"],
            "भૌતિક વિજ્ઞાન (Physics)": ["Ch 1: એકમ અને માપન", "Ch 2: સુરેખ પથ પર ગતિ", "Ch 3: સમતલમાં ગતિ", "Ch 4: ગતિના નિયમો"],
            "રસાયણ વિજ્ઞાન (Chemistry)": ["Ch 1: રસાયણ વિજ્ઞાનની પાયાની વિભાવનાઓ", "Ch 2: પરમાણુનું બંધારણ"]
        },
        "Std 12": {
            "ગણિત (Maths)": ["Ch 1: સંબંધ અને વિધેય", "Ch 2: ત્રિકોણમિત્તીય પ્રતિવિધેયો", "Ch 3: શ્રેણિક (Matrices)", "Ch 4: નિશ્ચાયક"],
            "ભૌતિક વિજ્ઞાન (Physics)": ["Ch 1: વિદ્યુતભારો અને ક્ષેત્રો", "Ch 2: સ્થિર વિદ્યુતસ્થિતિમાન અને કેપેસિટન્સ", "Ch 3: પ્રવાહ વિદ્યુત"],
            "રસાયણ વિજ્ઞાન (Chemistry)": ["Ch 1: દ્રાવણો", "Ch 2: વિદ્યુતરસાયણ", "Ch 3: રાસાયણિક ગતિકી"]
        }
    }

# ================= 🤖 ૧૦૦% પાવરફુલ ડાયનેમિક રેન્ડમ ક્વેશ્ચન મશીન =================
# 🚨 અહીં આપણે સામાજિક વિજ્ઞાન અને વિજ્ઞાન વચ્ચેનો ભેદ એકદમ ક્લિયર કરી દીધો છે!
def get_dynamic_question(ch_name, sub_name, q_index):
    random.seed(q_index + len(ch_name) + int(time.time() * 10) % 1000)
    
    if "ગણિત" in sub_name or "Maths" in sub_name:
        val1 = random.randint(2, 12)
        val2 = random.randint(3, 11)
        correct_ans = str(val1 * val2)
        ops = [correct_ans, str(val1 * val2 + 4), str(val1 * val2 - 3), str(val1 + val2)]
        random.shuffle(ops)
        return {
            "પ્રશ્ન": f"આપેલા ગણિતના પ્રશ્નની ગણતરી કરો: {val1} × {val2} નો સાચો જવાબ નીચેનામાંથી કયો થાય?",
            "વિકલ્પો": ops,
            "સાચો": correct_ans
        }
    elif "સામાજિક વિજ્ઞાન" in sub_name or "Social Science" in sub_name:
        ss_pool = [
            ("ભારતનો ભવ્ય સાંસ્કૃતિક વારસો શાના માટે જાણીતો છે?", ["વિવિધતા અને સમૃદ્ધિ", "માત્ર યુદ્ધો", "ગરીબી"], "વિવિધતા અને સમૃદ્ધિ"),
            ("નીચેનામાંથી કયો પાક ખરીફ પાકનું મુખ્ય ઉદાહરણ છે?", ["ડાંગર (ચોખા)", "ઘઉં", "રાઈ"], "ડાંગર (ચોખા)"),
            ("ભારત દેશ આર્થિક દૃષ્ટિએ કેવો દેશ ગણાય છે?", ["વિકસિત", "વિકાસશીલ", "પછાત"], "વિકાસશીલ"),
            ("તાજમહાલ સ્થાપત્ય કલા કયા મોગલ શાસકે બંધાવ્યો હતો?", ["અકબર", "શાહજહાં", "બાબર"], "શાહજહાં")
        ]
        topic = random.choice(ss_pool)
        return {
            "પ્રશ્ન": f"સામાજિક વિજ્ઞાનના અભ્યાસક્રમ મુજબ, {topic[0]}",
            "વિકલ્પો": topic[1],
            "સાચો": topic[2]
        }
    elif "વિજ્ઞાન" in sub_name or "Science" in sub_name:
        sci_pool = [
            ("એસિડ સ્વાદે કેવા હોય છે?", ["ખાટા", "તૂરા", "કડવા"], "ખાટા"),
            ("ભૂરા લિટમસ પત્રને લાલ કોણ બનાવે છે?", ["એસિડ", "બેઇઝ", "ક્ષાર"], "એસિડ"),
            ("પાણીનું રાસાયણિક સૂત્ર નીચેનામાંથી કયું છે?", ["H2O", "CO2", "O2"], "H2O"),
            ("શૂન્યાવકાશમાં પ્રકાશનો વેગ કેટલો હોય છે?", ["૩×૧૦⁸ મીટર/સેકંડ", "૩×૧૦⁶ મીટર/સેકંડ", "૩×૧૦⁵ મીટર/સેકંડ"], "૩×૧૦⁸ મીટર/સેકંડ")
        ]
        topic = random.choice(sci_pool)
        return {
            "પ્રશ્ન": f"વિજ્ઞાન (Science) પ્રકરણ મુજબ, {topic[0]}",
            "વિકલ્પો": topic[1],
            "સાચો": topic[2]
        }
    else:
        # ગુજરાતી અને અંગ્રેજી ભાષાઓ માટે
        return {
            "પ્રશ્ન": f"આ પાઠ્યપુસ્તકના આપેલા વિકલ્પોમાંથી સાહિત્યિક દ્રષ્ટિએ કયો ઉત્તર સાચો છે?",
            "વિકલ્પો": ["સાચો વિકલ્પ", "ખોટું વિધાન", "માહિતી અધૂરી છે", "કહી શકાય નહીં"],
            "સાચો": "साચો વિકલ્પ"
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

    # 🚨 અહીં આપણે વિષયનું નામ (sub_name) પણ પાસ કર્યું છે જેથી સાચો ડેટા લોડ થાય
    q = get_dynamic_question(પ્રકરણ, વિષય, st.session_state.question_index)

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
                    st.error(f"ખોટો જવાબ ❌ (-5)")
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
