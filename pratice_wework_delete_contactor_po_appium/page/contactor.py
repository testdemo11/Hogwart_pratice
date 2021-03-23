# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_demo.pratice_wework_delete_contactor_po_appium.basepage import BasePage
from pratice_demo.pratice_wework_delete_contactor_po_appium.page.search import Search


class Contactor(BasePage):
    def goto_search(self):
        # 点击搜索
        self.step('../data/contactor.yaml','goto_search')
        return Search(self.driver)
