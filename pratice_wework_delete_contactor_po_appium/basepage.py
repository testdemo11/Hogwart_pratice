# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from time import sleep
from typing import List

import yaml
from appium.webdriver.common.mobileby import MobileBy
import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import json

from pratice_demo.pratice_wework_delete_contactor_po_appium.conftest import logger


class BasePage:
    _params = {}
    # 黑名单
    _black_list = [(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gu_"]')]
    # 黑名单查找最大次数
    _error_max = 3
    # 黑名单查找从0次开始
    _error_num = 0
    # 收集删除联系人前后的名单列表的长度，分别放入列表中
    _contactor_num = []

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def set_implicitly_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def find(self, by, locator=None):
        logger.info(f"find: by = {by},locator = {locator}")
        try:
            element = self.driver.find_element(by, locator)
            self._error_num = 0
            self.set_implicitly_wait(10)
            return element
        except Exception as e:
            logger.info("进入黑名单处理")
            self.driver.get_screenshot_as_file('../report/error.png')
            self.set_implicitly_wait(3)
            if self._error_num > self._error_max:
                self._error_num = 0
                self.set_implicitly_wait(10)
                raise e
            self._error_num += 1
            for black in self._black_list:
                eles = self.finds(*black)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(by, locator)
            raise e

    def finds(self, by, locator=None):
        return self.driver.find_elements(by, locator)

    def find_click(self, by, locator):
        return self.find(by, locator).click()

    def send(self, by, locator, value):
        return self.find(by, locator).send_keys(value)

    def swipe_click(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().'
                                        'scrollable(true).instance(0)).'
                                        f'scrollIntoView(new UiSelector().text("{text}").'
                                        'instance(0));').click()

    def wait(self, by, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((by, locator)))

    def step(self, path, name):
        with open(path, 'r', encoding='utf-8') as f:
            fun = yaml.safe_load(f)
            steps: List[dict] = fun[name]
            # 将python对象转成字符串,序列化
            raw = json.dumps(steps)
            for key, value in self._params.items():
                raw = raw.replace("${" + key + "}", value)
            # 将字符串转成python对象，反序列化
            steps = json.loads(raw)

        for step in steps:
            if step['action'] == "click":
                self.find_click(step['by'], step['locator'])
            elif step['action'] == "swipe_click":
                self.swipe_click(step['locator'])
            elif step['action'] == 'send':
                self.send(step['by'], step['locator'], step['value'])
            elif step['action'] == 'wait':
                self.wait(step['by'], step['locator'])
            # 第二种获取联系人数目的方式
            # elif step['action'] == 'finds':
            #     sleep(3)
            #     eles = self.finds(step['by'],step['locator'])
            #     self._contactor_num.append(len(eles))
            #     print(self._contactor_num)
            #     return self._contactor_num
