# ！/user/bin/env/ python
# -*- coding: utf-8 -*-
# @Author : Chao
# @Time : 2023/11/21 20:42
# @File : BasePage.py

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    # 访问网址
    def visit(self, url):
        self.driver.get(url)

    # 元素定位
    def locate(self, locate_type, value):
        element = self.driver.find_element(locate_type, value)
        return element

    # 点击元素
    def click(self, locate_type, value):
        self.locate(locate_type, value).click()

    # 写入文本
    def write_text(self, locate_type, value, text):
        self.locate(locate_type, value).clear()
        self.locate(locate_type, value).send_keys(text)

    # 切换窗口
    def switch_handle(self, index):
        handles = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(handles[index])

    # 切换iframe框架
    def switch_iframe(self, locate_type, value):
        self.driver.switch_to.frame(self.locate(locate_type, value))

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 回车键封装
    def enter(self, locate_type, value):
        self.locate(locate_type, value).send_keys(Keys.ENTER)
