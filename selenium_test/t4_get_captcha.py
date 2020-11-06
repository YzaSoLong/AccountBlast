import tesserocr
from PIL import Image
import unittest

class ips_captcha(unittest.TestCase):

    def setup(self):
        pass
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def test_ips_captcha(self):

        image_dir = "screen_shot/screenshot_capture_1.png"

        # 新建Image对象
        image = Image.open(image_dir)

        # 进行置灰处理
        image = image.convert('L')

        # 这个是二值化阈值,在threshold值之上的值全部值为白色，之下的值置为黑色
        threshold = 225
        table = []

        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        image = image.point(table, "1")
        with tesserocr.PyTessBaseAPI(path='F:/software/tesserOcr/tessdata/.',lang='eng') as tess_api:
            tess_api.SetImage(image)
            print(tess_api.GetUTF8Text())


    def tearDown(self):
        pass
        #self.driver.close()

if __name__ == "__main__":

    unittest.main()
