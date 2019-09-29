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
# （十二）多窗口切换

class baiduSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)
    """
 
    """
    #（十二）多窗口切换
    def test_WebDriverWait(self):

        driver =self.driver
        driver.implicitly_wait(10)
        driver.get("https://www.baidu.com/")

        # 获得百度搜索窗口句柄
        sreach_windows = driver.current_window_handle

        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_link_text("立即注册").click()
        time.sleep(2)
        # 获得当前所有打开的窗口的句柄
        all_handles = driver.window_handles

        # 进入注册窗口
        for handle in all_handles:
            if handle == sreach_windows:
                driver.switch_to.window(handle)
                print('now register window!')
                driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
                driver.find_element_by_name("userName").send_keys('username')
                driver.find_element_by_name('password').send_keys('password')
                time.sleep(2)

        time.sleep(2)


    def tearDown(self):
        self.driver.quit()
        print("quit ____________________")
if  __name__ == "__main__":
    unittest.main()
"""
在本例中所涉及的新方法如下：

current_window_handle：获得当前窗口句柄。

window_handles：返回所有窗口的句柄到当前会话。

switch_to.window()：用于切换到相应的窗口，与上一节的switch_to.frame()类似，前者用于不同窗口的切换，后者用于不同表单之间的切换。
"""
