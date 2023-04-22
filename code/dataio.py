import numpy as np
import json
import shutil
import os

path = '../dataset_test_rgb_small/'
folder_name_img = path + 'val/images/'
folder_name_lab = path + 'val/labels/'

for folder_name in (folder_name_img, folder_name_lab):
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")
    
with open(path+'test.json', 'r') as json_file:
    json_data = json.load(json_file)
    
for i, data in enumerate(json_data):
    id = data['path'][-9: -4]
    src = path + f'rgb/test/{id}.png'
    dst = path + f'val/images/{id}.png'
    shutil.move(src, dst)
    with open(path + f'val/labels/{id}.txt', 'w') as file:
        for boxes in data['boxes']:
            x_max, x_min, y_max, y_min = boxes['x_max'], boxes['x_min'], boxes['y_max'], boxes['y_min']
            x_center, y_center = (x_max + x_min) / (1280 * 2), (y_max + y_min) / (720 * 2)
            width, hight = (x_max - x_min) / 1280, (y_max - y_min) / 720
            line = f'9 {x_center} {y_center} {width} {hight}\n'
            file.write(line)
        