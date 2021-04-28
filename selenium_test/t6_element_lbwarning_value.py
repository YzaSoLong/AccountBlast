
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
import pytesseract
import unittest
from selenium_test import global_var

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
        driver.get("https://wxbank.ynhtbank.com/euler-tld/#login")

        try:
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "big1"))
            ).click()
        except Exception as ex:
            print("密码框元素定位超时（5s）")

        if self.get_element_value() == "":
            print("value is empty")

    # 判断标签的值 1为账号或密码错误。 2为验证码不正确
    def get_element_value(self):
        driver = self.driver
        element = driver.find_element_by_xpath(self.xpath_string)
        element_value = element.text

        return element_value

    def tearDown(self):
        pass
        # self.driver.close()


if __name__ == "__main__":
    unittest.main()
