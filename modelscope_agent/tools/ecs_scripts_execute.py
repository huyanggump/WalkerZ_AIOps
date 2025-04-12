# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/11/2

import os
from typing import Dict, Optional
from modelscope_agent.tools.base import BaseTool, register_tool
from modelscope_agent.utils.utils import get_api_key
from ali_ecs_base import ecs_dir_query, ecs_script_execu


@register_tool('ecs_scripts_execute')
class EcsScriptsExecute(BaseTool):
    description = '执行阿里云ECS实例上的sh脚本文件，如果用户未指定或者提供错误的脚本文件路径，则调用ecs_directory_query工具查询目录文件，然后展示给用户'
    name = 'ecs_scripts_execute'
    parameters: list = [{
        'name': 'hostname',
        'type': 'string',
        'description': '用户所指定要执行sh脚本文件的目标实例的IP',  # 城市/区具体名称，如`北京市海淀区`请描述为`海淀区`
        'required': True
    },
    {
        'name': 'script_path',
        'type': 'string',
        'description': '用户所指定要执行的目标实例上的sh脚本文件的文件路径',  # 城市/区具体名称，如`北京市海淀区`请描述为`海淀区`
        'required': True
    }
    ]

    def __init__(self, cfg: Optional[Dict] = None):
        super().__init__(cfg)

    def call(self, params: str, **kwargs) -> str:
        params = self._verify_args(params)
        if isinstance(params, str):
            return 'Parameter Error'

        hostname = params['hostname']
        script_path = params['script_path']
        # print(f"\nregister_tool eip_addresses: {eip_addresses}")
        result, errors_text = ecs_script_execu.execute_remote_script(hostname, script_path)
        if not errors_text:
            return "执行成功！"
        else:
            return f"执行失败！错误信息：{errors_text}"







