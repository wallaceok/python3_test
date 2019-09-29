import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import  time
# （八）获取断言信息
class baiduSearch(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.set_window_size(1920,1080)



    """
    title：用于获得当前页面的标题。

    current_url：用户获得当前页面的URL。
    
    text：获取搜索条目的文本信息。
    """
    def test_action1(self):
        driver =self.driver

        driver.get("https://www.baidu.com")

        print('Before search================')

        # 打印当前页面title
        title = driver.title
        print(title)

        # 打印当前页面URL
        now_url = driver.current_url
        print(now_url)

        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(1)

        print('After search================')

        # 再次打印当前页面title
        title = driver.title
        print(title)

        # 打印当前页面URL
        now_url = driver.current_url
        print(now_url)

        # 获取结果数目
        user = driver.find_element_by_class_name('nums').text
        print(user)

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
