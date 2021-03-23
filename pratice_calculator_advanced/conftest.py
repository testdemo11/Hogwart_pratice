# -*- coding:utf-8 -*-
__author__ = 'Tnew'

# import sys

import pytest

from pratice_demo.pratice_calculator_advanced.demo.calc import Calculator


# sys.path.append("C:\\Users\\narak\\PycharmProjects\\test2\\pratice_demo")


@pytest.fixture(scope="module")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("计算结束")
