import streamlit as st
Title=print("SELAMAT DATANG!")
flex = st.container(horizontal=True, horizontal_alignment="right")

for card in range(3):
    flex.button(f"Button {card + 1}")

Copy
