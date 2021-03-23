# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium.webdriver.common.mobileby import MobileBy

from pratice_demo.pratice_wework_add_contactor_po_appium.page.add_contactor_page import AddContactorPage
from pratice_demo.pratice_wework_add_contactor_po_appium.page.basepage import BasePage



class ContactorPage(BasePage):
    def goto_add_contactor(self):
        """
        滑动到添加成员并点击
        跳转到添加联系人界面
        :return:
        """
        # 滑动到添加成员并点击
        self.step("../datas/contact_page.yaml")
        return AddContactorPage(self.driver)
