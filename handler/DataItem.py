# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 18:58:00 2017

@author: ZechT
"""

import os, sys

import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import configparser

class DataItem(QTreeWidgetItem):
    
    def __init__(self,root=None):
        QTreeWidgetItem.__init__(self)
        
        self.handler = None
        self.path = None
        
    def dragMoveEvent(self,e):
        pass