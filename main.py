# ！/user/bin/env/ python
# -*- coding: utf-8 -*-
# @Author : Chao
# @Time : 2023/11/21 22:00
# @File : main.py

from OperatePage import OperatePage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # 窗口最大化配置
    driver = webdriver.Chrome(options=chrome_options)  # 传入驱动
    og = OperatePage(driver=driver)
    og.login('15602623870', 'Aa123456789')
    og.send_message()

