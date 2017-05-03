# -*- coding: utf-8 -*-
"""
Created on Wed May 03 20:32:07 2017

@author: ZechT
"""

import os

import numpy as np

test_dir = "C:\Users\ZechT\git"

list_dir = os.walk(test_dir)

list_dir = []

for x in os.walk(test_dir):
    list_dir.append(x)