# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from typing import List

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find_click(self, locator):
        return self.driver.find_element_by_xpath(locator).click()

    def find_send(self, locator, value):
        return self.driver.find_element_by_xpath(locator).send_keys(value)

    def swipe_click(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().'
                                        'scrollable(true).instance(0)).'
                                        f'scrollIntoView(new UiSelector().text("{text}").'
                                        'instance(0));').click()

    def wait(self, by, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((by, locator)))

    def find_toast(self, locator):
        toast = self.driver.find_element_by_xpath(locator).text
        return toast

    def step(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            steps: List[dict] = yaml.safe_load(f)
        for step in steps:
            if step['action'] == "find_click":
                self.find_click(step['locator'])
            elif step['action'] == "swipe_click":
                self.swipe_click(step['locator'])
            elif step['action'] == 'find_send':
                #step['value'] = {username}, {phonenumber}
                content: str = step['value']
                # 给step['value']赋具体的值
                for param in self._params:
                    """self._params["value"] = value"""
                    content = content.replace("{%s}" % param, self._params[param])
                self.find_send(step['locator'], content)
            elif step['action'] == 'wait':
                self.wait(step['by'], step['locator'])
            elif step['action'] == 'find_toast':
                return self.find_toast(step['locator'])
