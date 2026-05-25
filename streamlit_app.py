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
    /* નામ લખવાના બોક્સમાં કાળો કલર */
    input { 
        color: #000000 !important; 
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 🎮 ઓફિશિયલ ગેમ ટાઇટલ હેડર
st.markdown("<h1>🎮 BEST GAME FOR REVISION AND TEST</h1>", unsafe_allow_html=True)

# 📚 Std 1 થી 12 ના તમામ વિષયોનો ડાયનેમિક પૂલ
if "base_db" not in st.session_state:
    st.session_state.base_db = {
        "Std 1": {"ગણિત ગમ્મત": {}, "કલરવ (ગુજરાતી)": {}, "અંગ્રેજી": {}},
        "Std 2": {"ગણિત ગમ્મત": {}, "હલ્લોલ (ગુજરાતી)": {}, "અંગ્રેજી": {}},
        "Std 3": {"ગણિત": {}, "ગુજરાતી (મયુર)": {}, "આસપાસ (પર્યાવરણ)": {}, "અંગ્રેજી": {}},
        "Std 4": {"ગણિત": {}, "ગુજરાતી": {}, "આસપાસ (પર્યાવરણ)": {}, "અંગ્રેજી": {}},
        "Std 5": {"ગણિત": {}, "ગુજરાતી (કેકારવ)": {}, "સૌની આસપાસ": {}, "અંગ્રેજી": {}, "હિન્દી": {}},
        "Std 6": {"ગણિત (Maths)": {}, "વિજ્ઞાન (Science)": {}, "સામાજિક વિજ્ઞાન": {}, "ગુજરાતી": {}, "અંગ્રેજી": {}, "હિન્દી": {}, "સંસ્કૃત": {}},
        "Std 7": {"ગણિત (Maths)": {}, "વિજ્ઞાન (Science)": {}, "સામાજિક વિજ્ઞાન": {}, "ગુજરાતી": {}, "અંગ્રેજી": {}, "હિન્દી": {}, "સંસ્કૃત": {}},
        "Std 8": {"ગણિત (Maths)": {}, "વિજ્ઞાન (Science)": {}, "સામાજિક વિજ્ઞાન": {}, "ગુજરાતી": {}, "અંગ્રેજી": {}, "હિન્દી": {}, "સંસ્કૃત": {}},
        "Std 9": {"ગણિત (Maths)": {}, "વિજ્ઞાન (Science)": {}, "સામાજિક વિજ્ઞાન": {}, "ગુજરાતી": {}, "અંગ્રેજી": {}, "હિન્દી": {}, "સંસ્કૃત": {}},
        "Std 10": {
            "વિજ્ઞાન (Science)": {
                "Ch 1: રાસાયણિક પ્રક્રિયાઓ": [
                    {"question": "મેગ્નેશિયમ પટ્ટીને હવામાં સળગાવતા પહેલાં શા માટે સાફ કરવામાં આવે છે? (PYQ)", "options": ["ભેજ દૂર કરવા", "નિષ્ક્રિય મેગ્નેશિયમ ઓક્સાઇડનું સ્તર દૂર કરવા", "ચળકાટ માટે", "કાર્બોનેટ સ્તર દૂર કરવા"], "answer": "નિષ્ક્રિય મેગ્નેશિયમ ઓક્સાઇડનું સ્તર દૂર કરવા"},
                    {"question": "કળી ચૂનાનું (Calcium Oxide) પાણી સાથે ભળવું એ કઈ પ્રક્રિયા છે? (PYQ)", "options": ["ઉષ્માશોષક", "ઉષ્માક્ષેપક", "વિઘટન", "દ્વિ-વિસ્થાપન"], "answer": "ઉષ્માક્ષેપક"}
                ],
                "Ch 2: એસિડ, બેઇઝ અને ક્ષાર": [
                    {"question": "કોઈ દ્રાવણ લાલ લિટમસ પત્રને ભૂરું બનાવે છે, તો તેની pH કેટલી હોઈ શકે? (PYQ)", "options": ["1", "4", "5", "10"], "answer": "10"}
                ]
            },
            "ગણિત (Maths)": {
                "Ch 2: બહુપદીઓ": [
                    {"question": "દ્વિઘાત બહુપદી x² + 7x + 10 ના શૂન્યોનો સરવાળો કેટલો થાય? (PYQ)", "options": ["7", "-7", "10", "-10"], "answer": "-7"}
                ]
            },
            "સામાજિક વિજ્ઞાન": {}, "ગુજરાતી": {}, "અંગ્રેજી": {}, "હિન્દી": {}, "સંસ્કૃત": {}
        },
        "Std 11 (Science)": {"ગણિત (Maths)": {}, "ભૌતિક વિજ્ઞાન (Physics)": {}, "રસાયણ વિજ્ઞાન (Chemistry)": {}, "જીવ વિજ્ઞાન (Biology)": {}, "અંગ્રેજી": {}},
        "Std 11 (Commerce)": {"નામાના મૂળતત્વો (Account)": {}, "આંકડાશાસ્ત્ર (Stats)": {}, "અર્થશાસ્ત્ર (Eco)": {}, "વાણિજ્ય વ્યવસ્થા (BA)": {}, "અંગ્રેજી": {}},
        "Std 12 (Science)": {"ગણિત (Maths)": {}, "ભૌતિક વિજ્ઞાન (Physics)": {}, "રસાયણ વિજ્ઞાન (Chemistry)": {}, "જીવ વિજ્ઞાન (Biology)": {}, "અંગ્રેજી": {}},
        "Std 12 (Commerce)": {"નામાના મૂળતત્વો (Account)": {}, "આંકડાશાસ્ત્ર (Stats)": {}, "અર્થશાસ્ત્ર (Eco)": {}, "વાણિજ્ય વ્યવસ્થા (BA)": {}, "અંગ્રેજી": {}}
    }

def generate_infinite_question(subject):
    if "ગણિત" in subject or "Maths" in subject or "આંકડાશાસ્ત્ર" in subject:
        a = random.randint(2, 9)
        b = random.randint(1, 12)
        ans = a * b
        return {
            "question": f"[DYNAMIC MATH RUN] {a} ગુણ્યા {b} નો સાચો જવાબ શું થાય?",
            "options": [str(ans), str(ans + random.randint(1,5)), str(ans - random.randint(1,3)), str(a + b)],
            "answer": str(ans)
        }
    else:
        options_pool = ["સાચું વિધાન", "ખોટું વિધાન", "માહિતી અધૂરી છે", "કહી શકાય નહીં"]
        return {
            "question": f"[DYNAMIC REVISION RUN] {subject} ના આ ટોપિક માટે નીચેનામાંથી કયો વિકલ્પ સૌથી યોગ્ય છે?",
            "options": options_pool,
            "answer": options_pool[0]
        }

if "player_name" not in st.session_state: st.session_state.player_name = "Jasharaj"
if "score" not in st.session_state: st.session_state.score = 100
if "current_match_questions" not in st.session_state: st.session_state.current_match_questions = []
if "match_index" not in st.session_state: st.session_state.match_index = 0
if "game_mode" not in st.session_state: st.session_state.game_mode = "SETUP"

col1, col2 = st.columns([1.3, 1])

with col1:
    if st.session_state.game_mode == "SETUP":
        st.header("⚙️ ગેમ સેટઅપ લોબી")
        name_input = st.text_input("✍️ તમારું નામ:", value=st.session_state.player_name)
        if name_input: st.session_state.player_name = name_input.strip()
            
        # 🎯 ૧ થી ૧૨ ધોરણનું ફિક્સ ડ્રોપડાઉન લિસ્ટ
        std_list = list(st.session_state.base_db.keys())
        selected_std = st.selectbox("🎯 ધોરણ પસંદ કરો (Std 1 to 12):", std_list)
        
        sub_list = list(st.session_state.base_db[selected_std].keys())
        selected_sub = st.selectbox("📚 વિષય (Subjects) પસંદ કરો:", sub_list)
        
        ch_list = ["પ્રકરણ ૧: રિવિઝન મેગા લૂપ"]
        if st.session_state.base_db[selected_std][selected_sub]:
            ch_list = list(st.session_state.base_db[selected_std][selected_sub].keys())
        selected_ch = st.selectbox("📖 પ્રકરણ પસંદ કરો:", ch_list)
        
        quiz_limit = st.selectbox("📊 આ મેચમાં કેટલા પ્રશ્નો રમવા છે?", [10, 20, 50, 100])
        
        if st.button(f"🎮 ગેમ સ્ટાર્ટ કરો, {st.session_state.player_name}!"):
            raw_q = []
            if selected_ch in st.session_state.base_db[selected_std][selected_sub]:
                raw_q = list(st.session_state.base_db[selected_std][selected_sub][selected_ch])
            
            random.shuffle(raw_q)
            final_set = []
            for q in raw_q:
                if len(final_set) < quiz_limit: final_set.append(q)
            
            while len(final_set) < quiz_limit:
                new_q = generate_infinite_question(selected_sub)
                if new_q["question"] not in [q["question"] for q in final_set]: final_set.append(new_q)
            
            st.session_state.current_match_questions = final_set
            st.session_state.match_index = 0
            st.session_state.score = 100
            st.session_state.game_mode = "PLAYING"
            st.rerun()

    elif st.session_state.game_mode == "PLAYING":
        st.header(f"🕹️ બેટલ ગ્રાઉન્ડ - {st.session_state.player_name}")
        if st.session_state.score <= 0:
            st.error(f"💥 GAME OVER {st.session_state.player_name}! તમારા પોઈન્ટ્સ 0 થઈ ગયા.")
            if st.button("🔄 લોબીમાં પાછા ફરો"):
                st.session_state.game_mode = "SETUP"
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
                        if st.session_state.score <= 0: st.rerun()
                    st.rerun()
            else:
                st.balloons()
                st.success(f"🎉 વિજેતા {st.session_state.player_name}! તમે આખી કાયમી ચેલેન્જ પાર કરી લીધી!")
                if st.button("🏁 નવો રેકોર્ડ સેટ કરો"):
                    st.session_state.game_mode = "SETUP"
                    st.rerun()

with col2:
    st.header("🧠 સ્ટડી ગુરુ AI")
    if "study_chat_history" not in st.session_state:
        st.session_state.study_chat_history = [{"role": "assistant", "message": f"નમસ્તે {st.session_state.player_name} ભાઈ! Std 1 થી 12 ની 'Best Game for Revision and Test' માં તમારું સ્વાગત છે. કોઈ પણ ડાઉટ અહીં પૂછો!"}]
    for chat in st.session_state.study_chat_history:
        with st.chat_message(chat["role"]): st.write(chat["message"])
    if study_msg := st.chat_input("અહીં સવાલ પૂછો..."):
        st.session_state.study_chat_history.append({"role": "user", "message": study_msg})
        with st.chat_message("user"): st.write(study_msg)
        study_reply = f"ખૂબ સરસ સવાલ {st.session_state.player_name}! આ કાયમી ગેમ તમારા બોર્ડની ધમાકેદાર તૈયારી કરાવી દેશે!"
        st.session_state.study_chat_history.append({"role": "assistant", "message": study_reply})
        with st.chat_message("assistant"): st.write(study_reply)
        st.rerun()
