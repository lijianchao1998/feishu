# ！/user/bin/env/ python
# -*- coding: utf-8 -*-
# @Author : Chao
# @Time : 2023/11/21 20:55
# @File : LoginPage.py

from time import sleep
from BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class OperatePage(BasePage):
    feishu_url = 'https://www.feishu.cn/'
    loginButton = ('xpath', "//a[text()='登录']")  # 登录按钮元素
    advertising_closure = ('xpath', '//div[@data-elem-id="MC2ANWQ36m"]')  # 广告关闭按钮元素
    account_switch = ('xpath', '//span[@class="universe-icon switch-icon"]')  # 登录切换按钮元素
    account = ('xpath', '//input[@name="mobile_input"]')  # 账号输入框元素
    password = ('xpath', '//input[@data-test="login-pwd-input"]')  # 密码输入框元素
    agree_box = ('xpath', '//input[@class="ud__checkbox__input"]')  # 同意框元素
    phone_next_btn = ('xpath', '//button[@data-test="login-phone-next-btn"]')  # 输入账号后的下一步元素
    pwd_next_btn = ('xpath', '//button[@data-test="login-pwd-next-btn"]')  # 输入密码后的下一步元素

    product_list = ('xpath', '//div[@class="headerExtra_productList"]')  # 菜单图标元素
    message = ('xpath', '//div[@title="消息"]')  # 消息图标元素
    quick_jump_enter_box = ('xpath', '//div[@class="quick-jump-enter-com__box"]')  # 消息搜索框
    quink_jump_input = ('xpath', '//input[@class="quickJump_input"]')  # 搜索输入框元素
    jumpitem = ('xpath', '//div[@class="jumpItem jumpItem-active"]')
    lark_empty = ('xpath', '//*[@class="lark-editor lark-empty"]')  # 消息输入框元素
    lark_editor = ('xpath', '//*[@class="lark-editor"]')  # 填写信息后的输入框元素

    def login(self, uname, pwd):
        # self = LoginPage(driver=driver)  # 实例化
        self.visit(self.feishu_url)  # 访问飞书网址
        self.click(*self.advertising_closure)  # 关闭广告
        self.click(*self.loginButton)  # 切换登录方式为账号登录
        sleep(2)
        self.click(*self.account_switch)  # 切换为账号密码登录
        self.write_text(*self.account, uname)  # 账号输入框
        self.click(*self.agree_box)  # 勾选同意框
        self.click(*self.phone_next_btn)  # 点击下一步
        self.write_text(*self.password, pwd)  # 输入密码
        self.click(*self.pwd_next_btn)  # 点击下一步

    def send_message(self, interlocutors='test2'):
        self.click(*self.product_list)  # 点击菜单按钮
        self.click('xpath', '//div[@title="消息"]')  # 点击消息图标
        self.switch_handle(-1)
        self.click(*self.quick_jump_enter_box)  # 点击消息搜索框
        self.write_text(*self.quink_jump_input, interlocutors)  # 在搜索框输入内容
        self.click(*self.jumpitem)
        sleep(2)
        self.write_text(*self.lark_empty, '发送一条信息')  # 在消息输入框输入内容
        self.enter(*self.lark_editor)  # 回车发送信息
        sleep(5)
        self.quit()




