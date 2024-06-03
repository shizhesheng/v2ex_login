# -*- coding: utf-8 -*-
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions, FirefoxProfile

options = FirefoxOptions()

options.add_argument("--no-sandbox")
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--user-data-dir=/Users/zhengchunyu/Library/Application Support/Google/Chrome/')


browser = Firefox()
browser.get("https://www.google.com.hk/")