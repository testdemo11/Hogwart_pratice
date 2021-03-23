"""
使用cookie登录企业微信，完成导入联系人，加上断言验证
"""
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestCookie:
    def setup(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9224'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_shelve(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        #shelve python 提供的内置模块，相当于小型数据库
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #从数据库中拿cookie
        db = shelve.open("./my_db/cookies")
        # db['cookie'] = cookies
        # db.close()
        cookies= db['cookie']
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        #刷新网页，得到有cookie的网页
        self.driver.refresh()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[2]/div/span[2]").click()
        self.driver.find_element_by_id("js_upload_file_input").send_keys(
            "C:/Users/narak/PycharmProjects/test2/pratice_demo/pratice_cookie_weixin/excel/myname.xlsx")
        assert 'myname.xlsx' == self.driver.find_element_by_id("upload_file_name").text

