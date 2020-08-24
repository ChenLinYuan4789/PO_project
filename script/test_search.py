import os, sys, pytest
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.search_page import SearchPage
from base.base_yml import yml_file

def yml_key(key):
    return yml_file("search")[key]

class TestSearch():

    def setup(self):
        self.driver = init_driver()
        self.search_page = SearchPage(self.driver)

    @pytest.mark.parametrize("keys", yml_key("test_search"))
    def test_search(self, keys):
        # 点击搜索按钮
        self.search_page.click_search()
        # 输入搜索内容
        self.search_page.send_text(keys)
        # 点击返回
        self.search_page.click_back()

    @pytest.mark.parametrize("keys", yml_key("test_search2"))
    def test_search2(self, keys):
        # 点击搜索按钮
        self.search_page.click_search()
        # 输入搜索内容
        self.search_page.send_text(keys)
        # 点击返回
        self.search_page.click_back()



