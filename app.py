# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/10/30

import streamlit as st
# hide side menu
# hide_menu_style = """
#         <style>
#         #MainMenu {visibility: hidden;}
#         </style>
#         """
# st.markdown(hide_menu_style, unsafe_allow_html=True)
#
# st.title("Hello World!")
#
# st.chat_input("Please input your message here...")
#

# 初始化对话历史记录
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# 显示对话内容
st.title("Z-AIOps Bot")

for chat in st.session_state["chat_history"]:
    if chat["sender"] == "user":
        st.markdown(f"<div style='background-color: #e0f7fa; padding: 10px; border-radius: 5px;'>{chat['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin-top: 5px;'>{chat['text']}</div>", unsafe_allow_html=True)

# 底部输入框和发送按钮
user_input = st.text_input("请输入您的消息：", "")
if st.button("发送"):
    if user_input:
        # 添加用户输入
        st.session_state["chat_history"].append({"sender": "user", "text": user_input})
        # 添加系统回复
        response = user_input[::-1]  # 简单反转用户输入作为回复
        st.session_state["chat_history"].append({"sender": "bot", "text": response})
