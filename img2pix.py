# coding:utf-8
import os
import cv2
import sys
from pixel import make_dot

argvs = sys.argv
img_path = argvs[1]

k = 128
scale = 6
# 0, 50, 100, 200
blur = 100
# 輪郭線膨張
erode = 1
# 透過PNGで書き出す
alpha = True
# Twitter用に1pxだけ透過
to_tw = False

img_res, colors = make_dot(
    img_path,
    k=k,
    scale=scale,
    blur=blur,
    erode=erode,
    alpha=alpha,
    to_tw=to_tw
)

img_name = os.path.basename(img_path) + '_pixel'
result_path = os.path.join('./', img_name + '.png')
cv2.imwrite(result_path, img_res)
