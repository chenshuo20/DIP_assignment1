import numpy as np
import cv2
import os
import shutil

path = '../dataset_test_rgb_small/'
src = path + 'val/labels/'
dst = path + 'val_gau/labels/'
image_path = path + 'val/images/' 

folder_name_img = path + 'val_gau/images/'
folder_name_lab = path + 'val_gau/labels/'

os.makedirs(folder_name_img)
shutil.copytree(src, dst)

for image_name in os.listdir(image_path):
    file_path = os.path.join(image_path, image_name)
    if os.path.isfile(file_path):
        img = cv2.imread(file_path)
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        print(folder_name_img + image_name)
        cv2.imwrite(folder_name_img + image_name, blur)
        