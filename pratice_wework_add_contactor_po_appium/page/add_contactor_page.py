# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_demo.pratice_wework_add_contactor_po_appium.page.add_contactor_info import AddContactorInfo
from pratice_demo.pratice_wework_add_contactor_po_appium.page.basepage import BasePage


class AddContactorPage(BasePage):
    """
    点击手动输入添加
    跳转到添加联系人的添加信息页面
    """
    def goto_add_contactor_info(self):
        # 点击手动输入添加
        self.step('../datas/add_contactor_page.yaml')
        return AddContactorInfo(self.driver)
