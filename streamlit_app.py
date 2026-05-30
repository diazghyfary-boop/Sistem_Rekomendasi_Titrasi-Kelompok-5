import streamlit as st
st.set_page_config(
page_title="SELAMAT DATANG!")
flex = st.container(horizontal=True, horizontal_alignment="right")

for card in range(3):
    flex.button(f"Button {card + 1}")

Copy
