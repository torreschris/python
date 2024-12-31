import streamlit as st
import kanji as kj

if "kanji" not in st.session_state:
    st.session_state['kanji'] = kj.GuessingGame()
    st.session_state.kanji.reset()

if "username" not in st.session_state:
    st.session_state.username = "Guest"

if "submit_state" not in st.session_state:
    st.session_state.submit_state = False

#def submit_pressed():
    #placeholder.write("You made a guess")
    
#def next_pressed():
    #placeholder.write("Next Item")
    
st.title("Learn Kanji")
st.sidebar.header('Logged in as:')
st.sidebar.markdown(f'<p style="font-family:Verdana; font-size:16px; color:green;">{st.session_state.username}</p>', unsafe_allow_html=True)

st.sidebar.header('Stats:')
mystats = st.sidebar.empty()
mystats.text(st.session_state.kanji.status_message)

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
    st.image(image='sprites/temp.png',use_container_width=True)

st.markdown(f'<div class="custom-font">{st.session_state.kanji.message}</div>', 
                unsafe_allow_html=True)

#Guess text input
guess=st.text_input("Enter your romanji guess:")

#Create submit and next buttons
col1,col2=st.columns((9,1))
#submit=col1.button("Submit")
#next=col2.button("Next")

if col1.button("Submit", disabled=st.session_state.submit_state):
    st.session_state.kanji.guess = guess.strip()
    st.session_state.kanji.guess_kanji()
    st.session_state.kanji.message
    st.session_state.submit_state = True
    

if col2.button("Next"):
    st.session_state.kanji.reset()
    st.session_state.submit_state = False


#Sst.dataframe(kanji.mydict)