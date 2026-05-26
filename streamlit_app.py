import streamlit as st
import random

# layout="centered" કરવાથી આખી ગેમ સ્ક્રીનની વચ્ચે એકદમ નાની અને સ્લિમ થઈ જશે
st.set_page_config(page_title="Best Game for Revision and Test", page_icon="🎮", layout="centered")

# શાનદાર પ્યોર RGB અને સુપર સ્લિમ ગેમિંગ થીમ
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(124deg, #ff2400, #e81d1d, #e8b71d, #1de840, #1ddde8, #2b1de8, #dd00ff, #dd00ff);
        background-size: 1600% 1600%;
        animation: RGB-Animation 14s ease infinite;
    }
    @keyframes RGB-Animation {
        0%{background-position:0% 82%}
        50%{background-position:100% 19%}
        100%{background-position:0% 82%}
    }
    /* ગેમ લોબીના બધા મુખ્ય બોક્સને સ્લિમ કરવા માટે */
    .stRadio, .stMarkdown, .stSelectbox, .stTextInput {
        background-color: rgba(10, 10, 15, 0.94) !important;
        padding: 12px 16px !important;
        border-radius: 10px !important;
        color: #ffffff !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
        border: 1px solid #00ffff !important;
        margin-bottom: 8px !important;
    }
    label[data-testid="stWidgetLabel"], div[data-testid="stRadio"] label, p, span {
        color: #ffffff !important;
        font-size: 14px !important;
    }
    h1 {
        color: #00ffff !important;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.6);
        text-align: center;
        font-size: 24px !important;
        margin-bottom: 15px !important;
    }
    h2, h3 {
        color: #00ffff !important;
        font-size: 18px !important;
    }
    /* નામ લખવાના બોક્સનો ટેક્સ્ટ કલર ડાર્ક કાળો */
    input { 
        color: #000000 !important; 
        font-weight: bold !important;
        height: 35px !important;
    }
    /* સ્ટાર્ટ ગેમ બટનની શાનદાર ગેમિંગ સ્ટાઇલ */
    .stButton>button {
        background-color: rgba(10, 10, 15, 0.95) !important;
        color: #00ffff !important;
        border: 1px solid #00ffff !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #00ffff !important;
        color: #000000 !important;
        box-shadow: 0 0 15px #00ffff;
    }
    
    /* વચ્ચેથી નકામો કાળો પટ્ટો હટાવવાની ટ્રીક */
    div[data-testid="stVerticalBlock"] > div:empty {
        display: none !important;
    }
    
    /* ચાણક્ય AI બોક્સનું સ્ટાઇલિંગ */
    .ai-sidebar-box {
        background-color: rgba(15, 25, 35, 0.98) !important;
        border: 2px dashed #00ffff !important;
        padding: 12px;
        border-radius: 8px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 🎮 ઓફિશિયલ ગેમ ટાઇટલ હેડર
st.markdown("<h1>🎮 BEST GAME FOR REVISION AND TEST</h1>", unsafe_allow_html=True)

# 📚 ધોરણ ૧ થી ૧૨ નો સાચો પ્રકરણો (Chapters) વાળો અસલી ડેટાબેઝ
if "base_db" not in st.session_state:
    st.session_state.base_db = {
        "Std 1": {
            "ગણિત ગમ્મત": ["Ch 1: આકારો અને જગ્યા", "Ch 2: ૧ થી ૯ સુધીની સંખ્યા"],
            "ગુજરાતી (કલરવ)": ["Ch 1: શાળા તત્પરતા ૧", "Ch 2: ચક્કીબેન ચક્કીબેન"]
        },
        "Std 6": {
            "વિજ્ઞાન (Science)": ["Ch 1: ખોરાક ક્યાંથી મળે છે?", "Ch 2: આહારના ઘટકો"],
            "ગણિત (Maths)": ["Ch 1: આપણી સંખ્યાઓને જાણવી", "Ch 2: પૂર્ણ સંખ્યાઓ"],
            "ગુજરાતી": ["Ch 1: રેલવે સ્ટેશન", "Ch 2: હિંદ માતાને સંબોધન"]
        },
        "Std 9": {
            "વિજ્ઞાન (Science)": ["Ch 1: આપણી આસપાસમાં દ્રવ્ય", "Ch 2: શું આપણી આસપાસના દ્રવ્યો શુદ્ધ છે?"],
            "ગણિત (Maths)": ["Ch 1: સંખ્યા પદ્ધતિ", "Ch 2: બહુપદીઓ"]
        },
        "Std 10": {
            "વિજ્ઞાન (Science)": [
                "Ch 1: રાસાયણિક પ્રક્રિયાઓ અને સમીકરણો", 
                "Ch 2: એસિડ, બેઇઝ અને ક્ષાર", 
                "Ch 6: જૈવિક ક્રિયાઓ",
                "Ch 10: પ્રકાશ-પરાવર્તન અને વક્રીભવન"
            ],
            "ગણિત (Maths)": [
                "Ch 1: વાસ્તવિક સંખ્યાઓ", 
                "Ch 2: બહુપદીઓ", 
                "Ch 5: સમાંતર શ્રેણી",
                "Ch 14: આંકડાશાસ્ત્ર"
            ],
            "ગુજરાતી (Gujarati)": ["Ch 1: મોરલી", "Ch 2: શરણાઈના સૂર", "Ch 4: જીવન અંજલિ થાજો"],
            "અંગ્રેજી (English)": ["Ch 1: Against the Odds", "Ch 2: The Human Robot"]
        },
        "Std 11": {"ગણિત": ["Ch 1: ગણ"], "भૌતિક વિજ્ઞાન": ["Ch 1: એકમ અને માપન"]},
        "Std 12": {"ગણિત": ["Ch 1: સંબંધ અને વિધેય"], "ભૌતિક વિજ્ઞાન": ["Ch 1: વિદ્યુતભારો અને ક્ષેત્રો"]}
    }

# 📝 ધોરણ ૧૦ ના સાચા બોર્ડ લેવલના પ્રશ્નો (PYQ)
if "real_questions" not in st.session_state:
    st.session_state.real_questions = {
        "Ch 1: રાસાયણિક પ્રક્રિયાઓ અને સમીકરણો": [
            {"question": "મેગ્નેશિયમ પટ્ટીને હવામાં સળગાવતા પહેલાં શા માટે સાફ કરવામાં આવે છે? (PYQ)", "options": ["ભેજ દૂર કરવા", "નિષ્ક્રિય મેગ્નેશિયમ ઓક્સાઇડનું સ્તર દૂર કરવા", "ચળકાટ માટે", "કાર્બોનેટ સ્તર દૂર કરવા"], "answer": "નિષ્ક્રિય મેગ્નેશિયમ ઓક્સાઇડનું સ્તર દૂર કરવા"},
            {"question": "કળી ચૂનાનું (Calcium Oxide) પાણી સાથે ભળવું એ કઈ પ્રક્રિયા છે? (PYQ)", "options": ["ઉષ્માશોષક", "ઉષ્માક્ષેપક", "વિઘટન", "દ્વિ-વિસ્થાપન"], "answer": "ઉષ્માક્ષેપક"}
        ],
        "Ch 2: એસિડ, બેઇઝ અને ક્ષાર": [
            {"question": "કોઈ દ્રાવણ લાલ લિટમસ પત્રને ભૂરું બનાવે છે, તો તેની pH કેટલી હોઈ શકે? (PYQ)", "options": ["1", "4", "5", "10"], "answer": "10"},
            {"question": "પ્લાસ્ટર ઓફ પેરિસ (POP) નું સાચું રાસાયણિક સૂત્ર કયું છે?", "options": ["CaSO₄ · 2H₂O", "CaSO₄ · ½H₂O", "CuSO₄ · 5H₂O"], "answer": "CaSO₄ · ½H₂O"}
        ],
        "Ch 2: બહુપદીઓ": [
            {"question": "દ્વિઘાત બહુપદી x² + 7x + 10 ના શૂન્યોનો સરવાળો કેટલો થાય? (PYQ)", "options": ["7", "-7", "10", "-10"], "answer": "-7"}
        ],
        "Ch 1: વાસ્તવિક સંખ્યાઓ": [
            {"question": "યુક્લિડની ભાગવિધિ મુજબ ગુ.સા.અ. શોધવાનું સૂત્ર કયું છે?", "options": ["a = bq + r", "a = b + q", "pv = nrt"], "answer": "a = bq + r"}
        ],
        "Ch 1: મોરલી": [
            {"question": "'મોરલી' પદના કવયિત્રીનું નામ શું છે?", "options": ["મીરાંબાઈ", "ગંગાસતી", "પ્રેમાનંદ"], "answer": "મીરાંબાઈ"}
        ],
        "Ch 1: Against the Odds": [
            {"question": "For how many years did the residents of Taj Nagar lobbied for a railway station?", "options": ["11 years", "25 years", "21 years"], "answer": "21 years"}
        ]
    }

def generate_infinite_question(chapter_name):
    if "ગણિત" in chapter_name or "બહુપદીઓ" in chapter_name or "સંખ્યાઓ" in chapter_name:
        a = random.randint(2, 9)
        b = random.randint(2, 10)
        return {
            "question": f"[MATH CHALLENGE] {chapter_name} મુજબ, {a} ગુણ્યા {b} નો સાચો જવાબ શું થાય?",
            "options": [str(a*b), str(a*b+4), str(a*b-2), str(a+b)],
            "answer": str(a*b)
        }
    else:
        return {
            "question": f"[REVISION RUN] {chapter_name} ના આ મહત્વના પ્રશ્ન માટે કયો વિકલ્પ સાચો છે?",
            "options": ["સાચું વિધાન", "ખોટું વિધાન", "માહિતી અધૂરી છે"],
            "answer": "સાચું વિધાન"
        }

# સેશન સ્ટેટ્સ સેટઅપ
if "player_name" not in st.session_state: st.session_state.player_name = "Aayush"
if "score" not in st.session_state: st.session_state.score = 100
if "current_match_questions" not in st.session_state: st.session_state.current_match_questions = []
if "match_index" not in st.session_state: st.session_state.match_index = 0
if "game_mode" not in st.session_state: st.session_state.game_mode = "SETUP"
if "ai_open" not in st.session_state: st.session_state.ai_open = False

# 🕹️ મેઈન ગેમ કન્ટેન્ટ
if st.session_state.game_mode == "SETUP":
    st.subheader("⚙️ ગેમ સેટઅપ લોબી")
    
    name_input = st.text_input("✍️ તમારું નામ લખો:", value=st.session_state.player_name)
    if name_input:
        st.session_state.player_name = name_input.strip()
        
    std_list = list(st.session_state.base_db.keys())
    selected_std = st.selectbox("🎯 ધોરણ પસંદ કરો (Std 1 to 12):", std_list, index=std_list.index("Std 10") if "Std 10" in std_list else 0)
    
    sub_list = list(st.session_state.base_db[selected_std].keys())
    selected_sub = st.selectbox("📚 વિષય (Subjects) પસંદ કરો:", sub_list)
    
    ch_list = st.session_state.base_db[selected_std][selected_sub]
    selected_ch = st.selectbox("📖 પ્રકરણ (Chapters) પસંદ કરો:", ch_list)
    
    quiz_limit = st.selectbox("📊 આ મેચમાં કેટલા પ્રશ્નો રમવા છે?", [10, 20, 50, 100])
    
    if st.button(f"🎮 ગેમ સ્ટાર્ટ કરો, {st.session_state.player_name}!"):
        final_set = []
        if selected_ch in st.session_state.real_questions:
            final_set = list(st.session_state.real_questions[selected_ch])
            random.shuffle(final_set)
        
        while len(final_set) < quiz_limit:
            new_q = generate_infinite_question(selected_ch)
            if new_q["question"] not in [q["question"] for q in final_set]: final_set.append(new_q)
        
        st.session_state.current_match_questions = final_set[:quiz_limit]
        st.session_state.match_index = 0
        st.session_state.score = 100
        st.session_state.game_mode = "PLAYING"
        st.rerun()

elif st.session_state.game_mode == "PLAYING":
    st.subheader(f"🕹️ બેટલ ગ્રાઉન્ડ - {st.session_state.player_name}")
    
    if st.session_state.score <= 0:
        st.error(f"💥 GAME OVER {st.session_state.player_name}! તમારા પોઈન્ટ્સ 0 થઈ ગયા.")
        if st.button("🔄 લોબીમાં પાછા ફરો", key="lobby_back_btn"):
            st.session_state.game_mode = "SETUP"
            st.session_state.score = 100
            st.session_state.match_index = 0
            st.session_state.current_match_questions = []
            st.rerun()
    else:
        idx = st.session_state.match_index
        total_q = len(st.session_state.current_match_questions)
        if idx < total_q:
            current_q = st.session_state.current_match_questions[idx]
            st.markdown(f"#### 🎯 સ્કોર: <span style='color:#00ffff'>{st.session_state.score}</span>")
            st.write(f"📊 પ્રશ્ન પ્રોગ્રેસ: **{idx + 1} / {total_q}**")
            st.subheader(current_q["question"])
            
            user_choice = st.radio("સાચો વિકલ્પ પસંદ કરો:", current_q["options"], index=None, key=f"inf_q_{idx}")
            if user_choice is not None:
                if user_choice == current_q["answer"]:
                    st.session_state.score += 10
                    st.toast(f"🎯 જોરદાર જવાબ! +10", icon="✅")
                    st.session_state.match_index += 1
                else:
                    st.session_state.score -= 50
                st.rerun()
        else:
            st.balloons()
            st.success(f"🎉 વિજેતા {st.session_state.player_name}! તમે આખી ચેલેન્જ પાર કરી લીધી!")
            if st.button("🏁 નવો રેકોર્ડ સેટ કરો", key="reset_match_btn"):
                st.session_state.game_mode = "SETUP"
                st.rerun()

# 🧠 --- ચાણક્ય AI બટન અને પોપઅપ જે રાઇટ સાઇડ સેટ થઈ ગયું છે ---
st.write("---")
col_space, col_btn = st.columns([2.8, 1.2])

with col_btn:
    if st.button("🧠 ચાણક્ય AI ઓપન / ક્લોઝ", key="chanakya_fixed_btn"):
        st.session_state.ai_open = not st.session_state.ai_open
        st.rerun()

if st.session_state.ai_open:
    st.markdown("<div class='ai-popup-box'>", unsafe_allow_html=True)
    st.subheader("🧠 ચાણક્ય AI")
    if "study_chat_history" not in st.session_state: st.session_state.study_chat_history = []
    if not st.session_state.study_chat_history:
        st.session_state.study_chat_history.append({"role": "assistant", "message": f"પ્રણામ {st.session_state.player_name} ભાઈ! હું ચાણક્ય AI છું. ભણવાનો કોઈ પણ પ્રશ્ન અહીં પૂછો!"})
    for chat in st.session_state.study_chat_history:
        with st.chat_message(chat["role"]): st.write(chat["message"])
    if study_msg := st.chat_input("અહીં સવાલ પૂછો..."):
        st.session_state.study_chat_history.append({"role": "user", "message": study_msg})
        reply = f"ખૂબ જ ઉત્તમ પ્રશ્ન {st.session_state.player_name} ભાઈ! હું આ વિષયને પાકો કરવામાં તમારી પૂરી મદદ કરીશ."
        st.session_state.study_chat_history.append({"role": "assistant", "message": reply})
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
