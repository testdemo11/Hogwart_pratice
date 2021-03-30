# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import requests


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def send_request(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)

    def get_token(self):
        SECRET = 'd8ZdcI76eHMi2oL2qJRA_VcwBUjOQoG-YjvAJ4RJF_o'
        ID = 'wwca233d5d5e521b32'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}'
        r = requests.get(url)
        token = r.json()['access_token']
        return token
