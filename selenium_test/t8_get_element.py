from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from selenium_test import global_var


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path=r'F:\software\python\python3.7\Tools\geckodriver\chromedriver.exe')
        self.driver = webdriver.Firefox(
            executable_path=r'F:\software\python\python3.7\Tools\geckodriver\geckodriver.exe')
        # self.xpath_string = "//span[@id='lbWarning']"

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(global_var.hn_login_url)

        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, global_var.hn_user_name_id))
            )
        except Exception as ex:
            print("密码框元素定位超时（5s）")

        self.get_element_value()


    def get_element_value(self):
        driver = self.driver
        driver.find_element_by_id(global_var.hn_user_name_id).send_keys("111")
        driver.find_element_by_id(global_var.hn_password_id).send_keys("111")
        sleep(1)
        driver.find_element_by_id(global_var.hn_login_button_id).click()
        return True

    def tearDown(self):
        pass
        # self.driver.close()


if __name__ == "__main__":
    unittest.main()
