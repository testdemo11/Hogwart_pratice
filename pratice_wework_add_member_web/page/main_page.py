# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import allure
from selenium.webdriver.common.by import By
from pratice_demo.pratice_wework_add_member_web.page.add_member_page import AddMemberPage
from pratice_demo.pratice_wework_add_member_web.page.base_page import BasePage


# 企业微信的主页面
class MainPage(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    @allure.story('点击添加联系人，跳到添加页面')
    def goto_add_member(self):
        """
        添加成员
        :return:
        """
        with allure.step('等待添加联系人元素出现'):
            self.wait((By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)'))
        with allure.step('点击添加联系人'):
            self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        # return AddMemberPage()
        return AddMemberPage(self.driver)
