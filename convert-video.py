#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 17:25:48 2021

@author: luangustavo
"""


from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np

import os
import cv2

image_frames = 'image_frames'


def files():
    try:
        os.remove(image_frames)
    except OSError:
        pass
        
    
    if not os.path.exists(image_frames):
        os.makedirs(image_frames)

    src_vid = cv2.VideoCapture('simulador-oracle.mp4')
    return(src_vid)


def process(src_vid):

    index = 0
    while src_vid.isOpened():
        ret, frames = src_vid.read()
        if not ret:
            break
        

        name = './image_frames/frames' + str(index) + '.png'

        if index % 700 == 0:
            print('Extraindo frames...' + name)
            cv2.imwrite(name, frames)
        index = index + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    src_vid.release()
    cv2.destroyAllWindows()

def get_text():
    for i in os.listdir(image_frames):
        #print(str(i))
        my_example = Image.open(image_frames + "/" + i)
        text = pytesseract.image_to_string(my_example, lang='eng')

        print(text)

if __name__ == '__main__':
    vid = files()
    process(vid)
    get_text()

