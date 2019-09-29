import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import  time
# 常用操作方法
class baiduSearch(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)
    # 点击和输入
    def test_click(self):
        driver =self.driver

        driver.get("https://www.baidu.com")

        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
    #提交
    def test_submit(self):
        driver = self.driver
        driver.get("https://www.baidu.com")

        search_text = driver.find_element_by_id('kw')
        search_text.send_keys('selenium')
        search_text.submit()
        assert  "百度"  in driver.title
        time.sleep(1)

    def test_other(self):
        driver = self.driver
        driver.get("http://www.baidu.com")
        # 获得输入框的尺寸
        size = driver.find_element_by_id('kw').size
        print(size)

        # 返回百度页面底部备案信息
        text = driver.find_element_by_id("cp").text
        print(text)

        # 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
        attribute = driver.find_element_by_id("kw").get_attribute('type')
        print(attribute)

        # 返回元素的结果是否可见， 返回结果为 True 或 False
        result = driver.find_element_by_id("kw").is_displayed()
        print(result)

    def tearDown(self):
        self.driver.quit()
        print("quit ____________________")
if  __name__ == "__main__":
    unittest.main()
