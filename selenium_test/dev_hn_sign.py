from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium_test import global_var
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class IpsSign:

    def __init__(self):
        # 存储当前页面需要输入的用户密码
        self.single_row_dict = {}
        # 存储正确的用户密码
        self.correct_account_dict = {}
        # 存储当前异常行的账户密码并加入异常信息
        self.result_message_dict = {}
        # 异常的用户密码字典
        self.unusual_account_dict = {}


        # 错误判断标签
        self.warn_xpath_string = global_var.hn_warn_string
        # 获取driver
        self.driver = webdriver.Firefox(
            executable_path=r'F:\software\python\python3.7\Tools\geckodriver\geckodriver.exe')
        # self.driver = webdriver.Chrome(executable_path=r'F:\software\python\python3.7\Tools\geckodriver\chromedriver.exe')

        # 登录按钮、账户、密码的标签id
        self.login_button_id = global_var.hn_login_button_id
        self.user_name_id = global_var.hn_user_name_id
        self.password_id = global_var.hn_password_id

        #字典路径
        self.user_name_dic_dir=global_var.hn_user_name_dic_dir
        self.password_dic_dir = global_var.hn_password_dic_dir

        # 从字典中获取数据
        self.user_name_dic_generator = self.get_user_name_dic_generator()

        self.user_name_pwd_generator = self.get_user_pwd_dic_generator()

        self.data_flag = True

    # 从字典中读取数据生成器
    def get_user_name_dic_generator(self):
        with open(self.user_name_dic_dir, 'r') as f:
            while True:
                lines = f.readlines(1000)
                if not lines:
                    break
                for line in lines:
                    yield line.replace("\n", "")

    def get_user_pwd_dic_generator(self):
        with open(self.password_dic_dir, 'r') as f:
            while True:
                lines = f.readlines(1000)
                if not lines:
                    break
                for line in lines:
                    yield line.replace("\n", "")

    # 从迭代器中读取一行数据
    def get_dict_data(self):
        try:
            self.single_row_dict['user_name_dic'] = next(self.user_name_dic_generator)

        except StopIteration:
            print("no user_name data")
            self.data_flag = False

        try:
            self.single_row_dict['user_pwd_dic'] = next(self.user_name_pwd_generator)

        except StopIteration:
            print("no user_pwd data")
            self.data_flag = False

    # 获取driver
    def get_driver(self):
        self.driver.get(global_var.hn_login_url)

    # 输入账户密码
    def enter_count_and_password(self):
        driver = self.driver

        driver.find_element_by_id(self.user_name_id).clear()
        print("当前账号" + self.single_row_dict['user_name_dic'])
        driver.find_element_by_id(self.user_name_id).send_keys(self.single_row_dict['user_name_dic'])

        driver.find_element_by_id(self.password_id).clear()
        print("当前密码" + self.single_row_dict['user_pwd_dic'])
        driver.find_element_by_id(self.password_id).send_keys("123456")

    # 点击登录
    def click_login(self):
        driver = self.driver
        driver.find_element_by_id(self.login_button_id).click()

    # 通过xpath_string判断标签是否存在
    def is_element_present(self, xpath_string):
        driver = self.driver
        try:
            element = driver.find_element_by_xpath(xpath_string)
            return True
        # 原文是except NoSuchElementException, e:
        except NoSuchElementException as e:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False

    # 判断标签的值并返回
    def get_element_value(self, xpath_string):
        driver = self.driver
        element = driver.find_element_by_xpath(xpath_string)
        element_value = element.text
        return element_value

    # 一个登录的过程
    def driver_ordinaryadmin_login(self):
        self.get_driver()
        self.no_convert_to_login()

    # 在原页面重新输入数据登陆
    def no_convert_to_login(self):
        self.enter_count_and_password()
        self.click_login()


    # 回退并刷新页面
    def back_and_refresh(self):
        driver = self.driver
        driver.back()
        driver.refresh()
        #driver.find_element_by_id("rdNormal").click()

    # 循环登录
    def loop_to_sign(self):
        driver = self.driver
        self.get_driver()


        #等待浏览器加载
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, global_var.hn_user_name_id))
            )
        except Exception as ex:
            print("账户框元素定位超时（5s）")


        correct_account_count = 0

        while self.data_flag:
            sleep(0.5)
        #for i in range(0, 5):
            #如果错误元素不存在，说明是登录正确 进入到了账户页面
            if not self.is_element_present(self.warn_xpath_string):
                self.result_message_dict = {}
                self.result_message_dict.update(self.single_row_dict)
                self.result_message_dict['information'] = ["正确的用户密码"]
                self.correct_account_dict[correct_account_count] = [self.result_message_dict]
                correct_account_count += 1
                self.back_and_refresh()

            #一开始的错误信息标签是空的或者账户错误信息显示
            elif self.get_element_value(self.warn_xpath_string) == global_var.hn_error_message[
                'ENUP'] or self.get_element_value(
                    self.warn_xpath_string) == "":
                self.get_dict_data()
                self.no_convert_to_login()

            #额外的错误信息，保存此时的账户密码留待查看
            else:
                self.result_message_dict = {}
                self.result_message_dict.update(self.single_row_dict)
                self.result_message_dict['information'] = [self.get_element_value(self.warn_xpath_string)]
                self.correct_account_dict[correct_account_count] = [self.result_message_dict]
                correct_account_count += 1
                self.get_dict_data()
                self.no_convert_to_login()

        print(self.correct_account_dict)


if __name__ == "__main__":
    T1 = IpsSign()
    T1.loop_to_sign()
