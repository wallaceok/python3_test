import unittest
from selenium import webdriver
import os
import  time
# （十五）文件上传

class baiduSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)
    """
 
    """
    #（十五）文件上传   接下来通过send_keys()方法来实现文件上传。
    def test_WebDriverWait(self):

        driver =self.driver
        file_path = 'file:///' + os.path.abspath('upfile.html')
        driver.get(file_path)
        # 定位上传按钮，添加本地文件
        u = driver.find_element_by_name("file")
        u.send_keys('d:\\upload_file.txt')
        print(u.get_attribute('value')+"**********************")


        time.sleep(2)


    def tearDown(self):
        self.driver.quit()
        print("已经退出浏览器")
if  __name__ == "__main__":
    unittest.main()
"""
有时我们会碰到下拉框，WebDriver提供了Select类来处理下拉框。 如百度搜索设置的下拉框，如下图：
Select类用于定位select标签。

select_by_value() 方法用于定位下接选项中的value值。
"""
