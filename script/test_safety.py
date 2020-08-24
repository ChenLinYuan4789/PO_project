import os, sys
sys.path.append(os.getcwd())
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from base.base_driver import init_driver
from page.safety_page import SafetyPage

class TestSafety():

    def setup(self):
        self.driver = init_driver()
        self.safety_page = SafetyPage(self.driver)

    def test_po3(self):
        # 分离测试脚本后：
        # 点击"指纹"
        sleep(1)
        self.safety_page.click_fingerprint()
        sleep(1)
        # 点击已保存的指纹
        self.safety_page.click_fingerprintName()
        # 点击重命名
        self.safety_page.click_rename()
        # 清除原有的指纹名称
        self.safety_page.clear_fingerprintName()
        # 输入新的指纹名称
        self.safety_page.send_fingerprintNewName("hello")
        # 点击确定按钮
        self.safety_page.click_confirm()
        # 点击返回
        self.safety_page.click_back()



        # 分离测试脚本前：
        # driver = self.driver
        # driver.find_element_by_xpath("//*[contains(@text, '指纹')]").click()
        # sleep(1)
        # TouchAction(driver).tap(x=525, y=833).perform()
        # WebDriverWait(driver, 10, 1).until(lambda x:x.find_element_by_id("com.android.settings:id/OKBtn")).click()
        # sleep(1)
        # driver.find_element_by_id("com.android.settings:id/edit").clear()
        # driver.find_element_by_id("com.android.settings:id/edit").send_keys("hello")
        # driver.find_element_by_xpath("//*[contains(@text, '确定')]").click()
        # sleep(1)
        # driver.keyevent(4)
