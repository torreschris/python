import streamlit as st
import kanji 

### Session state stuff
if "username" not in st.session_state:
    st.session_state.username = "Guest"

if "submit_state" not in st.session_state:
    st.session_state.submit_state = False

# Initialize session state for the text input
if "kanji_input" not in st.session_state:
    st.session_state.kanji_input = ""

if "kanji" not in st.session_state:
    if st.session_state.username != "Guest":
        st.session_state.kanji = kanji.GuessingGame(f'users/{st.session_state.csvfile}')
    else:
        st.session_state.kanji = kanji.GuessingGame()
    st.session_state.kanji.reset()
    st.session_state.submit_state = False

kj = st.session_state.kanji


### Functions to handle input and reset
def handle_input():
    # Call your method with the input value
    if st.session_state.submit_state != True:
        submit_button_event()

    # Reset the text input field
    st.session_state.kanji_input = ""

def submit_button_event():
    kj.guess = st.session_state.kanji_input
    kj.guess_kanji()
    st.session_state.submit_state = True
    with cols[2]:
        st.markdown(f'<div class="custom-font">{kj.message}</div>',unsafe_allow_html=True)
    mystats.text(kj.status_message)

def next_button_event():
    kj.reset()
    st.session_state.submit_state = False

    kanji_image.image(image='kanji/sprites/temp.png',use_container_width=True)
    kanji_placeholder.markdown(f'<div class="custom-font">{kj.message}</div>',unsafe_allow_html=True)

### Streamlit header
st.title("Learn Kanji")

### Streamlit sidebard 
st.sidebar.header('Logged in as:')
emptysidebar = st.sidebar.empty()
text_color = "green" if st.session_state.username != "Guest" else "red"
emptysidebar.markdown(
    f'<p style="font-family:Verdana; font-size:16px; color:{text_color};">{st.session_state.username}</p>', unsafe_allow_html=True)
st.sidebar.header('Stats:')
mystats = st.sidebar.empty()
mystats.text(kj.status_message)

st.sidebar.header('Game mode:')
choices = ['Easy (multiple choice answer)','Challenge (enter text)']
gamemode = st.sidebar.radio('Select mode:',choices)

### Streamlit body
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
        font-size: 25px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with cols[1]:
    kanji_image = st.empty()
    kanji_image.image(image='kanji/sprites/temp.png',use_container_width=False)

if st.session_state.submit_state:
    with cols[2]:
        st.markdown(f'<div class="custom-font">{kj.message}</div>',unsafe_allow_html=True)

kanji_placeholder = st.empty()
kanji_placeholder.markdown(f'<div class="custom-font">{kj.current_kanji}</div>',unsafe_allow_html=True)
st.write("")
if gamemode == choices[1]:
    # Text input field with on_change callback
    st.text_input(
        "Enter your romanji guess:",
        key="kanji_input",
        on_change=handle_input,  # Triggered when Enter is pressed
    )

    #Create submit and next buttons
    col1,col2=st.columns((9,1))

    col1.button("Submit", disabled=st.session_state.submit_state,on_click=submit_button_event,use_container_width=True)
    col2.button("Next",key="focus-button1", on_click=next_button_event)

else:
    answers = kj.shuffleAnswers()
    empytyEzMode = st.empty()
    col3,col4,col5 = empytyEzMode.columns(3)

    if col3.button(answers[0],use_container_width=True):
        st.session_state.kanji_input = answers[0]
        submit_button_event()
        empytyEzMode.write('')
    elif col4.button(answers[1],use_container_width=True):
        st.session_state.kanji_input = answers[1]
        submit_button_event()
        empytyEzMode.write('')
    elif col5.button(answers[2],use_container_width=True):
        st.session_state.kanji_input = answers[2]
        submit_button_event()
        empytyEzMode.write('')
    
    st.write()

if gamemode == choices[0]:
    st.write(" ")
    if st.session_state.submit_state:
        button_text = "Next"
    else:
        button_text = "Skip" 
    st.button(button_text,key="focus-button2", on_click=next_button_event, use_container_width=True)
