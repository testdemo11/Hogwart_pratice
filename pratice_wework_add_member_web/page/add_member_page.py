# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import allure
from selenium.webdriver.common.by import By

from pratice_demo.pratice_wework_add_member_web.page.base_page import BasePage


class AddMemberPage(BasePage):
    @allure.story("添加联系人")
    def add_member(self, username, account, phonenum):
        """
        添加联系人，详细信息
        :return:
        """

        with allure.step(f'输入用户名:{username}'):
            self.find(By.ID, 'username').send_keys(username)
        with allure.step(f'输入账号:{account}'):
            self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        with allure.step(f'输入手机号:{phonenum}'):
            self.find(By.ID, 'memberAdd_phone').send_keys(phonenum)
        # 点击保存，页面上有多个相同属性的元素，通过find_element找到的是第一个元素
        with allure.step('点击保存'):
            self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return True

    @allure.story("联系人的列表")
    def get_member(self):
        """
        获取所有联系人姓名
        """
        with allure.step("等待保存成功返回联系人界面"):
            self.wait((By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)'))
        with allure.step("找到所有联系人的姓名对应的元素"):
            eles_list = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        names = []
        with allure.step("找到对应姓名的title"):
            for ele in eles_list:
                names.append(ele.get_attribute('title'))
        return names
