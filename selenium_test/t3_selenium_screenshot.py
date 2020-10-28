import unittest

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#driver = webdriver.Chrome(executable_path=r'F:\software\python\python3.7\Tools\geckodriver\chromedriver.exe')
driver = webdriver.Firefox(executable_path=r'F:\software\python\python3.7\Tools\geckodriver\geckodriver.exe')


# 打开验证码界面driver = webdriver.Chrome()
url="http://merchant.ips.com.cn/Login.aspx?logType=1"
#url = "http://weixin.sogou.com/antispider/?from=%2fweixinwap%3Fpage%3d2%26_rtype%3djson%26ie%3dutf8%26type%3d2%26query%3d%E6%91%A9%E6%8B%9C%E5%8D%95%E8%BD%A6%26pg%3dwebSearchList%26_sug_%3dn%26_sug_type_%3d%26"

driver.set_window_size(1200, 800)

driver.get(url)

# 获取截图
driver.get_screenshot_as_file('../data/picture/screenshot_file_1.png')

# 获取指定元素位置
#element= driver.find_element_by_partial_link_text('img')
#element = driver.find_element_by_id('seccodeImage')
#element = driver.find_element_by_xpath('//input[@id=\'txtValidateCode\']')
element = driver.find_element_by_xpath("//img[@src='img.aspx']")
left = int(element.location['x'])
top = int(element.location['y'])
right = int(element.location['x'] + element.size['width'])
bottom = int(element.location['y'] + element.size['height'])

# 通过Image处理图像
im = Image.open('../data/picture/screenshot_file_1.png')
im = im.crop((left, top, right, bottom))
im.save('../data/picture/screenshot_capture_1.png')