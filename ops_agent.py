# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/10/31

# 配置环境变量；如果您已经提前将api-key提前配置到您的运行环境中，可以省略这个步骤
import os
os.environ['DASHSCOPE_API_KEY']='sk-2be205b8435d4528812c68ec78e0d9b2'
# os.environ['MODELSCOPE_API_TOKEN']='e8d2a5d5-1cbe-4b32-85c5-df6a8722ebd0'
os.environ['AMAP_TOKEN']='2acea0d65909370fb77d3fc4370d707c'
os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']='04789e3f50b94453a013994abd499b9d'

# 选用RolePlay 配置agent
from modelscope_agent.agents.role_play import RolePlay  # NOQA

# role_template = '你扮演一个天气预报助手，你需要查询相应地区的天气，并调用给你的画图工具绘制一张城市的图。'

# role_template = '你扮演一个精通devops的运维专家，你需要查询用户想要了解的开放API信息，及执行一些运维操作。'

role_template = '你是一个善于帮助用户处理各种生活事项的生活小助手，你需要查询相应地点的天气，还会根据用户的描述画画，还可以帮助用户用搜索引擎查询信息。'

llm_config = {'model': 'qwen-max', 'model_server': 'dashscope'}
# llm_config = {'model': 'Qwen/Qwen2.5-7B-Instruct', 'model_server': 'modelscope'}

# input tool name
function_list = ['amap_weather', 'image_gen', 'web_search']
# function_list = ['web_search']

bot = RolePlay(
    function_list=function_list, llm=llm_config, instruction=role_template)

def bot_run(prompt):
    response = bot.run(prompt)

    text = ''
    for chunk in response:
        text += chunk

    print('\n\n')
    print(text)
    return text



