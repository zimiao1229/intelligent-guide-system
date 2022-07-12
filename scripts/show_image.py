''' 

        Copyright (C) 2018-2022 East China Normal University
        All rights reserved

        filename: show_image.py
        description :


'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os

from IPython.display import Image, HTML, display

    
root = "tf_files/flower_photos/"
with open(root+"/LICENSE.txt") as f:
    attributions = f.readlines()[4:]
attributions = [line.split(' CC-BY') for line in attributions]
attributions = dict(attributions)
    
def show_image(image_path):
    display(Image(image_path))
    
    image_rel = image_path.replace(root,'')
    caption = "Image " + ' - '.join(attributions[image_rel].split(' - ')[:-1])
    display(HTML("<div>%s</div>" % caption))
