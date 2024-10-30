# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/10/30

import streamlit as st
# hide side menu
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("Hello World!")

st.chat_input("Please input your message here...")

st.dialog("Hello, I am a dialog box!")