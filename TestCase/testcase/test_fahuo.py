#! /usr/bin/env python
# -*- coding: utf-8 -*-
from TestCase.pages.fahuo_list import fahuo_list
from TestCase.pages.order_list import order_list


class Test_fahuo():

    def test_fahuo(self,base):
        base.driver.get("http://192.168.60.132/#/oms/order")
        # 初始化页面对象
        orders = order_list(base)
        # 点击订单状态
        orders.click_order_status_a()
        # 点击待发货
        orders.click_to_be_delivered()
        # 点击查询搜索
        orders.click_query_search()
        # 点击第一笔订单的订单发货
        orders.click_order_delivery()
        assert "发货列表" in base.driver.page_source
        #初始化发货列表页面
        fahuo = fahuo_list(base)
        # 点击物流公司
        fahuo.click_logistics_company()
        # 选择圆通快递
        fahuo.click_ytkd()
        # 输入物流单号
        fahuo.send_keys_wldh("12357890")
        # 点击确定
        fahuo.click_qd()
        # 点击确定
        fahuo.click_accept()
        # 获取提示文本
        text = fahuo.get_text_ts()
        # 断言
        assert "发货成功" in text