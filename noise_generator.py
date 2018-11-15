import cv2
import os
from os import listdir
from random import shuffle
from math import floor

# import shutil

import numpy as np


def noisy(noise_typ, image):
    if noise_typ == "gauss":
        row, col, ch = image.shape
        mean = 0
        var = 0.1
        sigma = var ** 0.5
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        noisy = image + gauss
        return noisy
    elif noise_typ == "s&p":
        row, col, ch = image.shape
        s_vs_p = 0.5
        amount = 0.01
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                  for i in image.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy
    elif noise_typ == "speckle":
        row, col, ch = image.shape
        gauss = np.random.randn(row, col, ch)
        gauss = gauss.reshape(row, col, ch)
        noisy = image + image * gauss
        return noisy


def noise_add_function(root_dir, dest_dir):
    os.mkdir(dest_dir)
    for em in ['AF', 'AN', 'DI', 'HA', 'NE', 'SA', 'SU']:
        if not os.path.exists(dest_dir + '\\' + em):
            os.mkdir(dest_dir + '\\' + em)
        images = listdir(root_dir + '\\' + em)
        for image in images:
            img = cv2.imread(root_dir + '\\' + em + '\\' + image)
            outimg = noisy(noise_type, img)
            cv2.imwrite(dest_dir + '\\' + em + '\\' + image, outimg)


noise_type = "speckle"
root_dir = "E:\\Datasets\\KDEF_and_AKDEF\\data\\test"
dest_dir = "E:\\Datasets\\KDEF_and_AKDEF\data\\" + noise_type

noise_add_function(root_dir, dest_dir)
