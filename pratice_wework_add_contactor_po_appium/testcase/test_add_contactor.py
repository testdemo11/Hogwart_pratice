# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import pytest
import yaml

from pratice_demo.pratice_wework_add_contactor_po_appium.page.app import App


class TestAddContactor:
    def setup(self):
        self.app = App()
    @pytest.mark.parametrize('name,number', yaml.safe_load(open('../datas/contact.yaml', encoding='utf-8')))
    def test_add_contactor(self,name,number):
        toast = self.app.start().goto_main().goto_contactor().goto_add_contactor().goto_add_contactor_info().add_contactor_info(name,number)
        assert '添加成功' == toast