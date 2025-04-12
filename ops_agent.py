# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/10/31

# 配置环境变量；如果您已经提前将api-key提前配置到您的运行环境中，可以省略这个步骤
import os
import ssl
import re
os.environ['DASHSCOPE_API_KEY']='sk-2be205b8435d4528812c68ec78e0d9b2'
# os.environ['MODELSCOPE_API_TOKEN']='e8d2a5d5-1cbe-4b32-85c5-df6a8722ebd0'
os.environ['AMAP_TOKEN']='2acea0d65909370fb77d3fc4370d707c'
os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']='04789e3f50b94453a013994abd499b9d'

os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'] = 'LTAI5tE9zxV6cmUg4aWwp63P'
os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'] = 'KC7b5l1zvdTwUotFL5LMwX1CRPDGAM'


ssl._create_default_https_context = ssl._create_unverified_context

# 选用RolePlay 配置agent
from modelscope_agent.agents.role_play import RolePlay  # NOQA

# role_template = '你扮演一个天气预报助手，你需要查询相应地区的天气，并调用给你的画图工具绘制一张城市的图。'

# role_template = '你扮演一个精通devops的运维专家，你需要查询用户想要了解的开放API信息，及执行一些运维操作。'

# role_template = '你是一个善于帮助用户处理各种生活事项的生活小助手，你需要查询相应地点的天气，还会根据用户的描述画画，还可以帮助用户用搜索引擎查询信息。'

role_template = '''
你是一个拥有很多技能和专业能力的强大生活、工作助手，可以帮助用户完成如下的生活和工作需求：
1、你可以查询相应地点的天气；
2、你会根据用户的描述画画；
3、你可以帮助用户用搜索引擎查询信息，然后返回给用户搜索结果；
4、你可以帮助用户打开浏览器网页自动进行网页浏览，自动完成鼠标点击、鼠标滚轮滑动、键盘输入等操作；
5、你可以帮助用户查询阿里云ecs实例的实例信息，如何用户未给出具体的IP地址，那么你需要查询所有的实例信息；
6、你可以帮助用户在用户指定的阿里云ECS实例上执行指定的sh脚本文件，如果用户未指定sh脚本文件或者提供错误的sh脚本文件路径，则调用ecs_directory_query工具查询实例的目录文件，向用户展示；
7、你可以帮助用户查询用户指定阿里云ECS实例上指定目录下的所有子目录和文件；
8、你可以帮助用户重启阿里云ECS实例。如果用户未给出具体的IP地址，也未给出具体的实例ID，那么你需要查询所有的实例信息，然后让用户输入想要重启的实例的实例ID，然后再进一步判断：如果实例状态为运行中（Running），才能调用此工具重启实例，否则告诉用户实例状态不是运行中，无法重启；
9、你可以帮助用户启动阿里云ECS实例。如果用户未给出具体的IP地址，也未给出具体的实例ID，那么你需要查询所有的实例信息，然后让用户输入想要启动的实例的实例ID，然后再进一步判断：如果实例状态为已停止（Stopped），才能调用此工具启动实例，否则告诉用户实例状态不是已停止，无法启动；
10、你可以帮助用户停止阿里云ECS实例。如果用户未给出具体的IP地址，也未给出具体的实例ID，那么你需要查询所有的实例信息，然后让用户输入想要停止的实例的实例ID，然后执行停止实例操作。

要求：你可以记住和用户的前几轮对话内容，并且可以从对话的上下文中获取与用户当前最新请求相关的信息，然后自己对信息进行整合，然后分析处理，最后响应给用户。
'''


llm_config = {'model': 'qwen-max', 'model_server': 'dashscope'}
# llm_config = {'model': 'Qwen/Qwen2.5-7B-Instruct', 'model_server': 'modelscope'}

# input tool name
function_list = ['amap_weather', 'image_gen', 'web_search', 'web_browser', 'query_ecs_info',
                 'ecs_scripts_execute', 'ecs_directory_query', 'reboot_ecs_tool', 'start_ecs_tool',
                 'stop_ecs_tool']

bot = RolePlay(
    function_list=function_list, llm=llm_config, instruction=role_template, verify_ssl=False)

def bot_run(prompt):
    response = bot.run(prompt)

    text = ''
    for chunk in response:
        text += chunk

    print('\n\n-----------------------------')
    print(f"bot_run response text: \n{text}\n\n---------------------------------")
    text_action = text + 'Action:'

    # # 编写正则表达式，匹配“Answer:”后的所有内容
    # pattern = r"Answer:(.*)"
    # match = re.search(pattern, text, re.DOTALL)  # re.DOTALL 使得 . 匹配包括换行符在内的任意字符
    #
    # if match:
    #     # 提取匹配到的文本，并去除前面的“Answer:”和可能的前导空白字符
    #     extracted_text = match.group(1).strip()
    #     print(extracted_text)
    # else:
    #     extracted_text = ''
    #     print("No match found.")
    # 正则表达式匹配"Answer:"和"Action:"之间的内容
    pattern = r"Answer:(.*?)Action:"
    matches = re.findall(pattern, text_action, re.DOTALL)

    if len(matches) >1:
        # 为每个匹配的部分添加换行符和数字顺序标识
        formatted_matches = "\n\n".join([f"{i + 1}. {match.strip()}" for i, match in enumerate(matches)])
    elif len(matches) == 0:
        formatted_matches = text
    else:
        formatted_matches = matches[0].strip()

    print(f"\n\nformatted_matches: {formatted_matches}")

    return formatted_matches



