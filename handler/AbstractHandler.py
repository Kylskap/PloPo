# -*- coding: utf-8 -*-
"""
Created on Thu May 04 19:53:03 2017

@author: ZechT
"""
import sys, os

import numpy as np

from PyQt5.QtWidgets import *


class AbstractHandler(QWidget):
    
    def __init__(self,parent=None):
        QWidget.__init__(self)
        self.parent=parent
        
        self.main_dir = None
        self.data = None
        self.read_function = None
        self.edit_function = None
        
    def setData(self,directory):
        self.main_dir = directory
        self.data = [dI for dI in os.listdir(directory) if os.path.isdir(os.path.join(directory,dI))]
        
    def exportData(self):
        return self.main_dir,self.data
    
    def importData(self,main_dir,data):
        self.main_dir = main_dir
        self.data = data
        
    def readData(self,dirs):
        
        if self.read_function==None:
            return 0
        
        data = {}
        if dirs==self.main_dir:
            self.read_function(self.data)
        elif np.asarray(dirs):
            for iDir in dirs:
                if os.path.isdir(iDir):
                    data['iDir']=self.read_function(iDir)                    
        return data
        
    def editData(self,Dir):
        
        if self.edit_function==None:
            return 0
        
        if os.path.isdir(Dir):
            self.edit_function(Dir)
            
    
    def setEditFunction(self,function):
        self.edit_function = function    
        
    def setReadFunction(self,function):
        self.read_function = function

        
        

def main():
        # Create an PyQT5 application object.
    a = QApplication(sys.argv)

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
        
    