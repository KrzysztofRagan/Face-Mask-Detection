'''

Documentation - Face Mask Detection 

'''
import os
import shutil
from random import choice

img_folder = '../archive/images/' #path to all images
labels_folder = '../archive/labels/' #path to all labels

train_factor = 0.8
val_factor = 0.2


all_img = os.listdir(img_folder) #list with all images
all_labels = os.listdir(labels_folder) #lsit with all labels
count_to_train = int(train_factor * len(all_img)) #how many images
for i in range(count_to_train):
  img_file = choice(all_img) #random choice from images list
  label_file = img_file[:-4] + '.txt' #same choice for label
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