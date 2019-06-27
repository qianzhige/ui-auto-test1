#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pytest
# import requests
from selenium import webdriver

from Common.Baseui import baseUI


@pytest.fixture(scope="session")
def base():
    driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
    # 打开浏览器
    dr = webdriver.Chrome(driver_path)
    dr.maximize_window()  # 最大化浏览器
    dr.implicitly_wait(8)  # 设置隐式时间等待
    # 使用baseUI
    base = baseUI(dr)
    # 打开登录页面
    dr.get('http://192.168.60.132/#/login')
    # 输入用户名
    base.send_keys("输入用户名", '''//input[@name="username"]''', 'admin')
    # 输入密码
    base.send_keys("输入密码", '''//input[@name="password"]''', '123456')
    # 点击登录
    base.click("点击登录", """(//span[contains(text(),'登录')])[1]""")
    assert '首页' in dr.page_source
    # sleep(3)
    yield base
    dr.quit()


# @pytest.fixture(scope="session")
# def token():
#     data = {
#         "password": "123456",
#         "username": "admin"
#     }
#     r = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
#     r_json = r.json()
#     print(r_json)
#     assert 200 == r_json["code"]
#     global token
#     return {"Authorization":r_json["data"]['tokenHead'] + r_json["data"]['token']}


@pytest.fixture(scope="session")
def test_session():
    print('------------------session之前---------------------------')
    yield
    print('------------------session之后---------------------------')

@pytest.fixture(scope="module")
def test_module():
    print('------------------module之前---------------------------')
    yield
    print('------------------module之后---------------------------')
@pytest.fixture(scope="class")
def test_class():
    print('------------------class之前---------------------------')
    yield
    print('------------------class之后---------------------------')

@pytest.fixture(scope="function")
def test_function():
    print('------------------function之前---------------------------')
    yield
    print('------------------function之后---------------------------')
