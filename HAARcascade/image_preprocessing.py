# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:31:06 2018

@author: jyotsnab
"""

import cv2
import os
import numpy as np
from glob import glob



def pre_process(img_path,save_path,save_folder,img_type='pos'):
    """
    Parameters:
    -----------        
    img_path = folder path containing
    save_path = folder path to save processed images
    img_type = 'pos' or 'neg'
    'pos' for positive images
    'neg' for negative images
    
    Returns:
    --------
    None: 
        image are pre-processed and saved at 'save_path' folder.
        
    """
    if img_type == 'pos':
        
        print('Done!')
        
    elif img_type == 'neg':
    print('Done!')
    
    img_files = glob(img_path+'/*.jpg')
    for image in img_files:
        img = cv2.imread(image,cv2.IMREAD_GRAYSCALE)
        resized_img = cv2.resize(img,(100,100))
        cv2.imwrite(save_path+"/"+save_folder+"/"+image,resized_img)
    
    os.chdir(save_path)
    filenames = glob(save_folder+'/*.jpg')
    if img_type == 'pos':
        thefile=open(os.getcwd()+'/'+img_type+'.dat','w')
    elif img_type == 'neg'
        thefile=open(os.getcwd()+'/'+img_type+'.txt','w')
    
    for item in filenames:
        thefile.write("%s\n" % item)

    thefile.close()
    
        
    

    