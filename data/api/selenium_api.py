import time
import traceback
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#在现有浏览器中打开新的标签页

# new_window = 'window.open("http://merchant.ips.com.cn/Login.aspx")'
# driver.execute_script(new_window)
#标签窗口切换，0是第一个标签 1是第二个标签  close()会删除第一个元素 并把第二个元素的序号变为0 一次类推
#driver.switch_to.window(driver.window_handles[0])

#当前标签关闭
#driver.close()
#浏览器关闭
#driver.quit()

#等待某个元素加载完成再继续 否则抛出异常
# try:
#     element = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "big1"))
#     ).click()
# except Exception as ex:
#     print("密码框元素定位超时（5s）")
#通过特定内容寻找标签
#element = driver.find_element_by_xpath("//img[@src='img.aspx']")