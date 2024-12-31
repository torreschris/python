import streamlit as st
import hashlib
import os

st.title("Login")

if "username" not in st.session_state:
    st.session_state.username = "Guest"

st.sidebar.header('Logged in as:')
emptysidebar = st.sidebar.empty()
text_color = "green" if st.session_state.username != "Guest" else "red"
emptysidebar.markdown(f'<p style="font-family:Verdana; font-size:16px; color:{text_color};">{st.session_state.username}</p>', unsafe_allow_html=True)

username = st.text_input(label='Username:')
password = st.text_input(label='Password:',type='password')

# Input string
input_string = username + password

# Create an MD5 checksum
checksum = hashlib.md5(input_string.encode()).hexdigest() + ".csv"

#st.write("MD5 Checksum: " +  checksum)

if st.button('login'):
    if os.path.isfile(f'users/{checksum}'):
        st.success('Succesfully logged in!')
        st.session_state.username = username
        st.balloons()
        emptysidebar.markdown(f'<p style="font-family:Verdana; font-size:16px; color:green;">{st.session_state.username}</p>', unsafe_allow_html=True)

    else:
        st.error('Username and password is incorrect, try again.')

