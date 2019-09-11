# -*- coding:utf-8 -*-

import cv2
import numpy as np
import glob

import os

# 先ほど集めてきた画像データのあるディレクトリ
input_data_path = '/Users/takayuki/Document/machine_learning/bing/Hillary_Clinton_20190905135127'
# 切り抜いた画像の保存先ディレクトリ(予めディレクトリを作っておいてください)
save_path = '/Users/takayuki/Document/machine_learning/bing/cutted_Clinton_image'
# OpenCVのデフォルトの分類器のpath。(https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xmlのファイルを使う)
cascade_path = '/Users/takayuki/Document/machine_learning/opencv-3.3.1/data/haarcascades/haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_path)
# faceCascade = cv2.CascadeClassifier(cascade_path)

assert os.path.isfile(cascade_path), 'haarcascade_frontalface_default.xml がない'


# 収集した画像の枚数(任意で変更)
image_count = 700
# 顔検知に成功した数(デフォルトで0を指定)
face_detect_count = 0

# 取得した画像を一括で読み込む
images = glob.glob("/Users/takayuki/Document/machine_learning/bing/Hillary_Clinton_20190905135127/*.jpg")
# 集めた画像データから顔が検知されたら、切り取り、保存する。
for i in images:
  img = cv2.imread(i, cv2.IMREAD_COLOR)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  face = cascade.detectMultiScale(gray, 1.1, 3)
  if len(face) > 0:
    for rect in face:
      # 顔認識部分を赤線で囲み保存(今はこの部分は必要ない)
      # cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=1)
      # cv2.imwrite('detected.jpg', img)
      x = rect[0]
      y = rect[1]
      w = rect[2]
      h = rect[3]
      cv2.imwrite(save_path + 'cutted_Clinton' + str(face_detect_count) + '.jpg', img[y:y+h, x:x+w])
      face_detect_count = face_detect_count + 1
  # else:
    # print 'noface'