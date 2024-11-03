# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/11/3

from typing import Dict, Optional
from modelscope_agent.tools.base import BaseTool, register_tool
from ali_ecs_base import stop_ecs


@register_tool('stop_ecs_tool')
class StopECSTool(BaseTool):
    description = '停止一台阿里云ECS实例，在停止之前需要先调用query_ecs_info工具查询实例ID和实例状态，然后让用户输入想要停止的实例的实例ID，然后执行停止实例操作'
    name = 'stop_ecs_tool'
    parameters: list = [{
        'name': 'instance_id',
        'type': 'string',
        'description': '用户想要停止的目标阿里云ECS实例的实例ID，例如：i-bp1e1f8yhdqa7fhbvbs2，此字段用户必须填写',
        'required': True
    }]

    def __init__(self, cfg: Optional[Dict] = None):
        super().__init__(cfg)
        self.stop_obj = stop_ecs.StopECS(instance_id='')

    def call(self, params: str, **kwargs) -> str:
        params = self._verify_args(params)
        if isinstance(params, str):
            return 'Parameter Error'

        instance_id = params['instance_id']
        print(f"\nregister_tool instance_id: {instance_id}")
        self.stop_obj.instance_id = instance_id
        info_response = self.stop_obj.stop_ecs_instance()
        return info_response







