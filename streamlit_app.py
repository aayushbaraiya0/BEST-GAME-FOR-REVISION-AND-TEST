import streamlit as st
import random

# ==========================================
# પેજ સેટિંગ
# ==========================================

st.set_page_config(
    page_title="ગુજરાતી એક્ઝામ ગેમ",
    page_icon="🎮",
    layout="wide"
)

# ==========================================
# અવાજ
# ==========================================

def અવાજ(url):
    st.markdown(
        f"""
        <audio autoplay>
        <source src="{url}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#14002e,#240046,#3c096c,#5a189a);
}

/* Main Box */
.main-box{
    background:#05010f;
    border:2px solid cyan;
    border-radius:25px;
    padding:25px;
    box-shadow:0px 0px 20px cyan;
    margin-bottom:20px;
}

/* Title */
.title{
    text-align:center;
    color:white;
    font-size:60px;
    font-weight:bold;
    text-shadow:0px 0px 20px cyan;
}

/* Setup Box */
.setup-box{
    background:#0b1020;
    border:2px solid cyan;
    border-radius:20px;
    padding:20px;
    margin-top:20px;
    box-shadow:0px 0px 15px cyan;
}

/* Question */
.question-box{
    background:#0d1325;
    border:2px solid #38bdf8;
    border-radius:20px;
    padding:25px;
    margin-top:20px;
    box-shadow:0px 0px 15px #06b6d4;
}

/* Text */
.white{
    color:white;
}

/* Head */
.head{
    color:cyan;
    font-size:28px;
    font-weight:bold;
}

/* Score */
.score{
    color:#22c55e;
    font-size:40px;
    font-weight:bold;
}

/* Buttons */
.stButton button{
    width:100%;
    background:linear-gradient(90deg,#06b6d4,#2563eb);
    color:white;
    border:none;
    border-radius:15px;
    padding:14px;
    font-size:20px;
    font-weight:bold;
}

.stButton button:hover{
    transform:scale(1.02);
    box-shadow:0px 0px 15px cyan;
}

/* Radio */
.stRadio label{
    color:white !important;
    font-size:20px !important;
}

/* Select */
.stSelectbox label{
    color:white !important;
    font-size:18px !important;
}

/* Input */
.stTextInput label{
    color:white !important;
    font-size:18px !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# બધા પ્રશ્નો
# ==========================================

questions = {

"ધોરણ ૧૦": {

"ગણિત": {

"વાસ્તવિક સંખ્યાઓ": [

{
"question":"૨ અને ૫ સિવાય અન્ય અવયવ ધરાવતી હરવાળી સંખ્યા કેવી દશાંશ આપે?",
"options":["અસીમ આવર્ત દશાંશ","સીમિત દશાંશ","પૂર્ણાંક","પ્રાકૃતિક સંખ્યા"],
"answer":"અસીમ આવર્ત દશાંશ"
},

{
"question":"યુક્લિડ વિભાગ અલ્ગોરિધમ કયા માટે ઉપયોગી છે?",
"options":["મહત્તમ સામાન્ય અવયવ","લઘુત્તમ સામાન્ય ગુણાક","ઘાતાંક","વિસ્તાર"],
"answer":"મહત્તમ સામાન્ય અવયવ"
},

{
"question":"HCF નો સંપૂર્ણ અર્થ શું છે?",
"options":["મહત્તમ સામાન્ય અવયવ","લઘુત્તમ સામાન્ય ગુણાક","ઘનમૂલ","ભાગાકાર"],
"answer":"મહત્તમ સામાન્ય અવયવ"
}

],

"ત્રિકોણમિતિ": [

{
"question":"sin²θ + cos²θ નું મૂલ્ય શું છે?",
"options":["૧","૦","૨","અનંત"],
"answer":"૧"
},

{
"question":"tanθ = ?",
"options":["sinθ/cosθ","cosθ/sinθ","૧","૦"],
"answer":"sinθ/cosθ"
},

{
"question":"૩૦° નો sin કેટલો?",
"options":["૧/૨","૧","૦","√૩"],
"answer":"૧/૨"
}

],

"વૃત્ત": [

{
"question":"વૃત્તની ત્રિજ્યા ૭ હોય તો વ્યાસ કેટલો?",
"options":["૭","૧૪","૨૧","૨૮"],
"answer":"૧૪"
},

{
"question":"વૃત્તનો વ્યાસ ત્રિજ્યાનો કેટલો ગણો હોય છે?",
"options":["૨","૩","૪","૧"],
"answer":"૨"
}

]

},

"વિજ્ઞાન": {

"વિદ્યુત": [

{
"question":"ઓહમનો નિયમ કોના સંબંધને દર્શાવે છે?",
"options":["વિભવાંતર અને વિદ્યુત પ્રવાહ","ભાર અને ગતિ","દબાણ અને ઘનફળ","તાપ અને ઊર્જા"],
"answer":"વિભવાંતર અને વિદ્યુત પ્રવાહ"
},

{
"question":"વિદ્યુત પ્રવાહનું એકમ શું છે?",
"options":["એમ્પિયર","વોલ્ટ","વોટ","જૂલ"],
"answer":"એમ્પિયર"
},

{
"question":"વિદ્યુત શક્તિનું એકમ શું છે?",
"options":["વોટ","એમ્પિયર","ઓહમ","વોલ્ટ"],
"answer":"વોટ"
}

],

"પ્રકાશ": [

{
"question":"અવતલ દર્પણ ક્યાં ઉપયોગી છે?",
"options":["વાહનના હેડલાઇટમાં","ઘડિયાળમાં","પંખામાં","દરવાજામાં"],
"answer":"વાહનના હેડલાઇટમાં"
},

{
"question":"પ્રકાશની ગતિ કેટલી છે?",
"options":["૩×૧૦⁸ મીટર/સેકન્ડ","૩×૧૦⁶","૩×૧૦⁴","૩×૧૦²"],
"answer":"૩×૧૦⁸ મીટર/સેકન્ડ"
}

]

},

"સામાજિક વિજ્ઞાન": {

"રાષ્ટ્રીય આંદોલન": [

{
"question":"દાંડી કૂચ કોણે શરૂ કરી હતી?",
"options":["મહાત્મા ગાંધી","સરદાર પટેલ","જવાહરલાલ નેહરુ","સુભાષચંદ્ર બોઝ"],
"answer":"મહાત્મા ગાંધી"
},

{
"question":"ભારત છોડો આંદોલન ક્યારે થયું?",
"options":["૧૯૪૨","૧૯૪૭","૧૯૩૦","૧૯૨૦"],
"answer":"૧૯૪૨"
}

]

}

},

"ધોરણ ૯": {

"ગણિત": {

"રેખાઓ અને ખૂણાઓ": [

{
"question":"સામસામેના ખૂણાઓને શું કહે છે?",
"options":["વિપરીત ખૂણાઓ","પૂરક ખૂણાઓ","લઘુ ખૂણાઓ","સમકોણ"],
"answer":"વિપરીત ખૂણાઓ"
},

{
"question":"સમકોણ કેટલા અંશનો હોય છે?",
"options":["૯૦","૪૫","૧૮૦","૩૬૦"],
"answer":"૯૦"
}

]

},

"વિજ્ઞાન": {

"પદાર્થ": [

{
"question":"ઘન પદાર્થમાં કણો કેવી સ્થિતિમાં હોય છે?",
"options":["ઘનિષ્ઠ રીતે ગોઠવાયેલા","દૂર દૂર","અવ્યવસ્થિત","પ્રવાહી"],
"answer":"ઘનિષ્ઠ રીતે ગોઠવાયેલા"
},

{
"question":"પાણી કઈ અવસ્થામાં મળે છે?",
"options":["ત્રણે અવસ્થામાં","માત્ર ઘન","માત્ર વાયુ","માત્ર પ્રવાહી"],
"answer":"ત્રણે અવસ્થામાં"
}

]

}

}

}

# ==========================================
# સેશન
# ==========================================

if "score" not in st.session_state:
    st.session_state.score = 0

# ==========================================
# મુખ્ય શીર્ષક
# ==========================================

st.markdown("""
<div class="main-box">
<div class="title">
🎮 ગુજરાતી એક્ઝામ ગેમ 🎮
</div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# ગેમ સેટઅપ
# ==========================================

st.markdown("""
<div class="setup-box">
<div class="head">
⚙️ ગેમ સેટઅપ
</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    name = st.text_input("તમારું નામ")

with col2:
    std = st.selectbox(
        "ધોરણ પસંદ કરો",
        list(questions.keys())
    )

with col3:
    subject = st.selectbox(
        "વિષય પસંદ કરો",
        list(questions[std].keys())
    )

with col4:
    chapter = st.selectbox(
        "પ્રકરણ પસંદ કરો",
        list(questions[std][subject].keys())
    )

# ==========================================
# પ્રશ્ન
# ==========================================

question_data = random.choice(
    questions[std][subject][chapter]
)

question = question_data["question"]
options = question_data["options"]
answer = question_data["answer"]

# ==========================================
# પ્રશ્ન UI
# ==========================================

left,right = st.columns([3,1])

with left:

    st.markdown(f"""
    <div class="question-box">

    <div class="head">
    📘 પ્રકરણ : {chapter}
    </div>

    <br>

    <h2 class="white">
    {question}
    </h2>

    </div>
    """, unsafe_allow_html=True)

    selected = st.radio(
        "જવાબ પસંદ કરો",
        options
    )

    c1,c2 = st.columns(2)

    with c1:

        if st.button("✅ જવાબ સબમિટ કરો"):

            if selected == answer:

                st.session_state.score += 1

                અવાજ("https://www.soundjay.com/buttons/sounds/button-09.mp3")

                st.success("સાચો જવાબ 🎉")

                st.balloons()

            else:

                અવાજ("https://www.soundjay.com/buttons/sounds/button-10.mp3")

                st.error(f"ખોટો જવાબ ❌ સાચો જવાબ : {answer}")

    with c2:

        if st.button("🔄 નવો પ્રશ્ન"):

            અવાજ("https://www.soundjay.com/buttons/sounds/button-3.mp3")

            st.rerun()

with right:

    st.markdown(f"""
    <div class="main-box">

    <div class="head">
    🏆 સ્કોર
    </div>

    <br>

    <div class="score">
    {st.session_state.score}
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="main-box">

    <div class="head">
    📚 અભ્યાસ
    </div>

    <br>

    <p style='color:white;font-size:18px;'>
    રોજ પ્રશ્નો ઉકેલો અને પરીક્ષામાં વધુ ગુણ મેળવો.
    </p>

    </div>
    """, unsafe_allow_html=True)
