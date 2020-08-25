from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_action import BaseAction


class NetWork(BaseAction):

    # 抽取元素特征：
    # WLAN按钮
    WLAN_button = By.XPATH, "//*[contains(@text, 'WLAN')]"
    # 更多按钮
    more_button = By.XPATH, "//*[contains(@content-desc, '更多选项')]"
    # 高级按钮
    advanced_button = By.XPATH, "//*[contains(@text, '高级')]"
    # WLAN状态选项
    state_button = By.XPATH, "//*[contains(@text, '保持WLAN')]"
    # WLAN仅限充电状态
    WLAN_recharge_button = By.XPATH, "//*[contains(@text, '仅限充电时')]"
    # WLAN始终连接状态
    WLAN_always_button = By.XPATH, "//*[contains(@text, '始终')]"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        # 当所有的测试脚本执行前都要进入同一个界面时，可以在__init__函数中一起调用，如下：
        # 点击WLAN
        self.click_WLAN()
        # 点击"更多"按钮
        self.click_more()
        # 点击"高级"按钮
        self.click_advanced()
        # 点击WLAN状态
        self.click_state()

    def click_WLAN(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, 'WLAN')]").click()
        # 查找元素也可写成如下格式，方便后续抽取：
        # self.my_element(self.WLAN_button).click()
        self.click(self.WLAN_button)

    def click_more(self):
        # self.driver.find_element_by_xpath("//*[contains(@content-desc, '更多选项')]").click()
        # self.my_element(self.more_button).click()
        self.click(self.more_button)

    def click_advanced(self):
        # WebDriverWait(self.driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@text, '高级')]")).click()
        # self.my_element(self.advanced_button).click()
        self.click(self.advanced_button)

    def click_state(self):
        # WebDriverWait(self.driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@text, '保持WLAN')]")).click()
        # self.my_element(self.state_button).click()
        self.click(self.state_button)

    def click_recharge(self):
        # WebDriverWait(self.driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@text, '仅限充电时')]")).click()
        # self.my_element(self.WLAN_recharge_button).click()
        self.click(self.WLAN_recharge_button)

    def click_always(self):
        # WebDriverWait(self.driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@text, '始终')]")).click()
        # self.my_element(self.WLAN_always_button).click()
        self.click(self.WLAN_always_button)

	def test_test(self):
		pass
	def test_test2(self):
		pass







