import unittest
from selenium import webdriver
import os
import  time
# （十六）cookie操作

class baiduSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)


    #（十六）cookie操作
    def test_WebDriver(self):

        driver =self.driver
        driver.get("http://www.yahoo.com")
        # 定位上传按钮，添加本地文件
        cookis = driver.get_cookies()
        print(cookis)
    def test_wall(self):
        driver = self.driver
        driver.get("http://www.yahoo.com")
        # 向cookie的name 和value中添加会话信息
        driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})

        # 遍历cookies中的name 和value信息并打印，当然还有上面添加的信息
        for cookie in driver.get_cookies():
            print("%s -> %s" % (cookie['name'], cookie['value']))

    def tearDown(self):
        self.driver.quit()
        print("已经退出浏览器")
if  __name__ == "__main__":
    unittest.main()
"""
有时候我们需要验证浏览器中cookie是否正确，因为基于真实cookie的测试是无法通过白盒和集成测试进行的。WebDriver提供了操作Cookie的相关方法，可以读取、添加和删除cookie信息。

WebDriver操作cookie的方法：

get_cookies()： 获得所有cookie信息。

get_cookie(name)： 返回字典的key为“name”的cookie信息。

add_cookie(cookie_dict) ： 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。

delete_cookie(name,optionsString)：删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。

delete_all_cookies()： 删除所有cookie信息。

下面通过get_cookies()来获取当前浏览器的cookie信息。

从执行结果可以看到，最后一条cookie信息是在脚本执行过程中通过add_cookie()方法添加的。通过遍历得到所有的cookie信息，从而找到key为“name”和“value”的特定cookie的value。
"""
