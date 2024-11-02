# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/11/2

import os
from typing import Dict, Optional
from modelscope_agent.tools.base import BaseTool, register_tool
from modelscope_agent.utils.utils import get_api_key
from ali_ecs_base import ecs_dir_query


@register_tool('ecs_directory_query')
class EcsDirectoryQuery(BaseTool):
    description = '查询用户指定的阿里云ECS实例上指定目录下的所有子目录和文件'
    name = 'ecs_directory_query'
    parameters: list = [{
        'name': 'hostname',
        'type': 'string',
        'description': '用户所指定要查询目录文件的目标实例的IP，此字段用户必须提供，不得默认填写',
        'required': True
    },
    {
        'name': 'directory_path',
        'type': 'string',
        'description': '用户所指定要查询的目录路径，如果用户未提供，则默认为"/"路径',
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
        directory_path = params['directory_path']
        # print(f"\nregister_tool eip_addresses: {eip_addresses}")
        result = ecs_dir_query.list_remote_directory(hostname, directory_path)
        return result











