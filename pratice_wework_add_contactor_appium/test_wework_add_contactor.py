# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from time import sleep

import pytest
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
打开企业微信，
点击通讯录，
点击添加成员，
点击手动输入添加，
输入姓名，性别，手机号并点击保存
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWework:
    def setup(self):
        desire_caps = {
            "platformName": 'android',
            "deviceName": '127.0.0.0:7555',
            "appPackage": 'com.tencent.wework',
            "appActivity": 'com.tencent.wework.launch.WwMainActivity',
            "noReset": 'true',
            'settings[waitForIdleTimeout]': 0,
            "ChromedriverExecutable": "D:/Study/Automation_Tester_Guide/Lesson6_appium/chromedriver"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 通过yaml文件给姓名，性别，手机号传参，注意有中文，添加encoding='utf-8'
    @pytest.mark.parametrize('name,gender,number', yaml.safe_load(open('./data/data.yaml', encoding='utf-8')))
    def test_wework(self, name, gender, number):
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 滑动到添加成员并点击
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        # 点击手动输入添加
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()

        # 输入姓名
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys(name)

        # 点击男弹出男女选择
        self.driver.find_element_by_xpath("//*[contains(@text,'性别')]/..//*[@text='男']").click()

        # 判断男女弹框是否可见
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[@text='女']")))
        # print(element.is_displayed())
        # 如果“女”元素可见，点击男、女
        if element.is_displayed() == True:
            self.driver.find_element_by_xpath(f"//*[@text='{gender}']").click()
        # 输入手机号
        self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys(number)
        # 点击保存
        self.driver.find_element_by_id("com.tencent.wework:id/gur").click()

        # 获取toast信息,并添加断言判断添加成功
        add = self.driver.find_element_by_xpath("//*[contains(@text,'添加成功')]").text
        assert '添加成功' == add
