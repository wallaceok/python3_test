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
# （九）设置元素等待
#  显式等待
class baiduSearch(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)


    def test_WebDriverWait(self):
        driver =self.driver

        driver.get("https://www.baidu.com")

        element = WebDriverWait(driver, 5, 0.5).until(
            EC.presence_of_element_located((By.ID, "kw"))
        )
        element.send_keys('selenium')
        time.sleep(2)
    #隐式等待
    """
    implicitly_wait() 默认参数的单位为秒，本例中设置等待时长为10秒。
    首先这10秒并非一个固定的等待时间，它并不影响脚本的执行速度。其次，它并不针对页面上的某一元素进行等待。
    当脚本执行到某个元素定位时，如果元素可以定位，则继续执行；如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到。
    假设在第6秒定位到了元素则继续执行，若直到超出设置时长（10秒）还没有定位到元素，则抛出异常。
    """
    def test_implicitly_wait(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("https://www.baidu.com")
        try:
            print(ctime())
            driver.find_element_by_id("kw22").send_keys('selenium')
        except NoSuchElementException as e:
            print(e)
        finally:
            print(ctime())


    def tearDown(self):
        self.driver.quit()
        print("quit ____________________")
if  __name__ == "__main__":
    unittest.main()
"""
WebDriverWait类是由WebDirver 提供的等待方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。具体格式如下：

WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
driver ：浏览器驱动。

timeout ：最长超时时间，默认以秒为单位。

poll_frequency ：检测的间隔（步长）时间，默认为0.5S。

ignored_exceptions ：超时后的异常信息，默认情况下抛NoSuchElementException异常。

WebDriverWait()一般由until()或until_not()方法配合使用，下面是until()和until_not()方法的说明。

until(method, message=‘’)
调用该方法提供的驱动程序作为一个参数，直到返回值为True。

until_not(method, message=‘’)
调用该方法提供的驱动程序作为一个参数，直到返回值为False。

在本例中，通过as关键字将expected_conditions 重命名为EC，并调用presence_of_element_located()方法判断元素是否存在。

"""
