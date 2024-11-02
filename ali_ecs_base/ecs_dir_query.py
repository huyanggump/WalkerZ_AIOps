# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/11/2

import paramiko


user_name = "root"
password = "985211WalkerZ*"
port = 22
host_name = "8.154.41.113"
# script_path = "/sh_scripts"


def list_remote_directory(hostname, directory_path):
    # 创建SSH客户端
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 连接到远程服务器
        client.connect(hostname, port=port, username=user_name, password=password)
        if not directory_path:
            directory_path = "/"
        # 执行`ls`命令来列出目录内容
        stdin, stdout, stderr = client.exec_command(f'ls -la {directory_path}')
        output = stdout.read().decode()
        errors = stderr.read().decode()

        if errors:
            print("Errors:", errors)
            return errors
        else:
            print("Directory content:\n", output)
            return output

    finally:
        client.close()


# 调用函数
# list_remote_directory(host_name, port, user_name, password, script_path)
