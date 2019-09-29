import unittest
from selenium import webdriver
import os
import  time
# （十七）调用JavaScript代码

class baiduSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)


    #（十七）调用JavaScript代码
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
        # 通过javascript设置浏览器窗口的滚动条位置
        js = "window.scrollTo(100,450);"
        driver.execute_script(js)

        time.sleep(12)
    def tearDown(self):
        self.driver.quit()
        print("已经退出浏览器")
if  __name__ == "__main__":
    unittest.main()
"""
虽然WebDriver提供了操作浏览器的前进和后退方法，但对于浏览器滚动条并没有提供相应的操作方法。在这种情况下，就可以借助JavaScript来控制浏览器的滚动条。WebDriver提供了execute_script()方法来执行JavaScript代码。

用于调整浏览器滚动条位置的JavaScript代码如下：

<!-- window.scrollTo(左边距,上边距); -->
window.scrollTo(0,450);
window.scrollTo()方法用于设置浏览器窗口滚动条的水平和垂直位置。方法的第一个参数表示水平的左间距，第二个参数表示垂直的上边距。其代码如下：
"""
