# -*- coding: utf-8 -*-
import pytest

from common.yaml_config import GetConf
from config.driver_config import DriverConfig
from page.CheckinPage import CheckinPage


class TestCheckin:

    def test_checkin(self):
        driver = DriverConfig().driver_config()
        driver.get(GetConf().get_url())
        CheckinPage().click_receive_button(driver)
        driver.implicitly_wait(30)
        CheckinPage().click_checkin_button(driver)


if __name__ == '__main__':
    TestCheckin().test_checkin()