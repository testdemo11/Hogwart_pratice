# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium.webdriver.common.mobileby import MobileBy

from pratice_demo.pratice_wework_delete_contactor_po_appium.basepage import BasePage
from pratice_demo.pratice_wework_delete_contactor_po_appium.conftest import logger
from pratice_demo.pratice_wework_delete_contactor_po_appium.page.info import Info
import logging


class Search(BasePage):
    def get_search_contactor_num(self,username):
        logger.info(f"输入待删除的用户名：{username}")
        self._params['name'] = username
        # 输入用户名
        self.step('../data/search.yaml','get_search_contactor_num')
        #输入用户名后，获取列举的用户名的数目
        # self.elements_before = self._contactor_num[0]
        # return self.elements_before
        #输入用户名后，获取列举的用户名的数目
        self.elements_before = self.finds(MobileBy.XPATH,"//*[@text='联系人']/../..//*[@resource-id='com.tencent.wework:id/avi']")
        return self.elements_before


    def goto_info(self):
        self.step('../data/search.yaml','goto_info')
        return Info(self.driver)
