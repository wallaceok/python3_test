import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import  time
# （十四）下拉框选择

class baiduSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)
    """
 
    """
    #（十四）下拉框选择
    def test_WebDriverWait(self):

        driver =self.driver
        driver.implicitly_wait(10)
        driver.get("https://www.baidu.com/")

        # 鼠标悬停至“设置”链接
        driver.find_element_by_link_text('设置').click()
        time.sleep(1)
        # 打开搜索设置
        driver.find_element_by_link_text("搜索设置").click()
        time.sleep(2)

        # 搜索结果显示条数
        sel = driver.find_element_by_xpath("//select[@id='nr']")
        Select(sel).select_by_value('50')  # 显示50条

        sel1 = driver.find_element_by_xpath("//select[@id='issw1']")
        Select(sel1).select_by_value('2')

        time.sleep(2)


    def tearDown(self):
        self.driver.quit()
        print("quit ____________________")
if  __name__ == "__main__":
    unittest.main()
"""
有时我们会碰到下拉框，WebDriver提供了Select类来处理下拉框。 如百度搜索设置的下拉框，如下图：
Select类用于定位select标签。

select_by_value() 方法用于定位下接选项中的value值。
"""
