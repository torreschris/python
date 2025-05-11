import streamlit as st
from gtts import gTTS
import base64
from io import BytesIO
import random

# --- DATA ---
consonants = [
    {"Hangul": "ㄱ", "Pronunciation": "g/k", "Romanization": "giyeok"},
    {"Hangul": "ㄴ", "Pronunciation": "n", "Romanization": "nieun"},
    {"Hangul": "ㄷ", "Pronunciation": "d/t", "Romanization": "digeut"},
    {"Hangul": "ㄹ", "Pronunciation": "r/l", "Romanization": "rieul"},
    {"Hangul": "ㅁ", "Pronunciation": "m", "Romanization": "mieum"},
    {"Hangul": "ㅂ", "Pronunciation": "b/p", "Romanization": "bieup"},
    {"Hangul": "ㅅ", "Pronunciation": "s", "Romanization": "siot"},
    {"Hangul": "ㅇ", "Pronunciation": "ng/silent", "Romanization": "ieung"},
    {"Hangul": "ㅈ", "Pronunciation": "j", "Romanization": "jieut"},
    {"Hangul": "ㅊ", "Pronunciation": "ch", "Romanization": "chieut"},
    {"Hangul": "ㅋ", "Pronunciation": "k", "Romanization": "kieuk"},
    {"Hangul": "ㅌ", "Pronunciation": "t", "Romanization": "tieut"},
    {"Hangul": "ㅍ", "Pronunciation": "p", "Romanization": "pieup"},
    {"Hangul": "ㅎ", "Pronunciation": "h", "Romanization": "hieut"},
    {"Hangul": "ㄲ", "Pronunciation": "kk", "Romanization": "ssang giyeok"},
    {"Hangul": "ㄸ", "Pronunciation": "tt", "Romanization": "ssang digeut"},
    {"Hangul": "ㅃ", "Pronunciation": "pp", "Romanization": "ssang bieup"},
    {"Hangul": "ㅆ", "Pronunciation": "ss", "Romanization": "ssang siot"},
    {"Hangul": "ㅉ", "Pronunciation": "jj", "Romanization": "ssang jieut"},
]

vowels = [
    {"Hangul": "ㅏ", "Pronunciation": "a", "Romanization": "a"},
    {"Hangul": "ㅑ", "Pronunciation": "ya", "Romanization": "ya"},
    {"Hangul": "ㅓ", "Pronunciation": "eo", "Romanization": "eo"},
    {"Hangul": "ㅕ", "Pronunciation": "yeo", "Romanization": "yeo"},
    {"Hangul": "ㅗ", "Pronunciation": "o", "Romanization": "o"},
    {"Hangul": "ㅛ", "Pronunciation": "yo", "Romanization": "yo"},
    {"Hangul": "ㅜ", "Pronunciation": "u", "Romanization": "u"},
    {"Hangul": "ㅠ", "Pronunciation": "yu", "Romanization": "yu"},
    {"Hangul": "ㅡ", "Pronunciation": "eu", "Romanization": "eu"},
    {"Hangul": "ㅣ", "Pronunciation": "i", "Romanization": "i"},
    {"Hangul": "ㅐ", "Pronunciation": "ae", "Romanization": "ae"},
    {"Hangul": "ㅒ", "Pronunciation": "yae", "Romanization": "yae"},
    {"Hangul": "ㅔ", "Pronunciation": "e", "Romanization": "e"},
    {"Hangul": "ㅖ", "Pronunciation": "ye", "Romanization": "ye"},
    {"Hangul": "ㅘ", "Pronunciation": "wa", "Romanization": "wa"},
    {"Hangul": "ㅙ", "Pronunciation": "wae", "Romanization": "wae"},
    {"Hangul": "ㅚ", "Pronunciation": "oe", "Romanization": "oe"},
    {"Hangul": "ㅝ", "Pronunciation": "wo", "Romanization": "wo"},
    {"Hangul": "ㅞ", "Pronunciation": "we", "Romanization": "we"},
    {"Hangul": "ㅟ", "Pronunciation": "wi", "Romanization": "wi"},
    {"Hangul": "ㅢ", "Pronunciation": "ui", "Romanization": "ui"},
]

all_cards = consonants + vowels

# --- CONFIG ---
st.set_page_config(page_title="Korean Alphabet Flashcards", layout="centered")
st.title("🇰🇷 Korean Hangul Learning App")

# --- MODE SWITCH ---
mode = st.sidebar.radio("Choose Mode", ["Flashcards", "Quiz"])

# --- AUDIO FUNCTION ---
def text_to_audio(text):
    tts = gTTS(text, lang='ko')
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp.read()

# --- FLASHCARDS MODE ---
if mode == "Flashcards":
    card_type = st.radio("Select card type:", ["Consonants", "Vowels"])
    cards = consonants if card_type == "Consonants" else vowels
    key_prefix = "con_index" if card_type == "Consonants" else "vow_index"

    if key_prefix not in st.session_state:
        st.session_state[key_prefix] = 0

    index = st.session_state[key_prefix]
    card = cards[index]

    st.markdown(
        f"""
        <div style="text-align: center; font-size: 100px;">{card['Hangul']}</div>
        <div style="text-align: center; font-size: 30px;">Pronunciation: {card['Pronunciation']}</div>
        <div style="text-align: center; font-size: 20px; color: gray;">Romanization: {card['Romanization']}</div>
        """,
        unsafe_allow_html=True
    )

    #st.button("🔊 Play Pronunciation")
    audio_data = text_to_audio(card['Hangul'])
    b64 = base64.b64encode(audio_data).decode()
    st.audio(f"data:audio/mp3;base64,{b64}", format="audio/mp3")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬅️ Back"):
            if index > 0:
                st.session_state[key_prefix] -= 1
    with col2:
        st.markdown(f"<div style='text-align: center;'>Card {index+1} of {len(cards)}</div>", unsafe_allow_html=True)
    with col3:
        if st.button("➡️ Next"):
            if index < len(cards) - 1:
                st.session_state[key_prefix] += 1

# --- QUIZ MODE ---
elif mode == "Quiz":
    st.subheader("🧠 Quiz: What is the Romanization of this Hangul?")

    if "quiz_question" not in st.session_state:
        st.session_state.quiz_question = random.choice(all_cards)
    if "quiz_options" not in st.session_state:
        distractors = random.sample([c for c in all_cards if c != st.session_state.quiz_question], 3)
        options = [c["Romanization"] for c in distractors] + [st.session_state.quiz_question["Romanization"]]
        random.shuffle(options)
        st.session_state.quiz_options = options

    q = st.session_state.quiz_question
    options = st.session_state.quiz_options

    st.markdown(f"<div style='text-align: center; font-size: 100px;'>{q['Hangul']}</div>", unsafe_allow_html=True)
    user_choice = st.radio("Choose the correct Romanization:", options)

    if st.button("Check Answer"):
        if user_choice == q["Romanization"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. The correct answer is: {q['Romanization']}")

    if st.button("🔄 New Question"):
        st.session_state.quiz_question = random.choice(all_cards)
        distractors = random.sample([c for c in all_cards if c != st.session_state.quiz_question], 3)
        options = [c["Romanization"] for c in distractors] + [st.session_state.quiz_question["Romanization"]]
        random.shuffle(options)
        st.session_state.quiz_options = options
