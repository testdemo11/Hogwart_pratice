# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_demo.pratice_xueqiu_search_PO_wrapper.basepage import BasePage


class Search(BasePage):
    def search(self,data):
        self._params["value"] = data
        self.step('../datas/search.yaml')
        assert True