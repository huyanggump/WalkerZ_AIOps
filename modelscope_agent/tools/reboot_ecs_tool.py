# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/11/3

import os
from typing import Dict, Optional
from modelscope_agent.tools.base import BaseTool, register_tool
from modelscope_agent.utils.utils import get_api_key
from ali_ecs_base import reboot_ecs


@register_tool('reboot_ecs_tool')
class RebootECSTool(BaseTool):
    description = '重启一台阿里云ECS实例，在重启之前需要先调用query_ecs_info工具查询实例ID和实例状态，然后让用户输入想要重启的实例的实例ID，然后再进一步判断：如果实例状态为运行中（Running），才能调用此工具重启实例，否则告诉用户实例状态不是运行中，无法重启'
    name = 'reboot_ecs_tool'
    parameters: list = [{
        'name': 'instance_id',
        'type': 'string',
        'description': '用户想要重启的目标阿里云ECS实例的实例ID，例如：i-bp1e1f8yhdqa7fhbvbs2，此字段用户必须填写',
        'required': True
    }]

    def __init__(self, cfg: Optional[Dict] = None):
        super().__init__(cfg)
        self.reboot_obj = reboot_ecs.RebootECS(instance_id='')

    def call(self, params: str, **kwargs) -> str:
        params = self._verify_args(params)
        if isinstance(params, str):
            return 'Parameter Error'

        instance_id = params['instance_id']
        print(f"\nregister_tool instance_id: {instance_id}")
        self.reboot_obj.instance_id = instance_id
        info_response = self.reboot_obj.reboot_ecs_instance()
        return info_response







