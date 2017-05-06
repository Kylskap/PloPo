# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 18:30:32 2017

@author: ZechT
"""

import os, sys

import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#import ConfigParser

class DirTreeWidget(QTreeWidget):
    
    def __init__(self,root,directory=None):
        QTreeWidget.__init__(self)
        self.root = root
        
        self.setSelectionMode(QAbstractItemView.MultiSelection)
        #self.config = ConfigParser.RawConfigParser()
        ####self.config.read('config.cfg')
        #self.home = self.config.get('Section1','home_directory')        
        
        self.file_icon = QIcon(r'ui\icons\File-64.png')
        self.folder_icon = QIcon(r'ui\icons\Folder-64.png')
        
        self.setAcceptDrops(True)
        
        if directory!=None:
            self.addDirectory(directory)
        self.show()    
    
    def addDirectory(self,directory):
        
        list_dir = []
        for iItem in os.walk(directory):
            list_dir.append(iItem)
        
        print(os.path.split(directory))
        
        main_item = QTreeWidgetItem()
        main_item.setText(0,os.path.split(directory)[1])
        main_item.setIcon(0,self.folder_icon) 
        main_item.setText(1,os.path.split(directory)[0])
        self.addTopLevelItem(main_item)
        
        dict_temp = {}
        
        dict_temp[directory] = main_item
        
        for iItem in list_dir:
            for iFolder in iItem[1]:
                item = QTreeWidgetItem()
                item.setText(0,iFolder)
                item.setIcon(0,self.folder_icon)
                dict_temp[os.path.join(iItem[0],iFolder)]=item
                dict_temp[iItem[0]].addChild(item)
            for iFile in iItem[2]:
                item = QTreeWidgetItem()
                item.setText(0,iFile)
                item.setIcon(0,self.file_icon)
                dict_temp[iItem[0]].addChild(item)
                
        del dict_temp
                

        
        
    def dragEnterEvent(self,e):
        if e.mimeData().hasUrls:            
            e.accept()            
        else:
            e.ignore()
    
    def dropEvent(self,e):
        for iUrl in e.mimeData().urls():
            print(iUrl.path())
            self.addDirectory(iUrl.path().strip('/'))
        
    def dragMoveEvent(self,e):
        pass
    
    
def main():
        # Create an PyQT5 application object.
    a = QApplication(sys.argv)

        # The QWidget widget is the base class of all user interface objects in PyQt5.    
    centralWidget = QWidget()
    tree = DirTreeWidget(centralWidget,r"C:\Users\ZechT\git")
    tree.setFixedSize(395,395)
    

        # Set window title
    tree.setWindowTitle("DirTreeWidget")

        # Show window
    tree.show()

    sys.exit(a.exec_())


if __name__ == "__main__":
    main()