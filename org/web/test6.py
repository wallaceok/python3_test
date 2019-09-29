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
# （十）定位一组元素

class baiduSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)
    """
    find_elements_by_id()
    find_elements_by_name()
    find_elements_by_class_name()
    find_elements_by_tag_name()
    find_elements_by_link_text()
    find_elements_by_partial_link_text()
    find_elements_by_xpath()
    find_elements_by_css_selector()
    """
    #（十）定位一组元素
    def test_WebDriverWait(self):

        driver =self.driver
        driver.get("https://www.baidu.com")

        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(1)
        # 定位一组元素
        texts = driver.find_elements_by_xpath('//div/h3/a')

        # 循环遍历出每一条搜索结果的标题
        for t in texts:
            print(t.text)

        time.sleep(2)


    def tearDown(self):
        self.driver.quit()
        print("quit ____________________")
if  __name__ == "__main__":
    unittest.main()

