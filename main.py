import streamlit as st
from time_series import show_time_series
from computer_vision import show_computer_vision

st.set_page_config(
    page_title="My Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

sidebar = st.sidebar.selectbox(
    "Select Project",
    ("Time Series", "Computer Vision")
)

if sidebar == "Time Series":
    show_time_series()
elif sidebar == "Computer Vision":
    show_computer_vision()
