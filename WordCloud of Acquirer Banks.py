#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
WordCloud of Acquirer Bank
Created on Wed Nov 13 15:03:13 2018

@author: fay
"""
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from PIL import Image
import numpy as np
import os

base_path='/Users/fay/Desktop/3-Tech/AFPD Projects/WordCloud'

# 🌟Read string from txt
banknames = open(base_path + os.sep + 'bankname.txt','r').read()
## encoding = UTF-8, a whole str with separator

# 🌟Shape: from a picture (transparent background png)
## Default rectangle
mask = Image.open(base_path+os.sep+'icon.png')
mask = np.array(mask) # get the color of mask image

# 🌟Color: from the picture
color_func = ImageColorGenerator(mask) # Arrary based on RGB

# 🌟Font: for En & Ch
font = base_path + os.sep + 'SNsanafonGyou.ttf'

# ❗️Build a wordcloud
wc = WordCloud(font_path=font, background_color="black", max_words=4000, mask=mask, max_font_size=300, color_func=color_func)
## width=400,height=200; max number of words; stopwords; 
wc.generate_from_text(banknames) # seperate words from str

wc.to_file(base_path + os.sep + 'wordcloud.png')