# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from base.CheckinBase import CheckinBase
from common.ObjectMap import ObjectMap


class CheckinPage(CheckinBase, ObjectMap):

    def click_receive_button(self, driver):
        """
        点击首页领取按钮
        :return:
        """
        button_xpath = self.receive_button()
        return self.element_click(driver, By.XPATH, button_xpath)

    def click_checkin_button(self, driver):
        """
        点击领取金币按钮
        :param driver:
        :return:
        """
        button_xpath = self.checkin_button()
        return self.element_click(driver, By.XPATH, button_xpath)


