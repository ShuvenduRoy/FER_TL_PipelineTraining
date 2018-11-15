import cv2
import os
from os import listdir
from random import shuffle
from math import floor 

import shutil



def get_train_test(data_list):
    split = 0.9
    index = floor(len(data_list)*split)
    training_data = data_list[:index]
    testing_data = data_list[index:]
    return training_data, testing_data


def test_train_split(root_dir,train_dir,test_dir):
    path_images = listdir(root_dir)

    an = []
    af = []
    di = []
    ha = []
    ne = []
    sa = []
    su = []

    for image in path_images:
        if(image[3:5]=='AN'):
            an.append(image)
        elif(image[3:5]=='FE'):
            af.append(image)
        elif(image[3:5]=='DI'):
            di.append(image)
        elif(image[3:5]=='HA'):
            ha.append(image)
        elif(image[3:5]=='NE'):
            ne.append(image)
        elif(image[3:5]=='SA'):
            sa.append(image)
        elif(image[3:5]=='SU'):
            su.append(image)
        else:
            print(image)
        

    image_dict = {"AN":an,"AF":af,"DI":di,"HA":ha,"NE":ne,"SA":sa,"SU":su}  


      
    for keys in image_dict:
        shuffle(image_dict[keys])
        training_data, testing_data = get_train_test(image_dict[keys])
        for i_image in training_data:
            dst_an = train_dir+"/"+keys
            src_an = root_dir+"/"+i_image
            img = cv2.imread(src_an)
            #shutil.copy(src_an,dst_an)
            cv2.imwrite(dst_an+'/'+i_image[:-4]+'jpg', img)
    
        for i_image in testing_data:
            dst_an = test_dir+"/"+keys
            src_an = root_dir+"/"+i_image
            img = cv2.imread(src_an)
            #shutil.copy(src_an,dst_an)
            cv2.imwrite(dst_an+'/'+i_image[:-4]+'jpg', img)
        
        
        
source_dir =  "jaffe"
train_dir = "data/train"
test_dir = "data/test"
    
test_train_split(source_dir, train_dir, test_dir) 
        

