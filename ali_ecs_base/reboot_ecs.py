# coding: utf-8
# @Author: WalkerZ
# @Time: 2024/11/3

import os

from Tea.exceptions import UnretryableException, TeaException
from alibabacloud_tea_openapi.models import Config
from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_util import models as util_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models

# os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'] = 'LTAI5tE9zxV6cmUg4aWwp63P'
# os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'] = 'KC7b5l1zvdTwUotFL5LMwX1CRPDGAM'


class RebootECS:
    def __init__(self, instance_id):
        self.instance_id = instance_id

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

    def reboot_ecs_instance(self):
        client = RebootECS.create_client()
        # 构造请求对象
        reboot_instances_request = ecs_20140526_models.RebootInstanceRequest(
            instance_id=self.instance_id,
        )
        # 设置运行时参数
        runtime = util_models.RuntimeOptions()
        try:
            # 调用 RebootInstanceRequest 接口
            reboot_instance_response = client.reboot_instance_with_options(reboot_instances_request, runtime)
            print(reboot_instance_response.body)
            return reboot_instance_response.body
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


# reboot = RebootECS(instance_id='i-bp1e1f8yhdqa7fhbvbs2')
# reboot.reboot_ecs_instance()
#

