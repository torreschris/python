import streamlit as st
import kanji 
import time

if "kanji" not in st.session_state:
    st.session_state.kanji = kanji.GuessingGame()
    st.session_state.kanji.reset()

kj = st.session_state.kanji

if "username" not in st.session_state:
    st.session_state.username = "Guest"

if st.session_state.username != "Guest":
    kj.read_csv_kanji(f'users/{st.session_state.csvfile}')

if "submit_state" not in st.session_state:
    st.session_state.submit_state = False

st.title("Learn Kanji")
st.sidebar.header('Logged in as:')
emptysidebar = st.sidebar.empty()
text_color = "green" if st.session_state.username != "Guest" else "red"
emptysidebar.markdown(f'<p style="font-family:Verdana; font-size:16px; color:{text_color};">{st.session_state.username}</p>', unsafe_allow_html=True)

st.sidebar.header('Stats:')
mystats = st.sidebar.empty()
mystats.text(kj.status_message)

#Placeholder for the kanji
placeholder = st.empty()

#Using Columns to center the box
cols = placeholder.columns(3)

# Inject custom CSS to change the font of kanji text
st.markdown(
    """
    <style>
    .custom-font {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 40px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with cols[1]:
    kanji_image = st.empty()
    kanji_image.image(image='sprites/temp.png',use_container_width=True)

kanji_placeholder = st.empty()
kanji_placeholder.markdown(f'<div class="custom-font">{kj.message}</div>',unsafe_allow_html=True)

#Guess text input
# Function to handle input and reset
def handle_input():
    # Call your method with the input value
    if st.session_state.submit_state != True:
        submit_button_event()

    
    # Reset the text input field
    st.session_state.kanji_input = ""


# Initialize session state for the text input
if "kanji_input" not in st.session_state:
    st.session_state.kanji_input = ""

# Text input field with on_change callback
st.text_input(
    "Enter your romanji guess:",
    key="kanji_input",
    on_change=handle_input,  # Triggered when Enter is pressed
)

#Create submit and next buttons
col1,col2=st.columns((9,1))

def submit_button_event():
    kj.guess = st.session_state.kanji_input
    kj.guess_kanji()
    st.session_state.submit_state = True
    #countdown(5)
    #next_button_event()
    

def next_button_event():
    kj.reset()
    st.session_state.submit_state = False

    kanji_image.image(image='sprites/temp.png',use_container_width=True)
    kanji_placeholder.markdown(f'<div class="custom-font">{kj.message}</div>',unsafe_allow_html=True)

col1.button("Submit", disabled=st.session_state.submit_state,on_click=submit_button_event)

col2.button("Next",key="focus-button", on_click=next_button_event)

# Placeholder for the countdown display
countdown_placeholder = st.empty()

# Function to perform the countdown
def countdown(seconds):
    for i in range(seconds, 0, -1):
        countdown_placeholder.write(f"Starting in {i} seconds...")
        time.sleep(1)  # Wait for 1 second
    countdown_placeholder.empty()  # Clear the countdown message
