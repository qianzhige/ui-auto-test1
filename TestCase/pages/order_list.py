#! /usr/bin/env python
# -*- coding: utf-8 -*-

class order_list():
    def __init__(self,base):
        self.base = base
    #订单列表超链接
    order_list_a = "//label[contains(text(),'订单状态：')]/following-sibling::div//input"
    #订单状态下拉框
    order_status_a = '''//label[contains(text(),'订单状态：')]/following-sibling::div//input'''
    #待发货选项
    to_be_delivered = '''//span[contains(text(),'待发货')]'''
    #查询搜索按钮
    query_search = '''//span[contains(text(),'查询搜索')]'''
    #订单发货按钮
    order_delivery = '''//tbody/tr[1]/td[10]//span[contains(text(),'订单发货')]'''
    def click_order_list_a(self):
        self.base.click("点击订单列表超链接",self.order_list_a)
    def click_order_status_a(self):
        self.base.click("点击订单状态下拉框",self.order_status_a)
    def click_to_be_delivered(self):
        self.base.click("点击待发货选项",self.to_be_delivered)
    def click_query_search(self):
        self.base.click("点击查询搜索按钮",self.query_search)
    def click_order_delivery(self):
        self.base.click("点击订单发货按钮",self.order_delivery)




