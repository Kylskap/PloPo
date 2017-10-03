# -*- coding: utf-8 -*-
"""
Created on Thu May 04 19:53:03 2017

@author: ZechT
"""
import sys, os

import numpy as np

import importlib

from PyQt5.QtWidgets import *


class AbstractHandler(QWidget):
    
    def __init__(self,parent=None,path=None,data=None,read_function=None,edit_function=None):
        QWidget.__init__(self)
        self.parent=parent
        
        self.path = path
        self.data = data
        self.setReadFunction(read_function)
        #self.edit_function = edit_function
        
    def setData(self,directory):
        self.path = directory
        self.data = [dI for dI in os.listdir(directory) if os.path.isdir(os.path.join(directory,dI))]
        
    def exportData(self):
        return self.path,self.data
    
    def importData(self,path,data):
        self.path = path
        self.data = data
        
    def readData(self):
        print(3)
        data = self.read_function.reader(self.path)
        print(4)
                         
        return data
    
    def setEditFunction(self,function):
        self.edit_function = function    
        
    def setReadFunction(self,function):
        print('X')
        self.read_function=importlib.import_module('handler.reader.'+function+'_Reader')
        

        
        

def main():
        # Create an PyQT5 application object.
    a = QApplication(sys.argv)
    os.chdir('../')
        # The QWidget widget is the base class of all user interface objects in PyQt5.    
    c = QWidget()
    w = AbstractHandler(c)
    w.setFixedSize(395,395)   

        # Set window title
    w.setWindowTitle("Widget")

        # Show window
    w.show()

    sys.exit(a.exec_())


if __name__ == "__main__":
    main()
        
    