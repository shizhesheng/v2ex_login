# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

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
options.add_argument("--user-data-dir=/Users/zhengchunyu/Library/Application Support/Google/Chrome/")
options.add_argument("--no-sandbox")
# options.add_argument('--remote-debugging-pipe')
# options.add_argument("--remote-debugging-port=6666")
# options.add_argument("ChromeOptions=CAPABILITY_W3C")


# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-extensions")
#
# options.add_argument("--headless")
# options.add_argument("--blink-settings=imagesEnabled=false")
#
# options.add_argument('--verbose')
# options.add_argument('--no-sandbox')
# # options.add_argument('--headless')
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--remote-debugging-port=9014')
# options.add_argument('--disable-extensions')
# options.add_argument('--disable-gpu')
# options.add_argument("--disable-extensions")
#
# options.add_argument("--disable-popup-blocking")
#
# options.add_argument("--profile-directory=Default")
#
# options.add_argument("--ignore-certificate-errors")
#
# options.add_argument("--disable-plugins-discovery")
#
# options.add_argument("--incognito")
# options.add_argument('--user-data-dir=/Users/zhengchunyu/Library/Application Support/Google/Chrome/')
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option('detach', True)
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

time.sleep(3)
driver.get("https://www.v2ex.com")
time.sleep(3)
driver.find_element(By.XPATH, '//*[@class="inner"]/*[@href="/mission/daily"]').click()
driver.implicitly_wait(30)
driver.find_element(By.XPATH, '//*[@class="cell"]/*[@value="领取 X 铜币"]').click()

# time.sleep(2)
# print(driver.current_url)
# driver.find_element(By.XPATH, '//*[@jsname="MBVUVe"]').click()
# driver.implicitly_wait(60)

# //*[@class="inner"]/*[@href="/mission/daily"]
# driver.find_element(By.XPATH, '//*[@class="inner"]/*[@href="/mission/daily"]')
print(driver.current_url)
