# _*_ coding:utf-8 _*_
# Author:liu
from PIL import Image
from pytesseract import *

# 上面都是导包，只需要下面这一行就能实现图片文字识别
# text = pytesseract.image_to_string(Image.open('2.png'), lang='chi_sim')  # 设置为中文文字的识别
# text = pytesseract.image_to_string(Image.open('2.png'), lang='eng')  # 设置为英文或阿拉伯字母的识别
# print(text)
from PIL import Image
import numpy as np

# 图片的灰度化
# 打开一张图片
# img = Image.open("./img/0th.png")
# # 图片灰度化
# img = img.convert("L")
# # 显示图片
# # img.show()
# # 将图片转换为数组形式，元素为其像素的亮度值
# print(np.asarray(img))


# ============================
# 图片的二值化
# 打开一张图片
# img = Image.open("./img/0th.png")
# # # 将图片化为32*21的
# img = img.resize((32, 32))
# # 二值化
# img = img.point(lambda x: 1 if x > 120 else 0)
# # 将图片转换为数组形式，元素为其像素的亮度值
# img_array = np.asarray(img)
# print(img_array)

# 将二值化后的数组转化成网格特征统计图
#
# def get_features(array):
#     # 拿到数组的高度和宽度
#     h, w = array.shape
#     data = []
#     for x in range(0, w / 4):
#         offset_y = x * 4
#         temp = []
#         for y in range(0, h / 4):
#             offset_x = y * 4
#             # 统计每个区域的1的值
#             temp.append(sum(sum(array[0 + offset_y:4 + offset_y, 0 + offset_x:4 + offset_x])))
#         data.append(temp)
#     return np.asarray(data)
#
#
# # 打开一张图片
# # img = Image.open("./img/0th.png")
# # 将图片化为32*32的
# img = img.resize((32, 32))
#
# # 二值化
# img = img.point(lambda x: 1 if x > 120 else 0)
# # 将图片转换为数组形式，元素为其像素的亮度值
# img_array = np.asarray(img)
# print(img_array)
#
# # 得到网格特征统计图
# features_array = get_features(img_array)
# print(features_array)
#
# features_vector = features_array.reshape(features_array.shape[0] * features_array.shape[1])
# print(features_vector)
import sys


