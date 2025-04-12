# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/11/3

from typing import Dict, Optional
from modelscope_agent.tools.base import BaseTool, register_tool
from ali_ecs_base import start_ecs


@register_tool('start_ecs_tool')
class StartECSTool(BaseTool):
    description = '启动一台阿里云ECS实例，在启动之前需要先调用query_ecs_info工具查询实例ID和实例状态，然后让用户输入想要启动的实例的实例ID，然后再进一步判断：如果实例状态为已停止（Stopped），才能调用此工具启动实例，否则告诉用户实例状态不是已停止，无法启动'
    name = 'start_ecs_tool'
    parameters: list = [{
        'name': 'instance_id',
        'type': 'string',
        'description': '用户想要启动的目标阿里云ECS实例的实例ID，例如：i-bp1e1f8yhdqa7fhbvbs2，此字段用户必须填写',
        'required': True
    }]

    def __init__(self, cfg: Optional[Dict] = None):
        super().__init__(cfg)
        self.start_obj = start_ecs.StartECS(instance_id='')

    def call(self, params: str, **kwargs) -> str:
        params = self._verify_args(params)
        if isinstance(params, str):
            return 'Parameter Error'

        instance_id = params['instance_id']
        print(f"\nregister_tool instance_id: {instance_id}")
        self.start_obj.instance_id = instance_id
        info_response = self.start_obj.start_ecs_instance()
        return info_response







