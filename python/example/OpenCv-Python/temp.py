# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

def blurImg(img_path):
    img = Image.open(img_path)
    blurImg = img.filter(ImageFilter.GaussianBlur)
    # blurImg.save(img_path[img_path.rfind('/')])
    # blurImg.show()
    return blurImg
