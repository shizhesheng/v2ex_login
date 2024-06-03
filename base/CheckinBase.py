# -*- coding: utf-8 -*-

class CheckinBase:

    @staticmethod
    def login_username():
        """
        返回登录页面，用户名定位元素
        :return:
        """
        return '//*[@placeholder="用户名或电子邮件地址"]'

    @staticmethod
    def login_password():
        """
        返回登录页面，密码定位元素
        :return:
        """
        return '//*[@type="password"]'

    @staticmethod
    def login_button():
        """
        返回登录页面，登录按钮元素
        :return:
        """
        return '//*[@type="submit"]'

    @staticmethod
    def receive_button():
        """
        返回首页领取按钮
        :return:
        """
        return '//*[@class="inner"]/*[@href="/mission/daily"]'

    @staticmethod
    def checkin_button():
        """
        领取奖励按钮
        :return:
        """
        return '//*[@class="cell"]/*[@value="领取 X 铜币"]'

