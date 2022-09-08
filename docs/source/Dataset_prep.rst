Dataset\_prep module
====================
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