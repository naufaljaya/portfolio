import streamlit as st
from constant import *


def show_computer_vision():
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Home", "Object Counter(Image)", "Object Counter(Video)", "Facial Recognition", "Supported Object"])
    with tab1:
        st.header("Welcome")
    with tab2:
        st.header("Object Counter From Image")
    with tab3:
        st.header("Object Counter From Video")
    with tab4:
        st.header("Facial Recognition")
    with tab5:
        st.header("Supported image")
        for alphabet in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            with st.expander(alphabet):
                for o in [obj for obj in CLASSNAMES if obj[0] == alphabet.lower()]:
                    st.write(o.title())
