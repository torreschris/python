import streamlit as st
from PIL import Image
import os
import random

# --- Config ---
CARD_FOLDER = os.path.join(os.path.dirname(__file__), "cards")
CARD_EXT = (".png", ".jpg", ".jpeg")

# --- Page Setup ---
st.set_page_config(page_title="Card Viewer", layout="centered")

# --- Load and Shuffle Cards Once ---
if "shuffled_cards" not in st.session_state:
    card_files = [f for f in os.listdir(CARD_FOLDER) if f.endswith(CARD_EXT)]
    random.shuffle(card_files)
    st.session_state.shuffled_cards = card_files
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.revealed = False

# --- Navigation Buttons ---
st.title("🎴 Card Navigator")

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️ Back") and st.session_state.current_index > 0:
        st.session_state.current_index -= 1
        st.session_state.revealed = False
with col3:
    if st.button("Next ➡️") and st.session_state.current_index < len(st.session_state.shuffled_cards) - 1:
        st.session_state.current_index += 1
        st.session_state.revealed = False

# --- Current Card Info ---
index = st.session_state.current_index
card_filename = st.session_state.shuffled_cards[index]
card_name = card_filename.rsplit(".", 1)[0]

st.subheader(f"Card {index + 1} of {len(st.session_state.shuffled_cards)}")
st.write(f"**Name:** {card_name.replace('_', ' of ')}")
# --- Show Image Button ---
if not st.session_state.revealed:
    if st.button("👁️ Show Image"):
        st.session_state.revealed = True

# --- Display Image if Revealed ---
if st.session_state.revealed:
    image_path = os.path.join(CARD_FOLDER, card_filename)
    image = Image.open(image_path)
    st.image(image, caption=card_name)
