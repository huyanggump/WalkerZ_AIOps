# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/10/31

import os
from typing import Dict, Optional

import pandas as pd
import requests
from modelscope_agent.constants import ApiNames
from modelscope_agent.tools.base import BaseTool, register_tool
from modelscope_agent.utils.utils import get_api_key
from ali_ecs_base import ecs_dir_query, ecs_instance_info, ecs_script_execu


@register_tool('query_ecs_info')
class QueryECSInfo(BaseTool):
    description = '查询阿里云ecs实例的实例信息'
    name = 'query_ecs_info'
    parameters: list = [{
        'name': 'eip_addresses',
        'type': 'list',
        'description': '用户所指定要查询实例的EIP，用户可以一次输入多个EIP，你需要自动使用","分隔，如果用户未指定，则赋值为None',  # 城市/区具体名称，如`北京市海淀区`请描述为`海淀区`
        'required': True
    }]

    def __init__(self, cfg: Optional[Dict] = None):
        super().__init__(cfg)
        self.info_query_obj = ecs_instance_info.ECSInstanceInfo()

    def call(self, params: str, **kwargs) -> str:
        params = self._verify_args(params)
        if isinstance(params, str):
            return 'Parameter Error'

        eip_addresses = params['eip_addresses']
        print(f"\nregister_tool eip_addresses: {eip_addresses}")
        self.info_query_obj.eip_addresses = eip_addresses
        info_response = self.info_query_obj.get_instance_info()
        return info_response







