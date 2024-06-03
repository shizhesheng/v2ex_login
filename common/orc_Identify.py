# -*- coding: utf-8 -*-

import ddddocr


class OrcIdentify:
    def __init__(self):
        self.ocr = ddddocr.DdddOcr()

    def identify(self, pic_path):
        with open(pic_path, 'rb') as f:
            image = f.read()
        res = self.ocr.classification(image)
        return res

    def yanzhengma(self, pic_path):
        pass


if __name__ == '__main__':
    print(OrcIdentify().identify('/Users/zhengchunyu/PycharmProjects/v2ex_login/v2ex_login/common/3captcha.jpg'))
