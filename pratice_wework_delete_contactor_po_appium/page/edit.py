# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_demo.pratice_wework_delete_contactor_po_appium.basepage import BasePage
from pratice_demo.pratice_wework_delete_contactor_po_appium.page.delete import Delete


class Edit(BasePage):

    def goto_delete(self):
        # 点击编辑成员
        self.step('../data/edit.yaml','goto_delete')
        return Delete(self.driver)