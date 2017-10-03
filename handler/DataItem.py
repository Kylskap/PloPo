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
import handler.AbstractHandler as Handler

class DataItem(QTreeWidgetItem):
    
    def __init__(self,root=None):
        QTreeWidgetItem.__init__(self)
        
        self.handler = None
        self.path = None
        self.data = None
        self.comment = None
        
    def dragMoveEvent(self,e):
        pass
    
    def readData(self):
        if self.data is None:
            print(self.path)
            print(self.handler)
            inst_handler = Handler.AbstractHandler(path=self.path,read_function=self.handler)
            print(2)
            self.data = inst_handler.readData()