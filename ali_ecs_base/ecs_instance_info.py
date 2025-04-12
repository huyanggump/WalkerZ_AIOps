# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/11/1

import os

from Tea.exceptions import UnretryableException, TeaException
from alibabacloud_tea_openapi.models import Config
from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_util import models as util_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models


class ECSInstanceInfo:
    def __init__(self, eip_addresses=None):
        self.eip_addresses = eip_addresses if eip_addresses else None

    @staticmethod
    def create_client() -> Ecs20140526Client:
        config = Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'],
            endpoint='ecs.cn-hangzhou.aliyuncs.com'
        )
        return Ecs20140526Client(config)

    def get_instance_info(self):
        client = ECSInstanceInfo.create_client()
        # 构造请求对象
        describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
            region_id='cn-hangzhou',
            eip_addresses = self.eip_addresses
        )
        # 设置运行时参数
        runtime = util_models.RuntimeOptions()
        try:
            # 调用 DescribeInstances 接口
            describe_instances_response = client.describe_instances_with_options(describe_instances_request, runtime)
            print(describe_instances_response.body)
            return describe_instances_response.body
        except UnretryableException as e:
            # 网络异常，此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常
            print(e)
            raise Exception(e)
        except TeaException as e:
            # 业务异常，此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常
            print(e)
            raise Exception(e)
        except Exception as e:
            # 其他异常，此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常
            print(e)
            raise Exception(e)


# if __name__ == '__main__':
#     ecs_info_obj = ECSInstanceInfo(eip_addresses=[''])
#     ecs_info_obj.get_instance_info()
