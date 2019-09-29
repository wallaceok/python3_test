#coding=utf-8
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import  time

# 打开浏览器，同时打开首页
url = 'http://www.baidu.com'
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver = webdriver.Chrome()
driver.get(url)
assert  "百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.clear()
elem.send_keys("pycon")
time.sleep(1)
elem.send_keys(Keys.RETURN)
time.sleep(1)
driver.close()