import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import ctime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import  time
# （十一）多表单切换

class baiduSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)
    """
 
    """
    #（十一）多表单切换
    def test_WebDriverWait(self):

        driver =self.driver
        driver.get("https://www.126.com/")
        driver.find_element_by_id("lbNormal").click()
        time.sleep(2)
        #driver.switch_to.frame('x-URS-iframe')
        xf = driver.find_element_by_xpath('.//iframe')
        driver.switch_to.frame(xf)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("username")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_id("dologin").click()
        driver.switch_to.default_content()

        time.sleep(2)


    def tearDown(self):
        self.driver.quit()
        print("quit ____________________")
if  __name__ == "__main__":
    unittest.main()
"""
switch_to.frame() 默认可以直接取表单的id 或name属性。如果iframe没有可用的id和name属性，则可以通过下面的方式进行定位。

……
#先通过xpth定位到iframe
xf = driver.find_element_by_xpath('//*[@id="x-URS-iframe"]')

#再将定位对象传给switch_to.frame()方法
driver.switch_to.frame(xf)
……
driver.switch_to.parent_frame()
除此之外，在进入多级表单的情况下，还可以通过switch_to.default_content()跳回最外层的页面。
"""
