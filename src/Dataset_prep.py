"""

Here is prepared the data, that is used to learn yolov5 neural network. It is devided on datasets to train and validate. 


Parameters
----------
img_folder: str
  Path to all images
labels_folder: str
  Path to all labels
train_factor: float
  Factor, that is used to show how many images and labales are going to be used to train
val_factor: float
  Factor, that is used to show how many images and labales are going to be used to validation
all_img: list
  List with all images
all_labels: list
  List with all labels
count_to_train: int
  How many images are going to be trained
img_file: str
  Random choice of image of all images list
label_file: str
  The same choice as image for labels
"""

import os
import shutil
from random import choice

img_folder = '../archive/images/'
labels_folder = '../archive/labels/'

train_factor = 0.8
val_factor = 0.2


all_img = os.listdir(img_folder)
all_labels = os.listdir(labels_folder)
count_to_train = int(train_factor * len(all_img))
for i in range(count_to_train):
  img_file = choice(all_img)
  label_file = img_file[:-4] + '.txt'
  shutil.copy2(img_folder+img_file, '../ext/yolov5/dataset/images/train')
  shutil.copy2(labels_folder+label_file, '../ext/yolov5/dataset/labels/train')

  all_img.remove(img_file)
  all_labels.remove(label_file)

for i in range(len(all_img)):
  img_file = choice(all_img)
  label_file = img_file[:-4] + '.txt'
  shutil.copy2(img_folder+img_file, '../ext/yolov5/dataset/images/val')
  shutil.copy2(labels_folder+label_file, '../ext/yolov5/dataset/labels/val')

  all_img.remove(img_file)
  all_labels.remove(label_file)