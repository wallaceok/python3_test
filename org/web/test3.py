import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import  time
# 常用操作方法
class baiduSearch(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)
    # 鼠标移动到设置 上  鼠标悬停操作
    def test_action1(self):
        driver =self.driver

        driver.get("https://www.baidu.com")

        # 定位到要悬停的元素
        above = driver.find_element_by_link_text("设置")
        # 对定位到的元素执行鼠标悬停操作
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(2)
    #键盘操作
    def test_action2(self):
        driver = self.driver

        driver.get("http://www.baidu.com")
        # 输入框输入内容
        driver.find_element_by_id("kw").send_keys("seleniumm")

        # 删除多输入的一个 m
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

        # 输入空格键+“教程”
        driver.find_element_by_id("kw").send_keys(Keys.SPACE)
        driver.find_element_by_id("kw").send_keys("教程")

        # ctrl+a 全选输入框内容
        driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

        # ctrl+x 剪切输入框内容
        driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

        # ctrl+v 粘贴内容到输入框
        driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

        # 通过回车键来代替单击操作
        driver.find_element_by_id("su").send_keys(Keys.ENTER)


        time.sleep(2)


    def tearDown(self):
        self.driver.quit()
        print("quit ____________________")
if  __name__ == "__main__":
    unittest.main()
"""
需要说明的是， 上面的脚本没有什么实际意义， 仅向我们展示模拟键盘各种按键与组合键的用法。

from selenium.webdriver.common.keys import Keys
在使用键盘按键方法前需要先导入 keys 类。
以下为常用的键盘操作：

send_keys(Keys.BACK_SPACE) 删除键（BackSpace）

send_keys(Keys.SPACE) 空格键(Space)

send_keys(Keys.TAB) 制表键(Tab)

send_keys(Keys.ESCAPE) 回退键（Esc）

send_keys(Keys.ENTER) 回车键（Enter）

send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）

send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）

send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）

send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）

send_keys(Keys.F1) 键盘 F1

……

send_keys(Keys.F12) 键盘 F12
"""
