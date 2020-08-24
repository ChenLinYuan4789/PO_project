from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_action import BaseAction

class SafetyPage(BaseAction):

    # 指纹按钮
    fingerprint_button = By.XPATH, "//*[contains(@text, '指纹')]"
    # 重命名按钮
    rename_button = By.ID, "com.android.settings:id/OKBtn"
    # 输入框
    input_view = By.ID, "com.android.settings:id/edit"
    # 确定按钮
    confirm_button = By.XPATH, "//*[contains(@text, '确定')]"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def click_fingerprint(self):
        # self.my_element(self.fingerprint_button).click()
        self.click(self.fingerprint_button)

    def click_fingerprintName(self):
        TouchAction(self.driver).tap(x=525, y=833).perform()

    def click_rename(self):
        # self.my_element(self.rename_button).click()
        self.click(self.rename_button)

    def clear_fingerprintName(self):
        # self.my_element(self.input_view).clear()
        self.content_clear(self.input_view)

    def send_fingerprintNewName(self, text):
        # self.my_element(self.input_view).send_keys(text)
        self.send_keys(self.input_view, text)

    def click_confirm(self):
        # self.my_element(self.confirm_button).click()
        self.click(self.confirm_button)

    def click_back(self):
        self.driver.keyevent(4)




