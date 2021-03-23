# -*- coding:utf-8 -*-
__author__ = 'Tnew'

"""
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
"""

import money


# 定义发工资模块 send_money，用来增加收入计算
def send_money(salary):
    print(f"你未发工资前的存款为{money.saved_money}")
    money.saved_money += salary
    print(f"你发完工资后目前的存款为{money.saved_money}")
    return money.saved_money
