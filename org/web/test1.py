import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import  time
# 测试浏览导航 back forword
class baiduSearch(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)

    def test_search_in_baidu(self):
        driver =self.driver

        driver.get("http://www.baidu.com")

        self.assertIn("百度",driver.title)
        elem = driver.find_element_by_name('wd')
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)

    def test_back_in_chrome(self):
        driver = self.driver
        driver.get("https://www.sina.com.cn/")

        driver.get("https://mil.news.sina.com.cn/")
        driver.back()   #回退
        driver.forward()  #前进
        driver.refresh()  #刷新


    def tearDown(self):
        self.driver.quit()
        print("quit ____________________")
if  __name__ == "__main__":
    unittest.main()
