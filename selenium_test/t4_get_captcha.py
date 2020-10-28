import os
import pytesseract
from PIL import Image
from collections import defaultdict

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# tesseract.exe所在的文件路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ips_captcha(unittest.TestCase):

    def setup(self):
        pass
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def test_ips_captcha(self):

        str1 = "screen_shot/screenshot_capture_1.png"
        # 新建Image对象
        image = Image.open(str1)
        # 进行置灰处理
        image = image.convert('L')
        # image = image.convert('P')
        # 这个是二值化阈值
        threshold = 225
        table = []

        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        #
        # 通过表格转换成二进制图片，1的作用是白色，不然就全部黑色了

        image = image.point(table, "1")
        # image.show()
        result = pytesseract.image_to_string(image)
        result = result.replace("\x0c", "")
        result = result.replace("\n", "")
        print(result)


    def tearDown(self):
        pass
        #self.driver.close()

if __name__ == "__main__":

    unittest.main()
