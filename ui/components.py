import streamlit as st

def input_box():
    return st.text_input(
        "Enter a company name or question:",
        key="user_input"     
    )


def primary_button(label="Search"):
    return st.button(label)
