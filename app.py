# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/10/30

import streamlit as st
from ops_agent import bot_run

# 初始化对话历史记录
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# 显示对话内容
st.title("Z-AIOps Bot")

# 遍历并显示历史对话内容
for chat in st.session_state["chat_history"]:
    if chat["sender"] == "user":
        # 用户消息：带人类头像在右侧
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; justify-content: flex-end; margin-bottom: 10px;">
                <div style="background-color: #e0f7fa; padding: 10px; border-radius: 5px; max-width: 60%; text-align: right;">
                    {chat['text']}
                </div>
                <img src="https://img.icons8.com/color/48/000000/person-male.png" width="30" style="margin-left: 10px;"/>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        # 系统回复：带机器人头像在左侧
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 10px;">
                <img src="https://img.icons8.com/color/48/000000/robot.png" width="30" style="margin-right: 10px;"/>
                <div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; max-width: 60%;">
                    {chat['text']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# 固定底部的输入框和提交按钮
user_input = st.chat_input("请输入您的消息：")
if user_input:
    # 添加用户输入
    st.session_state["chat_history"].append({"sender": "user", "text": user_input})
    # 添加系统回复
    # response = user_input[::-1]  # 简单反转用户输入作为回复
    response = bot_run(user_input)
    st.session_state["chat_history"].append({"sender": "bot", "text": response})

    # 强制刷新页面，显示新消息
    # st.experimental_rerun()
    st.rerun()