import streamlit as st
flex = st.container(vertical=True, vertical_alignment="left")

for card in range(3):
    flex.button(f"Button {card + 1}")

Copy

