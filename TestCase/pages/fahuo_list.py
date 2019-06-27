#! /usr/bin/env python
# -*- coding: utf-8 -*-

class fahuo_list():

    def __init__(self,base):
        self.base = base
    #物流公司
    logistics_company = "//tbody/tr[1]/td[6]//input"
    #圆通快递
    ytkd = "//span[contains(text(),'圆通')]"
    #物流单号
    wldh = '''//tbody/tr[1]/td[7]//input'''
    #确定
    qd = '''//span[contains(text(),'确定')]'''
    #接受
    accept = '''//div[@role="dialog"]//span[contains(text(),'确定')]'''
    #提示
    ts = """//div[@role="alert"]//p"""

    def click_logistics_company(self):
        self.base.click("点击物流公司",self.logistics_company)
    def click_ytkd(self):
        self.base.click("点击圆通快递",self.ytkd)
    def send_keys_wldh(self,text):
        self.base.send_keys("输入物流单号", self.wldh, text)
    def click_qd(self):
        self.base.click("点击确定",self.qd)
    def click_accept(self):
        self.base.click('点击确认',self.accept)
    def get_text_ts(self):
        return self.base.get_text("获取提示文本", self.ts)
