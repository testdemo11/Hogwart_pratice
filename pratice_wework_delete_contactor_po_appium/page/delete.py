# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from pratice_demo.pratice_wework_delete_contactor_po_appium.basepage import BasePage


class Delete(BasePage):
    def delete_contactor(self):
        self.step('../data/delete.yaml', 'delete_contactor')
        # 获取删除一个联系人后联系人的数目
        # self.elements_after = self._contactor_num[1]
        # 等待两秒，防止删除的联系人信息还没消失
        sleep(2)
        self.elements_after = self.finds(MobileBy.XPATH,
                                         "//*[@text='联系人']/../..//*[@resource-id='com.tencent.wework:id/avi']")
        return self.elements_after

