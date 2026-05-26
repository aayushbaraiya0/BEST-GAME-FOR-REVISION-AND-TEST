import streamlit as st
import random
from groq import Groq

# layout="centered" કરવાથી આખી ગેમ સ્ક્રીનની વચ્ચે એકદમ નાની અને સ્લિમ થઈ જશે
st.set_page_config(page_title="Best Game for Revision and Test", page_icon="🎮", layout="centered")

# શાનદાર પ્યોર RGB અને સુપર સ્લિમ ગેમિંગ થીમ (બધી એરર ફિક્સ)
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
    input { 
        color: #000000 !important; 
        font-weight: bold !important;
        height: 35px !important;
    }
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
    div[data-testid="stVerticalBlock"] > div:empty {
        display: none !important;
    }
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

# 📚 ધોરણ ૧ થી ૧૨ નો માસ્ટર ડેટાબેઝ
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
        }
    }

if "real_questions" not in st.session_state:
    st.session_state.real_questions = {
        "Ch 1: રાસાયણિક પ્રક્રિયાઓ અને સમીકરણો": [
            {"question": "મેગ્નેશિયમ પટ્ટીને હવામાં સળગાવતા પહેલાં શા માટે સાફ કરવામાં આવે છે? (PYQ)", "options": ["ભેજ દૂર કરવા", "નિષ્ક્રિય મેગ્નેશિયમ ઓક્સાઇડનું સ્તર દૂર કરવા", "ચળકાટ માટે", "કાર્બોનેટ સ્તર દૂર કરવા"], "answer": "નિષ્ક્રિય મેગ્નેશિયમ ઓક્સાઇડનું સ્તર દૂર કરવા"},
            {"question": "કળી ચૂનાનું (Calcium Oxide) પાણી સાથે ભળવું એ કઈ પ્રક્રિયા છે? (PYQ)", "options": ["ઉષ્માશોષક", "ઉષ્માક્ષેપક", "વિઘટન", "દ્વિ-વિસ્થાપન"], "answer": "ઉષ્માક્ષેપક"}
        ],
        "Ch 2: એસિડ, બેઇઝ અને ક્ષાર": [
            {"question": "કોઈ દ્રાવણ લાલ લિટમસ પત્રને ભૂરું બનાવે છે, તો તેની pH કેટલી હોઈ શકે? (PYQ)", "options": ["1", "4", "5", "10"], "answer": "10"}
        ],
        "Ch 2: બહુપદીઓ": [
            {"question": "દ્વિઘાત બહુપદી x² + 7x + 10 ના શૂન્યોનો સરવાળો કેટલો થાય? (PYQ)", "options": ["7", "-7", "10", "-10"], "answer": "-7"}
        ]
    }

def generate_infinite_question(chapter_name):
    a = random.randint(2, 9)
    b = random.randint(2, 10)
    return {
        "question": f"[MATH CHALLENGE] {chapter_name} મુજબ, {a} ગુણ્યા {b} નો સાચો જવાબ શું થાય?",
        "options": [str(a*b), str(a*b+4), str(a*b-2), str(a+b)],
        "answer": str(a*b)
    }

if "player_name" not in st.session_state: st.session_state.player_name = "Aayush"
if "score" not in st.session_state: st.session_state.score = 100
if "current_match_questions" not in st.session_state: st.session_state.current_match_questions = []
if "match_index" not in st.session_state: st.session_state.match_index = 0
if "game_mode" not in st.session_state: st.session_state.game_mode = "SETUP"
if "ai_open" not in st.session_state: st.session_state.ai_open = False

# 🕹️ મેઈન ગેમ લૂપ
if st.session_state.game_mode == "SETUP":
    st.subheader("⚙️ ગેમ સેટઅપ લોબી")
    name_input = st.text_input("✍️ તમારું નામ લખો:", value=st.session_state.player_name)
    if name_input: st.session_state.player_name = name_input.strip()
        
    std_list = list(st.session_state.base_db.keys())
    selected_std = st.selectbox("🎯 ધોરણ પસંદ કરો (Std 1 to 12):", std_list, index=std_list.index("Std 10") if "Std 10" in std_list else 0)
    
    sub_list = list(st.session_state.base_db[selected_std].keys())
    selected_sub = st.selectbox("📚 વિષય (Subjects) પસંદ કરો:", sub_list)
    
    ch_list = st.session_state.base_db[selected_std][selected_sub]
    selected_ch = st.selectbox("📖 પ્રકરણ (Chapters) પસંદ કરો:", ch_list)
    
    quiz_limit = st.selectbox("📊 આ મેચમાં કેટલા પ્રશ્નો રમવા છે?", [10, 20, 50])
    
    if st.button(f"🎮 ગેમ સ્ટાર્ટ કરો, {st.session_state.player_name}!"):
        final_set = []
        if selected_ch in st.session_state.real_questions:
            final_set = list(st.session_state.real_questions[selected_ch])
            random.shuffle(final_set)
        
        while len(final_set) < quiz_limit:
            new_q = generate_infinite_question(selected_ch)
            final_set.append(new_q)
            
        st.session_state.current_match_questions = final_set[:quiz_limit]
        st.session_state.match_index = 0
        st.session_state.score = 100
        st.session_state.game_mode = "PLAYING"
        st.rerun()

elif st.session_state.game_mode == "PLAYING":
    st.subheader(f"🕹️ બેટલ Г્રાઉન્ડ - {st.session_state.player_name}")
    if st.session_state.score <= 0:
        st.error(f"💥 GAME OVER {st.session_state.player_name}!")
        if st.button("🔄 લોબીમાં પાછા ફરો"):
            st.session_state.game_mode = "SETUP"
            st.rerun()
    else:
        idx = st.session_state.match_index
        total_q = len(st.session_state.current_match_questions)
        if idx < total_q:
            current_q = st.session_state.current_match_questions[idx]
            st.markdown(f"#### 🎯 સ્કોર: {st.session_state.score} | 📊 પ્રશ્ન: {idx + 1} / {total_q}")
            st.subheader(current_q["question"])
            user_choice = st.radio("વિકલ્પ પસંદ કરો:", current_q["options"], index=None, key=f"q_{idx}")
            if user_choice is not None:
                if user_choice == current_q["answer"]:
                    st.session_state.score += 10
                    st.toast("સાચો જવાબ! +10", icon="✅")
                    st.session_state.match_index += 1
                else:
                    st.session_state.score -= 50
                st.rerun()
        else:
            st.balloons()
            st.success("🎉 તમે વિજેતા બન્યા!")
            if st.button("🏁 નવી મેચ"):
                st.session_state.game_mode = "SETUP"
                st.rerun()

# 🧠 --- ચાણક્ય AI સાઇડ ફોલ્ડર બોક્સ લોકેશન ---
st.write("---")
col_space, col_btn = st.columns([2.8, 1.2])
with col_btn:
    if st.button("🧠 ચાણક્ય AI ઓપન / ક્લોઝ", key="chanakya_btn"):
        st.session_state.ai_open = not st.session_state.ai_open
        st.rerun()

if st.session_state.ai_open:
    st.markdown("<div class='ai-sidebar-box'>", unsafe_allow_html=True)
    st.subheader("🧠 ચાણક્ય AI")
    st.write(f"પ્રણામ {st.session_state.player_name} ભાઈ! હું ચાણક્ય AI છું. અહીં તમારા ડાઉટ્સ પૂછો!")
    st.markdown("</div>", unsafe_allow_html=True)
