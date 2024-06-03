# -*- coding: utf-8 -*-
import time

from selenium.common.exceptions import WebDriverException, ElementNotVisibleException, StaleElementReferenceException


class ObjectMap:

    def wait_for_ready_state_complete(self, driver, timeout=10):
        """
        等待页面元素加载完成
        :param driver:
        :param timeout:
        :return:
        """
        start_ms = time.time() * 1000
        end_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                ready_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                time.sleep(0.03)
                return True
            if ready_state.lower() == 'complete':
                time.sleep(0.01)

    def element_appear(self, driver, locator_type, locator_value, timeout=30):
        """
        等待页面元素出现
        :param driver:
        :param locator_type:
        :param locator_value:
        :param timeout:
        :return:
        """
        if locator_type:
            start_ms = time.time() * 1000
            end_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locator_type, value=locator_value)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= end_ms:
                        break
                    time.sleep(0.1)
                    pass
            raise ElementNotVisibleException("元素没有出现，定位方式：" + locator_type + "\n定位方式：" + locator_value)
        else:
            pass

    def element_disappear(self, driver, locator_type, locator_value, timeout=30):
        """
        等待页面元素消失
        :param driver:
        :param locator_type:
        :param locator_value:
        :param timeout:
        :return:
        """
        if locator_type:
            start_ms = time.time() * 1000
            end_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locator_type, value=locator_value)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= end_ms:
                        break
                    time.sleep(0.1)
                    pass
            raise Exception("元素没有消失，定位方式：" + locator_type + "\n定位方式：" + locator_value)
        else:
            pass

    def element_click(self,
                      driver,
                      locator_type,
                      locator_expression,
                      locator_type_appear=None,
                      locator_expression_appear=None,
                      locator_type_disappear=None,
                      locator_expression_disappear=None,
                      timeout=30):
        """

        :param timeout:
        :param driver:
        :param locator_type: 定位方式
        :param locator_expression: 定位表达式
        :param locator_type_appear: 等待元素消失的定位方式
        :param locator_expression_appear: 等待元素消失的定位表达式
        :param locator_type_disappear: 等待元素显示的定位方式
        :param locator_expression_disappear: 等待元素显示的定位表达式
        :return:
        """
        element = self.element_appear(
            driver=driver,
            locator_type=locator_type,
            locator_value=locator_expression,
            timeout=timeout
        )
        try:
            element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.08)
            element = self.element_appear(
                driver=driver,
                locator_type=locator_type,
                locator_value=locator_expression,
                timeout=timeout
            )
            element.click()
        except Exception as e:
            print("页面出现异常，元素不可点击", e)
            return False
        try:
            # 点击元素后，元素的出现和消失
            self.element_appear(
                driver,
                locator_type_appear,
                locator_expression_appear
            )
            self.element_disappear(
                driver,
                locator_type_disappear,
                locator_expression_disappear
            )
        except Exception as e:
            print("等待元素消失或出现失败", e)
            return False

    def element_click(self,
                      driver,
                      locator_type,
                      locator_expression,
                      locator_type_appear=None,
                      locator_expression_appear=None,
                      locator_type_disappear=None,
                      locator_expression_disappear=None,
                      timeout=30):
        """

        :param timeout:
        :param driver:
        :param locator_type: 定位方式
        :param locator_expression: 定位表达式
        :param locator_type_appear: 等待元素消失的定位方式
        :param locator_expression_appear: 等待元素消失的定位表达式
        :param locator_type_disappear: 等待元素显示的定位方式
        :param locator_expression_disappear: 等待元素显示的定位表达式
        :return:
        """
        element = self.element_appear(
            driver=driver,
            locator_type=locator_type,
            locator_value=locator_expression,
            timeout=timeout
        )
        try:
            element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.08)
            element = self.element_appear(
                driver=driver,
                locator_type=locator_type,
                locator_value=locator_expression,
                timeout=timeout
            )
            element.click()
        except Exception as e:
            print("页面出现异常，元素不可点击", e)
            return False
        try:
            self.element_appear(
                driver,
                locator_type_appear,
                locator_expression_appear
            )
            self.element_disappear(
                driver,
                locator_type_disappear,
                locator_expression_disappear
            )
        except Exception as e:
            print("等待元素消失或出现失败", e)
            return False