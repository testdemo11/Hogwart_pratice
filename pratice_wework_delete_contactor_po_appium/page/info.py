# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_demo.pratice_wework_delete_contactor_po_appium.basepage import BasePage
from pratice_demo.pratice_wework_delete_contactor_po_appium.page.edit import Edit


class Info(BasePage):
    def goto_edit_contactor(self):
        # 点击更多,进入编辑用户信息界面
        self.step('../data/info.yaml',"goto_edit_contactor")
        return Edit(self.driver)