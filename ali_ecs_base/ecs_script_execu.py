# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/11/1

import paramiko


user_name = "root"
password = "985211WalkerZ*"
port = 22
host_name = "8.154.41.113"
script_path = "/sh_scripts/transformer_api.sh"


def execute_remote_script(hostname, port, username, password, script_path):
    # 创建SSH客户端
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 连接到远程ECS实例
        client.connect(hostname, port=port, username=username, password=password)

        # 执行sh脚本
        stdin, stdout, stderr = client.exec_command(f"bash {script_path}")
        output = stdout.read().decode()
        errors = stderr.read().decode()

        print("Output:", output)
        print("Errors:", errors)
    finally:
        client.close()


# # 调用
# execute_remote_script(host_name, port, user_name, password, script_path)
