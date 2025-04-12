# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/10/30

import streamlit as st
from ops_agent import bot_run

# 初始化对话历史记录
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if "awaiting_response" not in st.session_state:
    st.session_state["awaiting_response"] = False

# 显示对话内容
st.title("Z-AIOps Bot")

system_input = '''您好！我是您的生活、工作助手，可以帮助您完成如下的生活和工作需求：

1. 查询相应地点的天气；

2. 根据您的描述画画；

3. 使用Bing搜索帮您查询信息；

4. 查询阿里云ecs实例的实例信息；

5. 帮助您在指定的阿里云ECS实例上执行指定的sh脚本文件；

6. 帮助您查询阿里云ECS实例上指定目录下的所有子目录和文件；

7. 帮助您重启 / 启动 / 停止阿里云ECS实例。'''

st.markdown(
            f"""
            <div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 10px;">
                <img src="https://img.icons8.com/color/48/000000/robot.png" width="30" style="margin-right: 10px;"/>
                <div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; max-width: 60%;">
                    {system_input}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )



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
    temp_response = "【分析执行中，请稍侯...】"
    st.session_state["chat_history"].append({"sender": "bot", "text": temp_response})
    st.session_state["awaiting_response"] = True
    st.rerun()
    # st.markdown(
    #     f"""
    #             <div style="display: flex; align-items: center; justify-content: flex-end; margin-bottom: 10px;">
    #                 <div style="background-color: #e0f7fa; padding: 10px; border-radius: 5px; max-width: 60%; text-align: right;">
    #                     {user_input}
    #                 </div>
    #                 <img src="https://img.icons8.com/color/48/000000/person-male.png" width="30" style="margin-left: 10px;"/>
    #             </div>
    #             """,
    #     unsafe_allow_html=True
    # )

    # 添加系统回复
    # response = user_input[::-1]  # 简单反转用户输入作为回复
    # 临时回复

    # response = bot_run(user_input)
    # st.session_state["chat_history"][-1]["text"] = response  # 更新最后一条消息为实际回复
    # # st.session_state["chat_history"].append({"sender": "bot", "text": response})
    #
    # # 强制刷新页面，显示新消息
    # st.rerun()

# 实际执行bot_run并更新消息
if st.session_state["awaiting_response"]:
    response = bot_run(st.session_state["chat_history"][-2]["text"])  # 获取用户输入
    st.session_state["chat_history"][-1]["text"] = response  # 更新占位消息为真实响应
    st.session_state["awaiting_response"] = False
    st.rerun()




