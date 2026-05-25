import streamlit as st
import random

# પેજ સેટઅપ અને ઓફિશિયલ ટાઇટલ
st.set_page_config(page_title="Best Game for Revision and Test", page_icon="🎮", layout="wide")

# શાનદાર પ્યોર RGB અને ડાર્ક નિયોન ગેમિંગ થીમ (ગ્રીન થીમ રીમુવ્ડ)
st.markdown("""
    
    """, unsafe_allow_html=True)

# 🎮 ઓફિશિયલ ગેમ ટાઇટલ હેડર
st.markdown("🎮 BEST GAME FOR REVISION AND TEST", unsafe_allow_html=True)

# પ્રશ્નોનો બેઝ પૂલ
if "base_db" not in st.session_state:
    st.session_state.base_db = {
        "Std 10": {
            "વિજ્ઞાન (Science)": {
                "Ch 1: રાસાયણિક પ્રક્રિયાઓ": [
                    {"question": "મેગ્નેશિયમ પટ્ટીને હવામાં સળગાવતા પહેલાં શા માટે સાફ કરવામાં આવે છે? (PYQ)", "options": ["ભેજ દૂર કરવા", "નિષ્ક્રિય મેગ્નેશિયમ ઓક્સાઇડનું સ્તર દૂર કરવા", "ચળકાટ માટે", "કાર્બોનેટ સ્તર દૂર કરવા"], "answer": "નિષ્ક્રિય મેગ્નેશિયમ ઓક્સાઇડનું સ્તર દૂર કરવા"},
                    {"question": "કળી ચૂનાનું (Calcium Oxide) પાણી સાથે ભળવું એ કઈ પ્રક્રિયા છે? (PYQ)", "options": ["ઉષ્માશોષક", "ઉષ્માક્ષેપક", "વિઘટન", "દ્વિ-વિસ્થાપન"], "answer": "ઉષ્માક્ષેપક"},
                    {"question": "લેડ નાઇટ્રેટ પાવડરને ગરમ કરતા કેવા રંગનો ધુમાડો નીકળે છે? (PYQ)", "options": ["સફેદ", "પીળો", "કથ્થઈ (Brown)", "લીલો"], "answer": "કથ્થઈ (Brown)"}
                ],
                "Ch 2: એસિડ, બેઇઝ અને ક્ષાર": [
                    {"question": "કોઈ દ્રાવણ લાલ લિટમસ પત્રને ભૂરું બનાવે છે, તો તેની pH કેટલી હોઈ શકે? (PYQ)", "options": ["1", "4", "5", "10"], "answer": "10"},
                    {"question": "પ્લાસ્ટર ઓફ પેરિસ (POP) નું સાચું રાસાયણિક સૂત્ર કયું છે? (PYQ)", "options": ["CaSO₄ · 2H₂O", "CaSO₄ · ½H₂O", "CuSO₄ · 5H₂O", "Na₂CO₃ · 10H₂O"], "answer": "CaSO₄ · ½H₂O"}
                ]
            },
            "ગણિત (Maths)": {
                "Ch 2: બહુપદીઓ": [
                    {"question": "દ્વિઘાત બહુપદી x² + 7x + 10 ના શૂન્યોનો સરવાળો કેટલો થાય? (PYQ)", "options": ["7", "-7", "10", "-10"], "answer": "-7"}
                ]
            }
        }
    }

def generate_infinite_question(subject, chapter):
    if "ગણિત" in subject:
        a = random.randint(2, 9)
        b = random.randint(1, 15)
        ans = -b
        return {
            "question": f"[INFINITE MATH CHALLENGE] દ્વિઘાત બહુપદી {a}x² + {b*a}x + 12 ના શૂન્યોનો સરવાળો (-b/a) કેટલો થાય?",
            "options": [str(b), str(-b), str(a), str(-a)],
            "answer": str(ans)
        }
    else:
        ph_val = random.choice([1, 2, 3, 4, 5, 6])
        return {
            "question": f"[INFINITE SCIENCE CHALLENGE] એક અજ્ઞાત એસિડિક દ્રાવણની pH નું મૂલ્ય નીચેનામાંથી કયું હોઈ શકે?",
            "options": [str(ph_val), "7", "9", "13"],
            "answer": str(ph_val)
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
            
        std_list = ["Std 10"]
        selected_std = st.selectbox("🎯 ધોરણ પસંદ કરો:", std_list)
        quiz_limit = st.selectbox("📊 આ મેચમાં કેટલા પ્રશ્નો રમવા છે?", [10, 20, 50, 100])
        
        sub_list = list(st.session_state.base_db[selected_std].keys())
        selected_sub = st.selectbox("📚 વિષય પસંદ કરો:", sub_list)
        ch_list = list(st.session_state.base_db[selected_std][selected_sub].keys())
        selected_ch = st.selectbox("📖 પ્રકરણ પસંદ કરો:", ch_list)
        
        if st.button(f"🎮 ગેમ સ્ટાર્ટ કરો, {st.session_state.player_name}!"):
            raw_q = list(st.session_state.base_db[selected_std][selected_sub][selected_ch])
            random.shuffle(raw_q)
            final_set = []
            for q in raw_q:
                if len(final_set) < quiz_limit: final_set.append(q)
            while len(final_set) < quiz_limit:
                new_q = generate_infinite_question(selected_sub, selected_ch)
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
                st.markdown(f"#### 🎯 સ્કોર: {st.session_state.score}", unsafe_allow_html=True)
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
        st.session_state.study_chat_history = [{"role": "assistant", "message": f"નમસ્તે {st.session_state.player_name} ભાઈ! 'Best Game for Revision and Test' માં તમારું સ્વાગત છે. કોઈ પણ ડાઉટ અહીં પૂછો!"}]
    for chat in st.session_state.study_chat_history:
        with st.chat_message(chat["role"]): st.write(chat["message"])
    if study_msg := st.chat_input("અહીં સવાલ પૂછો..."):
        st.session_state.study_chat_history.append({"role": "user", "message": study_msg})
        with st.chat_message("user"): st.write(study_msg)
        study_reply = f"ખૂબ સરસ સવાલ {st.session_state.player_name}! આ રિવિઝન ગેમ તમારા બોર્ડના માર્ક્સ પાકા કરાવી દેશે. રકમ લખો એટલે હું ગણી આપું!"
        st.session_state.study_chat_history.append({"role": "assistant", "message": study_reply})
        with st.chat_message("assistant"): st.write(study_reply)
        st.rerun()
