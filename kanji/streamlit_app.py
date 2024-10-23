import streamlit as st
#from kanji import GuessingGame

def submit_pressed():
    placeholder.write("You made a guess")

def next_pressed():
    placeholder.write("Next Item")

st.title("Learn Kanji")

#Placeholder for the kanji
placeholder = st.empty()

#Using Columns to center the box
cols = placeholder.columns((1,4,1))
#Make a box as a placeholder image
box = """<p style="padding: 10px; border: 2px solid red;">YOUR IMG</p>"""
#Put the box in the middle column
with cols[1]:
    st.markdown(box,unsafe_allow_html=True)

#Guess text input
guess=st.text_input("Guess")

#Create submit and next buttons
col1,col2=st.columns((9,1))
submit=col1.button("Submit")
next=col2.button("Next")

if submit:
    submit_pressed()
if next:
    next_pressed()