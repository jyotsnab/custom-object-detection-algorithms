# -*- coding: utf-8 -*-
"""
Created on Fri Jun 1 08:54:55 2018

@author: jyotsnab
"""

opencv_createsamples -img positive_images\find_phone-cropped/62.jpg -bg negative_images/negatives.txt -info positive_images/cropped60.txt -num 128 -maxxangle 0.0 -maxyangle 0.0 -maxzangle 0.3 -bgcolor 255 -bgthresh 8 -w 20 -h 20
