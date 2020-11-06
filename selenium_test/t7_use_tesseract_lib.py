from tesserocr import PyTessBaseAPI

with PyTessBaseAPI(path='F:/software/tesserOcr/tessdata/.',lang='eng') as tess_api:
    tess_api.SetImageFile('screen_shot/screenshot_capture_1.png')
    print(tess_api.GetUTF8Text())

