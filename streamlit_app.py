import streamlit as st
import random

# પેજ સેટઅપ અને ઓફિશિયલ ટાઇટલ
st.set_page_config(page_title="Best Game for Revision and Test", page_icon="🎮", layout="wide")

# શાનદાર પ્યોર RGB અને ડાર્ક નિયોન ગેમિંગ થીમ
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
    div[data-testid="stColumn"], .stRadio, .stMarkdown, .stButton>button, .stSelectbox, .stTextInput {
        background-color: rgba(10, 10, 15, 0.94) !important;
        padding: 18px !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.8);
        border: 1px solid #00ffff !important;
    }
    label[data-testid="stWidgetLabel"], div[data-testid="stRadio"] label, p, span {
        color: #ffffff !important;
    }
    h1, h2, h3 {
        color: #00ffff !important;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.6);
        text-align: center;
    }
    /* નામ બોક્સનો ટેક્સ્ટ કલર ડાર્ક કાળો */
    input { 
        color: #000000 !important; 
        font-weight: bold !important;
    }
    .ai-popup-box {
        background-color: rgba(15, 25, 35, 0.98) !important;
        border: 2px dashed #00ffff !important;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 🎮 ઓફિશિયલ ગેમ ટાઇટલ હેડર
st.markdown("<h1>🎮 BEST GAME FOR REVISION AND TEST</h1>", unsafe_allow_html=True)

# 📚 તમામ ધોરણ અને ભાષાઓનો ડેટાબેઝ
if "base_db" not in st.session_state:
    st.session_state.base_db = {
        "Std 1": ["ગણિત ગમ્મત", "ગુજરાતી (કલરવ)", "અંગ્રેજી (English)"],
        "Std 2": ["ગણિત ગમ્મત", "ગુજરાતી (હલ્લોલ)", "અંગ્રેજી (English)"],
        "Std 3": ["ગણિત", "ગુજરાતી (મયુર)", "આસપાસ (પર્યાવરણ)", "અંગ્રેજી (English)"],
        "Std 4": ["ગણિત", "ગુજરાતી", "આસપાસ (પર્યાવરણ)", "અંગ્રેજી (English)"],
        "Std 5": ["ગણિત", "ગુજરાતી (કેકારવ)", "સૌની આસપાસ", "અંગ્રેજી (English)", "હિન્દી"],
        "Std 6": ["ગણિત (Maths)", "વિજ્ઞાન (Science)", "સામાજિક વિજ્ઞાન", "ગુજરાતી (Gujarati)", "અંગ્રેજી (English)", "हिन्दी", "સંસ્કૃત"],
        "Std 7": ["ગણિત (Maths)", "વિજ્ઞાન (Science)", "સામાજિક વિજ્ઞાન", "ગુજરાતી (Gujarati)", "અંગ્રેજી (English)", "हिन्दी", "સંસ્કૃત"],
        "Std 8": ["ગણિત (Maths)", "વિજ્ઞાન (Science)", "સામાજિક વિજ્ઞાન", "ગુજરાતી (Gujarati)", "અંગ્રેજી (English)", "हिन्दी", "સંસ્કૃત"],
        "Std 9": ["ગણિત (Maths)", "વિજ્ઞાન (Science)", "સામાજિક વિજ્ઞાન", "ગુજરાતી (Gujarati)", "અંગ્રેજી (English)", "हिन्दी", "સંસ્કૃત"],
        "Std 10": ["વિજ્ઞાન (Science)", "ગણિત (Maths)", "સામાજિક વિજ્ઞાન", "ગુજરાતી (Gujarati)", "અંગ્રેજી (English)", "हिन्दी", "સંસ્કૃત"],
        "Std 11": ["ગણિત (Maths)", "ભૌતિક વિજ્ઞાન", "રસાયણ વિજ્ઞાન", "જીવ વિજ્ઞાન", "ગુજરાતી (Gujarati)", "અંગ્રેજી (English)", "એકાઉન્ટ", "સ્ટેટ્સ"],
        "Std 12": ["ગણિત (Maths)", "ભૌતિક વિજ્ઞાન", "રસાયણ વિજ્ઞાન", "જીવ વિજ્ઞાન", "ગુજરાતી (Gujarati)", "અંગ્રેજી (English)", "એકાઉન્ટ", "સ્ટેટ્સ"]
    }

if "real_questions" not in st.session_state:
    st.session_state.real_questions = {
        "વિજ્ઞાન (Science)": [
            {"question": "મેગ્નેશિયમ પટ્ટીને હવામાં સળગાવતા પહેલાં શા માટે સાફ કરવામાં આવે છે? (PYQ)", "options": ["ભેજ દૂર કરવા", "નિષ્ક્રિય મેગ્નેશિયમ ઓક્સાઇડનું સ્તર દૂર કરવા", "ચળકાટ માટે", "કાર્બોનેટ સ્તર દૂર કરવા"], "answer": "નિષ્ક્રિય મેગ્નેશિયમ ઓક્સાઇડનું સ્તર દૂર કરવા"},
            {"question": "કળી ચૂનાનું (Calcium Oxide) પાણી સાથે ભળવું એ કઈ પ્રક્રિયા છે? (PYQ)", "options": ["ઉષ્માશોષક", "ઉષ્માક્ષેપક", "વિઘટન", "દ્વિ-વિસ્થાપન"], "answer": "ઉષ્માક્ષેપક"},
            {"question": "કોઈ દ્રાવણ લાલ લિટમસ પત્રને ભૂરું બનાવે છે, તો તેની pH કેટલી હોઈ શકે? (PYQ)", "options": ["1", "4", "5", "10"], "answer": "10"}
        ],
        "ગણિત (Maths)": [
            {"question": "દ્વિઘાત બહુપદી x² + 7x + 10 ના શૂન્યોનો સરવાળો કેટલો થાય? (PYQ)", "options": ["7", "-7", "10", "-10"], "answer": "-7"}
        ],
        "ગુજરાતી (Gujarati)": [
            {"question": "નીચેનામાંથી કઈ જોડણી સાચી છે?", "options": ["પરિક્ષા", "પરીક્ષા", "પ્રિક્ષા", "પરિડ્શા"], "answer": "પરીક્ષા"},
            {"question": "‘પર્વત’ શબ્દનો સાચો સમાનર્થી શબ્દ કયો થાય?", "options": ["નદી", "ગીરી", "સાગર", "આકાશ"], "answer": "ગીરી"}
        ],
        "અંગ્રેજી (English)": [
            {"question": "Identify the correct plural form of 'Child':", "options": ["Childs", "Childrens", "Children", "Childes"], "answer": "Children"},
            {"question": "Fill in the blank: Honesty is ______ best policy.", "options": ["a", "an", "the", "no article"], "answer": "the"}
        ]
    }

def generate_infinite_question(subject):
    if "ગુજરાતી" in subject or "Gujarati" in subject:
        words = [("સૂર્ય", "ભાનુ"), ("રાત", "નિશા"), ("આકાશ", "ગગન"), ("પાણી", "જળ")]
        w = random.choice(words)
        return {
            "question": f"[GUJARATI CHALLENGE] ‘{w[0]}’ શબ્દનો સાચો સમાનાર્થી શબ્દ ઓળખો:",
            "options": [w[1], "પાતાળ", "ધરતી", "વાયુ"],
            "answer": w[1]
        }
    elif "અંગ્રેજી" in subject or "English" in subject:
        verbs = [("Go", "Went"), ("Eat", "Ate"), ("Play", "Played"), ("See", "Saw")]
        v = random.choice(verbs)
        return {
            "question": f"[ENGLISH GRAMMAR] What is the past tense form of the verb '{v[0]}'? ",
            "options": [v[1], v[0]+"ing", v[0]+"s", "goed"],
            "answer": v[1]
        }
    elif "ગણિત" in subject or "Maths" in subject:
        a = random.randint(2, 9)
        b = random.randint(2, 12)
        return {
            "question": f"[MATH FLASH RUN] {a} × {b} નો સાચો જવાબ શું થાય?",
            "options": [str(a*b), str(a*b+3), str(a*b-2), str(a+b)],
            "answer": str(a*b)
        }
    else:
        return {
            "question": f"[GENERAL REVISION] {subject} વિષયના આ મહત્વના ટોપિક માટે નીચેનામાંથી કયો વિકલ્પ સૌથી સાચો છે?",
            "options": ["સાચો વિકલ્પ", "ખોટો વિકલ્પ", "અસ્પષ્ટ વિધાન", "કહી શકાય નહીં"],
            "answer": "સાચો વિકલ્પ"
        }

# સેશન સ્ટેટ્સ સેટઅપ
if "player_name" not in st.session_state: st.session_state.player_name = "Jasharaj"
if "score" not in st.session_state: st.session_state.score = 100
if "current_match_questions" not in st.session_state: st.session_state.current_match_questions = []
if "match_index" not in st.session_state: st.session_state.match_index = 0
if "game_mode" not in st.session_state: st.session_state.game_mode = "SETUP"
if "ai_open" not in st.session_state: st.session_state.ai_open = False

# લેઆઉટ: ડાબી બાજુ ગેમ સેટઅપ, જમણી બાજુ ચાણક્ય AI આઇકોન અને બટન
col_game, col_ai = st.columns([1.5, 1])

with col_ai:
    # 🎯 હેલ્પ સેન્ટર અહીથી રીમુવ કર્યું છે. માત્ર ચાણક્યજીનો નાનો ગોળ આઇકોન અને બટન રાખ્યું છે.
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/color/96/avatar.png", width=70) # સ્લિમ અને નાનો પ્રીમિયમ આઇકોન
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("🧠 ચાણક્ય AI ખોલો / બંધ કરો"):
        st.session_state.ai_open = not st.session_state.ai_open
        st.rerun()
        
    if st.session_state.ai_open:
        st.markdown("<div class='ai-popup-box'>", unsafe_allow_html=True)
        st.subheader("🧠 ચાણક્ય AI")
        if "study_chat_history" not in st.session_state: st.session_state.study_chat_history = []
        if not st.session_state.study_chat_history:
            st.session_state.study_chat_history.append({"role": "assistant", "message": f"પ્રણામ {st.session_state.player_name} ભાઈ! હું ચાણક્ય AI છું. શિક્ષણ કે રિવિઝનનો કોઈ પણ મૂંઝવતો પ્રશ્ન અહીં પૂછો!"})
        for chat in st.session_state.study_chat_history:
            with st.chat_message(chat["role"]): st.write(chat["message"])
        if study_msg := st.chat_input("અહીં સવાલ પૂછો..."):
            st.session_state.study_chat_history.append({"role": "user", "message": study_msg})
            reply = f"ખૂબ જ ઉત્તમ જિજ્ઞાસા {st.session_state.player_name} ભાઈ! નીતિશાસ્ત્ર અને બોર્ડના વિષયોમાં હું તમને વિજેતા બનાવીશ!"
            st.session_state.study_chat_history.append({"role": "assistant", "message": reply})
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

with col_game:
    if st.session_state.game_mode == "SETUP":
        st.header("⚙️ ગેમ સેટઅપ લોબી")
        name_input = st.text_input("✍️ તમારું નામ લખો:", value=st.session_state.player_name)
        if name_input: st.session_state.player_name = name_input.strip()
            
        std_list = list(st.session_state.base_db.keys())
        selected_std = st.selectbox("🎯 ધોરણ પસંદ કરો (Std 1 to 12):", std_list)
        
        sub_list = st.session_state.base_db[selected_std]
        selected_sub = st.selectbox("📚 વિષય (Subjects) પસંદ કરો:", sub_list)
        
        quiz_limit = st.selectbox("📊 આ મેચમાં કેટલા પ્રશ્નો રમવા છે?", [10, 20, 50, 100])
        
        if st.button(f"🎮 ગેમ સ્ટાર્ટ કરો, {st.session_state.player_name}!"):
            final_set = []
            if selected_sub in st.session_state.real_questions:
                final_set = list(st.session_state.real_questions[selected_sub])
                random.shuffle(final_set)
            
            while len(final_set) < quiz_limit:
                new_q = generate_infinite_question(selected_sub)
                if new_q["question"] not in [q["question"] for q in final_set]: final_set.append(new_q)
            
            st.session_state.current_match_questions = final_set[:quiz_limit]
            st.session_state.match_index = 0
            st.session_state.score = 100
            st.session_state.game_mode = "PLAYING"
            st.rerun()

    elif st.session_state.game_mode == "PLAYING":
        st.header(f"🕹️ બેટલ ગ્રાઉન્ડ - {st.session_state.player_name}")
        
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
                st.markdown(f"#### 🎯 સ્કોર: <span style='color:#00ffff'>{st.session_state.score}</span>", unsafe_allow_html=True)
                st.write(f"📊 પ્રશ્ન પ્રોગ્રેસ: **{idx + 1} / {total_q}**")
                st.subheader(current_q["question"])
                
                user_choice = st.radio("સાચો વિકલ્પ પસંદ કરો:", current_q["options"], index=None, key=f"inf_q_{idx}")
                if user_choice is not None:
                    if user_choice == current_q["answer"]:
                        st.session_state.score += 10
                        st.toast(f"🎯 જોરદાર જવાબ {st.session_state.player_name}! +10", icon="✅")
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
