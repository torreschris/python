import streamlit as st
import hashlib
import os
import shutil

# Initialize session state for the button
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if "username" not in st.session_state:
    st.session_state.username = "Guest"

st.title("New user account")

# Styled text
st.sidebar.header('Logged in as:')
text_color = "green" if st.session_state.username != "Guest" else "red"
emptysidebar = st.sidebar.empty()
emptysidebar.markdown(f'<p style="font-family:Verdana; font-size:16px; color:{text_color};">{st.session_state.username}</p>', unsafe_allow_html=True)


username = st.text_input(label='Username:')
password = st.text_input(label='Password:',type='password')

# Input string
input_string = username + password
# Create an MD5 checksum
checksum = hashlib.md5(input_string.encode()).hexdigest() + ".csv"

if st.button('Create new account', disabled=st.session_state.button_clicked):
    if not password:
        st.error('Password cannot be blank.')
    elif not os.path.isfile(f'users/{checksum}'):
        st.success('New account successfully created!')
        st.session_state['username'] = username
        st.session_state['csvfile'] = checksum
        shutil.copy('allkanji.csv', f'users/{checksum}')
        st.session_state.button_clicked = True
    else:
        st.error('Username and password is already in use, please try again.')
    