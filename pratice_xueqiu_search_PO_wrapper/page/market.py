# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium.webdriver.common.mobileby import MobileBy

from pratice_demo.pratice_xueqiu_search_PO_wrapper.basepage import BasePage
from pratice_demo.pratice_xueqiu_search_PO_wrapper.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.step('../datas/market.yaml')
        return Search(self.driver)
