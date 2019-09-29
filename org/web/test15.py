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
在前面的例子中我们一直使用quit()方法，其含义为退出相关的驱动程序和关闭所有窗口。除此之外，WebDriver还提供了close()方法，用来关闭当前窗口。例多窗口的处理，在用例执行的过程中打开了多个窗口，我们想要关闭其中的某个窗口，这时就要用到close()方法进行关闭了。

close() 关闭单个窗口

quit() 关闭所有窗口
"""
