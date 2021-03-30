# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_demo.pratice_requests.wework.base import Base


class Address(Base):

    def create_member(self, user_id, name, mobile, department):
        create_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send_request("POST", url=create_url, json=data)
        return r.json()

    def delete_member(self, user_id):
        # 注意url名字过长，可以把后面携带的参数以params方式写入
        # https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        delete_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        # self.s携带access_token,在BASE类的init方法里面：self.s.params，所以params不用再写access_token
        params = {
            "userid": user_id
        }
        r = self.send_request("GET", url=delete_url, params=params)
        return r.json()

    def update_member(self, user_id, name, mobile, department):
        update_url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send_request("POST", url=update_url, json=data)
        return r.json()

    def get_member_info(self, user_id):
        # 注意url名字过长，可以把后面携带的参数以params方式写入
        # https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        get_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        # self.s携带access_token,在BASE类的init方法里面：self.s.params，所以params不用再写access_token
        params = {
            "userid": user_id
        }
        r = self.send_request("GET", url=get_url, params=params)
        return r.json()
