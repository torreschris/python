import streamlit as st
import hashlib
import os
import shutil

### Initialize session state for the button
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if "username" not in st.session_state:
    st.session_state.username = "Guest"

### Function calls
def new_user():
    if password.strip() == "":
        emptymessage.error('Password cannot be blank.')
    elif not os.path.isfile(f'kanji/users/{checksum}') and username != "Guest":
        emptymessage.success('New account successfully created!')
        st.session_state['username'] = username
        st.session_state['csvfile'] = checksum
        shutil.copy('kanji/allkanji.csv', f'kanji/users/{checksum}')
        st.session_state.button_clicked = True
        st.balloons()
    else:
        emptymessage.error('Username and password is already in use, please try again.')

### Streamlit body
st.title("New user account")
# Styled text
st.sidebar.header('Logged in as:')
text_color = "green" if st.session_state.username != "Guest" else "red"
emptysidebar = st.sidebar.empty()
emptysidebar.markdown(f'<p style="font-family:Verdana; font-size:16px; color:{text_color};">{st.session_state.username}</p>', unsafe_allow_html=True)

username = st.text_input(label='Username:')
password = st.text_input(label='Password:',type='password',on_change=new_user)

# Input string
input_string = username + password
# Create an MD5 checksum
checksum = hashlib.md5(input_string.encode()).hexdigest() + ".csv"

emptymessage = st.empty()

if st.button('Create new account', disabled=st.session_state.button_clicked):
    new_user()

