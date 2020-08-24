from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction():

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.my_element(loc).click()

    def send_keys(self, loc, text):
        self.my_element(loc).send_keys(text)

    def content_clear(self, loc):
        self.my_element(loc).clear()

    def my_element(self, loc):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.xpath_more_pinjie(value)
        return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(by, value))

    def my_elements(self, loc):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.xpath_more_pinjie(value)
        return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_elements(by, value))

    def xpath_one_pinjie(self, loc):

        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(",")
        feature = ""

        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + " and "
        elif len(args) == 3:
            if args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + " and "
            elif args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + " and "
        return feature

    def xpath_more_pinjie(self, loc):
        start = "//*["
        end = "]"
        feature = ""

        if isinstance(loc, str):
            if loc.startswith("//"):
                return loc
            else:
                feature = self.xpath_one_pinjie(loc)
        else:
            for i in loc:
                feature += self.xpath_one_pinjie(i)

        vue = start + feature.rstrip(" and") + end
        return vue