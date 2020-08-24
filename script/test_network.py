import os, sys
sys.path.append(os.getcwd())
from appium import webdriver
from base.base_driver import init_driver
from page.network_page import NetWork

class TestNetWork():

    def setup(self):
        self.driver = init_driver()
        self.network_page = NetWork(self.driver)

    def test_po1(self):
        # 分离测试脚本后：
        # 点击"仅限充电时"
        self.network_page.click_recharge()



        # 分离测试脚本前：
        # driver = self.driver
        # driver.find_element_by_xpath("//*[contains(@text, 'WLAN')]").click()
        # WebDriverWait(driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@content-desc, '更多选项')]")).click()
        # WebDriverWait(driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@text, '高级')]")).click()
        # WebDriverWait(driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@text, '保持WLAN')]")).click()
        # WebDriverWait(driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@text, '仅限充电时')]")).click()

    def test_po2(self):
        # 分离测试脚本后：
        # 点击"始终"
        self.network_page.click_always()


        # 分离测试脚本前：
        # driver = self.driver
        # driver.find_element_by_xpath("//*[contains(@text, 'WLAN')]").click()
        # WebDriverWait(driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@content-desc, '更多选项')]")).click()
        # WebDriverWait(driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@text, '高级')]")).click()
        # WebDriverWait(driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@text, '保持WLAN')]")).click()
        # WebDriverWait(driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@text, '始终')]")).click()











