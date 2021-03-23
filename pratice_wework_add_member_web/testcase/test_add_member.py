import os

import allure
import pytest
import yaml

from pratice_demo.pratice_wework_add_member_web.page.main_page import MainPage


@allure.feature('测试添加联系人的用例，看添加的姓名是否添加成功')
class TestAddMember:
    def setup(self):
        self.main_page = MainPage()

    @allure.story("传入用户名，账号，手机号三个参数，测试是否添加联系人成功")
    @pytest.mark.parametrize('username, account, phonenum',
                             yaml.safe_load(open('../data/contact.yaml', encoding='utf-8')),
                             ids=['user1', 'user2', 'user3'])
    def test_add_member(self, username, account, phonenum):
        page = self.main_page.goto_add_member()
        page.add_member(username, account, phonenum)
        names = page.get_member()
        assert username in names
