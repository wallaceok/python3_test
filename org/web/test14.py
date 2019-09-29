import unittest
from selenium import webdriver
import os
import  time
# （十八）窗口截图

class baiduSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)


    #（（十八）窗口截图
    def test_WebDriver(self):

        driver =self.driver
        driver.get("http://www.baidu.com")
        # 设置浏览器窗口大小
        driver.set_window_size(1024, 768)
        # 搜索
        driver.find_element_by_id("kw").send_keys("selenium")
        time.sleep(1)
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.get_screenshot_as_file("d:\\baidy.png")

        time.sleep(12)
    def tearDown(self):
        self.driver.quit()
        print("已经退出浏览器")
if  __name__ == "__main__":
    unittest.main()
"""
自动化用例是由程序去执行的，因此有时候打印的错误信息并不十分明确。如果在脚本执行出错的时候能对当前窗口截图保存，
那么通过图片就可以非常直观地看出出错的原因。WebDriver提供了截图函数get_screenshot_as_file()来截取当前窗口。
"""
