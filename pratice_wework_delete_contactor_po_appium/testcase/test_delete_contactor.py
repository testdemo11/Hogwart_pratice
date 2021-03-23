# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_demo.pratice_wework_delete_contactor_po_appium.app import App


class TestDeleteContactor:
    def setup(self):
        self.app = App()

    def test_delete_contactor(self):
        username = 'tt'
        page = self.app.start().goto_main().goto_contactor().goto_search()
        ele_before = page.get_search_contactor_num(username)
        ele_after = page.goto_info().goto_edit_contactor().goto_delete().delete_contactor()
        assert len(ele_before) - len(ele_after) == 1
