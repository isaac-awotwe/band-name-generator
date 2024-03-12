""" 
The Band Name Generator Application powered by Streamlit
"""

import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.write("Click the button below to begin")
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    st.write("## Welcome to the Band Name Generator.")
    name = st.text_input('What is your name?', on_change=set_state, args=[2])


if st.session_state.stage >=2:
    st.write(f'Hello {name.capitalize()}!')
    city = st.text_input(
        "Which city did you grow up in?",
        on_change = set_state, args=[3]
        )
    if city is None:
        set_state(2)

#if st.session_state.stage == 3:
#   st.button("Next", on_click=set_state, args=[4])

if st.session_state.stage >=3:
    pet = st.text_input(
        "What is the name of a pet?",
        on_change = set_state, args = [4])
    if pet is None:
        set_state(3)

if st.session_state.stage >=4:
    band_name = city.capitalize() + " " + pet.capitalize()
    st.markdown(f"##### Your band name could be :orange[{band_name}]")
    st.button("Start Over", on_click=set_state, args=[0])
