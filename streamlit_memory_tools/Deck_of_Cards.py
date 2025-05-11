import streamlit as st
from PIL import Image, ImageOps
import os

st.set_page_config(
    page_title="Card Viewer",
    layout="wide",           # <- This makes the app use the full width
    initial_sidebar_state="collapsed"
)
# --- Configuration ---
CARD_FOLDER = os.path.join(os.path.dirname(__file__), "cards")
THUMB_SIZE = (150, 200)
INSERT_SIZE = (600, 800)


# Load card image filenames
card_files = sorted([f for f in os.listdir(CARD_FOLDER) if f.endswith((".png", ".jpg", ".jpeg"))])[::-1]

# Session state for selected card
if "selected_card" not in st.session_state:
    st.session_state.selected_card = None

st.title("🃏 Card Gallery Viewer")

# --- Gallery View ---
#st.subheader("Card Gallery")

# Display thumbnails in a grid
cols = st.columns(4)
for i, card_file in enumerate(card_files):
    col = cols[i % 4]
    with col:
        thumb = Image.open(os.path.join(CARD_FOLDER, card_file)).convert("RGBA")
        thumb.thumbnail(THUMB_SIZE)
        st.image(thumb, caption=card_file.split('.')[0])
        #if st.button("", key=f"thumb_{i}"):
        #    st.session_state.selected_card = card_file
        

# --- Fullscreen View ---
if st.session_state.selected_card:
    card_path = os.path.join(CARD_FOLDER, st.session_state.selected_card)
    card_image = Image.open(card_path).convert("RGBA")
    #st.image(card_image)
