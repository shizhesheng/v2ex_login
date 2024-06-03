# -*- coding: utf-8 -*-

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from common.yaml_config import GetConf


class DriverConfig:
    def driver_config(self):
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1920,1080')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('detach', True)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('disable-infobars')
        # options.add_argument('--allow-insecure-localhost')
        options.add_argument("--disable-gpu")
        options.add_argument("--user-data-dir=" + GetConf().get_user_data_dir())

        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        return driver


if __name__ == '__main__':
    DriverConfig().driver_config().get("https://www.v2ex.com/")
