import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


class Common:
    def __init__(self, browser):
        # 浏览器初始化验证 [2]()
        browser_map = {
            'Firefox': webdriver.Firefox,
            'Chrome': webdriver.Chrome
        }
        if browser not in browser_map:
            raise ValueError(f"Unsupported browser: {browser}")

        self.driver = browser_map[browser]()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def open_url(self, url):
        self.driver.get(url)

    def locate_element(self, locate_type, value):
        # 使用新版元素定位方式 [3]()
        locators = {
            'id': By.ID,
            'name': By.NAME,
            'class': By.CLASS_NAME,
            'text': By.LINK_TEXT,
            'partial': By.PARTIAL_LINK_TEXT,
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'tag': By.TAG_NAME
        }

        try:
            return self.driver.find_element(locators[locate_type], value)
        except (NoSuchElementException, KeyError):
            return None

    def click(self, locate_type, value):
        el = self.locate_element(locate_type, value)
        el.click()


    def input_data(self, locate_type, value, data):
        el = self.locate_element(locate_type, value)
        el.clear()
        el.send_keys(data)


    def switch_to_frame(self, locate_type, value):
        el = self.locate_element(locate_type, value)
        self.driver.switch_to.frame(el)


    def get_text(self, locate_type, value):
        el = self.locate_element(locate_type, value)
        return el.text


    def get_alert_text(self):
        try:
            return self.driver.switch_to.alert.text
        except Exception:
            return ""


    def select_dropdown(self, locate_type, value, visible_text):
        el = self.locate_element(locate_type, value)
        Select(el).select_by_visible_text(visible_text)


    def switch_to_default_content(self):
        self.driver.switch_to.default_content()


    def __del__(self):
        time.sleep(3)
        if hasattr(self, 'driver'):
            self.driver.quit()