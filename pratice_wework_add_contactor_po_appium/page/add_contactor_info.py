# -*- coding:utf-8 -*-
__author__ = 'Tnew'


from pratice_demo.pratice_wework_add_contactor_po_appium.page.basepage import BasePage


class AddContactorInfo(BasePage):
    """
    添加联系人：
    输入用户名
    选择性别女
    输入手机号
    点击保存
    通过获取toast的text来判断是否保存成功
    """
    def add_contactor_info(self,name,number):
        #获取name，number的值，给后面的动态取值提供值
        self._params['username'] = name
        self._params['phonenumber'] = number
        #toast变量接收toast文本信息，通过return返回的值
        toast = self.step('../datas/add_contactor_info.yaml')
        #将值返回，一定要加return,不然默认返回None
        return toast



