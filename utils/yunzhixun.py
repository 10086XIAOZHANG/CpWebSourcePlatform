# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 下午12:43
# @Author  : Jimck
# @Email   : jimck_zhang@163.com
# @File    : yunzhixun.py
# @Software: PyCharm Community Edition
import requests
import json


class YunZhiXun(object):
    def __init__(self, token):
        self.single_send_url = "https://open.ucpaas.com/ol/sms/sendsms"
        self.app_id = "*********"
        self.sid = "******"
        self.token = token

    def send_sms(self, templateId, mobile, code, timeout):
        params = {
            "sid": self.sid,
            "token": self.token,
            "appid": self.app_id,
            "templateid": templateId,
            "param": "{code},{timeout}".format(code=code, timeout=timeout),
            "mobile": mobile
        }
        response = requests.post(self.single_send_url, data=json.dumps(params),
                                 headers={"Content-Type": "application/json"})
        return json.loads(response.text)


if __name__ == "__main__":
    yunzhixun = YunZhiXun("76bbf196cc5491bdc341d07d4855253d")
    yunzhixun.send_sms("14699", "17689818889", "201218", "1")
