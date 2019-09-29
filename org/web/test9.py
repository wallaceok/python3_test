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
# 警告框处理

class baiduSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)
    """
 
    """
    #警告框处理
    def test_WebDriverWait(self):

        driver =self.driver
        driver.implicitly_wait(10)
        driver.get("https://www.baidu.com/")

        # 鼠标悬停至“设置”链接
        link = driver.find_element_by_link_text('设置')
        ActionChains(driver).move_to_element(link).perform()

        # 打开搜索设置
        driver.find_element_by_link_text("搜索设置").click()
        time.sleep(2)
        # 保存设置
        driver.find_element_by_class_name("prefpanelgo").click()
        time.sleep(2)

        # 接受警告框
        driver.switch_to.alert.accept()

        time.sleep(2)


    def tearDown(self):
        self.driver.quit()
        print("quit ____________________")
if  __name__ == "__main__":
    unittest.main()
"""
在WebDriver中处理JavaScript所生成的alert、confirm以及prompt十分简单，具体做法是使用 switch_to.alert 方法定位到 alert/confirm/prompt，然后使用text/accept/dismiss/ send_keys等方法进行操作。

text：返回 alert/confirm/prompt 中的文字信息。

accept()：接受现有警告框。

dismiss()：解散现有警告框。

send_keys(keysToSend)：发送文本至警告框。keysToSend：将文本发送至警告框。

如下图，百度搜索设置弹出的窗口是不能通过前端工具对其进行定位的，这个时候就可以通过switch_to_alert()方法接受这个弹窗。 



通过switch_to_alert()方法获取当前页面上的警告框，并使用accept()方法接受警告框。
"""
