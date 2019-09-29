import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import  time

class baiduSearch(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)

    def test_search_in_baidu(self):
        driver =self.driver

        driver.get("http://www.baidu.com")

        self.assertIn("百度",driver.title)
        elem = driver.find_element_by_name('wd')
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)

        driver.get("http://blog.sina.com.cn/s/blog_6a65271b0101ictj.html")
        links = driver.find_elements_by_tag_name("div")
        for l in links :
            print("div de class  value is :%s" % l.get_attribute("class"))

            # 关闭标签页
            #ActionChains(driver).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
        #assert  "lihaimin" not in  driver.page_source

    def tearDown(self):
        self.driver.close()
if  __name__ == "__main__":
    unittest.main()
