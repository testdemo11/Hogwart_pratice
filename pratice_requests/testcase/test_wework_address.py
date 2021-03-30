# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import pytest

from pratice_demo.pratice_requests.wework.wework import Address


class TestAddress:
    def setup(self):
        self.address = Address()
        self.user_id = 'zhangsan00123'
        self.name = '张三'
        self.mobile = '+86 13800022222'
        self.department = [1]

    @pytest.mark.parametrize("user_id,mobile", [['zhangsan00121', '+86 13800021112'],
                                                ['zhangsan00124', '+86 13800022222'],
                                                ['zhangsan00125', '+86 13800022332'],
                                                ['zhangsan00126', '+86 13800022442'],
                                                ])
    def test_create_member(self, user_id, mobile):
        # 数据清洗
        self.address.delete_member(user_id)
        r = self.address.create_member(user_id, self.name, mobile, self.department)
        # get不会抛异常,代替r.json()['errmsg']
        assert r.get('errmsg') == "created"
        r = self.address.get_member_info(user_id)
        # 处理数据，防止数据冗余
        self.address.delete_member(user_id)
        assert r.get('name') == self.name

    def test_delete_member(self):
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.delete_member(self.user_id)
        assert r.get('errmsg') == "deleted"
        r = self.address.get_member_info(self.user_id)
        assert "userid not found" in r.get('errmsg')

    def test_update_member(self):
        # 保证一定是新创建的成员
        self.address.delete_member(self.user_id)
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        new_name = self.name + 'tmp'
        # 修改的名字传给update_member
        r = self.address.update_member(self.user_id, new_name, self.mobile, self.department)
        assert r.get('errmsg') == "updated"
        r = self.address.get_member_info(self.user_id)
        self.address.delete_member(self.user_id)
        assert r.get('name') == new_name

    def test_get_member_info(self):
        self.address.delete_member(self.user_id)
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.get_member_info(self.user_id)
        self.address.delete_member(self.user_id)
        assert r.get('errmsg') == 'ok'
        assert r.get('name') == self.name
