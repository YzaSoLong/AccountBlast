import unittest
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import pytesseract
import unittest
from PIL import Image

# tesseract.exe所在的文件路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path=r'F:\software\python\python3.7\Tools\geckodriver\chromedriver.exe')
        self.driver = webdriver.Firefox(
            executable_path=r'F:\software\python\python3.7\Tools\geckodriver\geckodriver.exe')
        self.xpath_string = "//span[@id='lbWarning']"

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://merchant.ips.com.cn/Login.aspx?logType=1")
        driver.get("http://www.baidu.com")
        driver.back()
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "big1"))
            ).click()
        except Exception as ex:
            print("密码框元素定位超时（5s）")

        #driver.find_element_by_class_name("big1").click()

        driver.find_element_by_id("rdNormal").click()
        driver.find_element_by_id("txtMerchantCode").send_keys("1")
        driver.find_element_by_id("txtUserName").send_keys("1")
        driver.find_element_by_id("txtUserPwd").send_keys("1")
        self.get_CAPTCHA_picture()
        self.get_CAPTCHA_content()
        self.enter_CAPTCHA()
        #driver.find_element_by_id("txtValidateCode").send_keys("1")

        driver.find_element_by_id("btnLogin").click()

        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "big1"))
            )
        except Exception as ex:
            print("密码框元素定位超时（5s）")

        if self.is_element_present():
            print("span is exist")
        else:
            print("Page load error")

        print(self.get_element_value())


    # driver.find_element_by_id("txtUserName").send_keys("1")
    # self.assertIn("Python", driver.title)
    # elem = driver.find_element_by_name("q")
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source

    def is_element_present(self):

        driver = self.driver
        try:
            element = driver.find_element_by_xpath(self.xpath_string)
            # 原文是except NoSuchElementException, e:
            return True
        except NoSuchElementException as e:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False

    # 判断标签的值 1为账号或密码错误。 2为验证码不正确
    def get_element_value(self):
        driver = self.driver
        element = driver.find_element_by_xpath(self.xpath_string)
        element_value = element.text

        return element_value

        # if element_value == "账号或密码错误。":
        #     return 1
        #
        # elif element_value == "验证码不正确":
        #     return 2
        #
        # elif element_value == "请输入验证码":
        #     return 3

        # 获取验证码图片

    def get_CAPTCHA_picture(self):

        driver = self.driver
        driver.get_screenshot_as_file('screen_shot/screenshot_file_1.png')
        element = driver.find_element_by_xpath("//img[@src='img.aspx']")
        left = int(element.location['x'])
        top = int(element.location['y'])
        right = int(element.location['x'] + element.size['width'])
        bottom = int(element.location['y'] + element.size['height'] + float(5))
        # 通过Image处理图像
        im = Image.open('screen_shot/screenshot_file_1.png')
        im = im.crop((left, top, right, bottom))
        im.save('screen_shot/screenshot_capture_1.png')

        # 读取验证码内容

    def get_CAPTCHA_content(self):

        str1 = "screen_shot/screenshot_capture_1.png"
        # 新建Image对象
        image = Image.open(str1)
        # 进行置灰处理
        image = image.convert('L')

        # 二值化阈值
        threshold = 225
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        # 通过表格转换成二进制图片，1的作用是白色，不然就全部黑色了
        image = image.point(table, "1")
        # image.show()
        self.result = pytesseract.image_to_string(image).replace("\x0c", "").replace("\n", "")
        print(self.result)

    # 输入验证码
    def enter_CAPTCHA(self):
        driver = self.driver
        driver.find_element_by_id("txtValidateCode").send_keys(self.result)

    def tearDown(self):
        pass
        # self.driver.close()


if __name__ == "__main__":
    unittest.main()
