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


# 在新打开的标签页中输入

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path=r'F:\software\python\python3.7\Tools\geckodriver\chromedriver.exe')
        self.driver = webdriver.Firefox(
            executable_path=r'F:\software\python\python3.7\Tools\geckodriver\geckodriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://merchant.ips.com.cn/Login.aspx?logType=1")

        new_window = 'window.open("http://merchant.ips.com.cn/Login.aspx")'
        driver.execute_script(new_window)

        driver.close()

        driver.switch_to.window(driver.window_handles[0])

        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "big1"))
            ).click()
        except Exception as ex:
            print("密码框元素定位超时（5s）")

        driver.find_element_by_id("rdNormal").click()
        driver.find_element_by_id("txtMerchantCode").send_keys("1")
        driver.find_element_by_id("txtUserName").send_keys("1")
        driver.find_element_by_id("txtUserPwd").send_keys("1")

    def tearDown(self):
        pass
        #self.driver.close()


if __name__ == "__main__":
    unittest.main()
