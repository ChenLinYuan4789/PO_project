from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import pytest

class SearchPage(BaseAction):
    # 搜索按钮
    search_button = By.XPATH, "content-desc,搜索设置,1"
    # 搜索框
    search_view = By.ID, "android:id/search_src_text"
    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    # 点击搜索按钮
    def click_search(self):
        self.click(self.search_button)

    # 输入搜索内容
    def send_text(self, text):
        self.send_keys(self.search_view, text)

    def click_back(self):
        self.click(self.back_button)