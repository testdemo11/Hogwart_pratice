# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium.webdriver.common.mobileby import MobileBy

from pratice_demo.pratice_wework_add_contactor_po_appium.page.basepage import BasePage
from pratice_demo.pratice_wework_add_contactor_po_appium.page.contactor_page import ContactorPage


class InformationPage(BasePage):
    """
    点击通讯录，跳到联系人界面
    """
    def goto_contactor(self):
        # 点击通讯录
        self.step('../datas/information_page.yaml')
        return ContactorPage(self.driver)