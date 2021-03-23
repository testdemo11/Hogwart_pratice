# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from selenium.webdriver.common.by import By

from pratice_demo.pratice_wework_delete_contactor_po_appium.basepage import BasePage
from pratice_demo.pratice_wework_delete_contactor_po_appium.page.contactor import Contactor


class Main(BasePage):
    def goto_contactor(self):
        self.step('../data/mainpage.yaml','goto_contactor')
        return Contactor(self.driver)