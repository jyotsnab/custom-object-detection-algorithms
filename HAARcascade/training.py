# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:07:15 2018

@author: jyotsnab

Haar Cascade for object detection
=================================
Notes:
1) It is assumed the script run from the path of the folder containing this script.
2) For a collection of negative images, I have manually cropped images within 
find_phone, however random baground images can be downloaded online and 
automated in this script.

Following steps are performed:
    1) identify right folders
    2) pre-process negative and positive images
    3) Create more positive samples 
"""

#import libraries
import os
import subprocess
import cv2
import numpy as np
from glob import glob
from image_preprocessing import pre_process


def main():
    """
    Note:
    Download/save negative images in "negative_images" folder.
    For positive images, manually mark ROI (region of interest) and save in the 
    format: <image path> <number of objects> <ROI_xmin ROI_ymin  ROI_width ROI_height>
    and save as 'positive_images/positives.txt'
    Example. positive_images/05.jpg 1 56 70 05 06
    And save few cropped images of phone at "cropped_images" folder
    
    """
    # make directories
    folders = ['find_phone','negative_images', 'cropped_images']
    
    for folder in folders:
        try: 
            os.stat(folder)
            if folder == "find_phone":
                os.rename("find_phone","positive_images")
        except:
            os.mkdir(folder)
            
    
    #preprocessing images
    pre_process('positive_images',os.getcwd(),'positive_images',img_type='pos')
    pre_process('negative_images',os.getcwd(),'negative_images',img_type='neg')
   
    """ create a """
    os.system("sh create_samlples.sh")
    
    #merge descripter files of newly generated positive images into one txt
    
    # =============================================================================
    # #Train Cascade
    # =============================================================================
    

if __name__ == "__main__":
    print("Begin training HaarCascade Model")
    main()
    
