# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 14:17:00 2016

@author: tobias
"""

import os, sys,sip

import numpy as np
import scipy.signal as signal
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DirTreeWidget(QTreeWidget):
    
    def __init__(self,root,directory=None):
        QTreeWidget.__init__(self)
        self.root = root
        self.directories_list = []
        self.setSelectionMode(QAbstractItemView.MultiSelection)
        self.selectedList = []
        headerItem = QTreeWidgetItem()
        headerItem.setText(0,"File Name")
        self.file_icon = QIcon("C:\Users\ZechT\git\PloPo_Init\ui\icons\file-icon.png")
        self.folder_icon = QIcon("C:\Users\ZechT\git\PloPo_Init\ui\icons\folder-icon.png")
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        
        self.setHeaderItem(headerItem)
        
        if (directory != None):
            self.directories_list.append(directory)
            self.initDirectory()        
        
        self.itemClicked.connect(self.showDirectory)
        #self.connect(self,SIGNAL("itemClicked(QTreeWidgetItem*, int)"),self.showDirectory)
        self.show()
        
    def initDirectory(self):
        self.clear()
        
        for iDir in self.directories_list:
            filesList = iDir.entryInfoList()
            print(iDir.path())
            for fileInfo in filesList[2:]:
                item = QTreeWidgetItem()
                item.setText(0,fileInfo.fileName())
                
                if(fileInfo.isFile()):
                    item.setText(1,str(fileInfo.size()))
                    item.setIcon(0,self.file_icon) 
                    item.setText(2,fileInfo.filePath())
                if(fileInfo.isDir()):
                    item.setIcon(0,self.folder_icon)
                    self.addTopLevelItem(item,fileInfo.filePath())
                item.setText(2,fileInfo.filePath())
                self.addTopLevelItem(item)
            
            pass
        
        
    def addDirectory(self, directory):
        self.directories_list.append(QDir(directory))
        filesList=self.directories_list[-1].entryInfoList()
        for fileInfo in filesList[2:]:
            
            item = QTreeWidgetItem()
            item.setText(0,fileInfo.fileName())
            
            if(fileInfo.isFile()):
                item.setText(1,str(fileInfo.size()))
                item.setIcon(0,self.file_icon) 
                item.setText(2,fileInfo.filePath())
            if(fileInfo.isDir()):
                item.setIcon(0,self.folder_icon)
                self.addChildren(item,fileInfo.filePath())
            item.setText(2,fileInfo.filePath())
            self.addTopLevelItem(item)
        
    def removeDirectory(self, directory):
        self.directories_list.remove(QDir(directory))
        self.initDirectory()        
        
    def showDirectory(self,item,column):

        rootDir = QDir(item.text(2))
        filesList = rootDir.entryInfoList()
        
        if len(filesList) == item.childCount():
            return 0
        
        for fileInfo in filesList[2:]:
            
            child = QTreeWidgetItem()
            child.setText(0,fileInfo.fileName())
            
            if(fileInfo.isFile()):
                child.setText(1,str(fileInfo.size()))
                child.setIcon(0,self.file_icon)
                child.setText(2,fileInfo.filePath())
            if(fileInfo.isDir()):
                child.setIcon(0,self.folder_icon)
                child.setText(2,fileInfo.filePath())
            item.addChild(child)
      
        
        
    def addChildren(self,item,path):
        
        rootDir = QDir(path)
        filesList = rootDir.entryInfoList()
        
        for fileInfo in filesList[2:]:
            
            child = QTreeWidgetItem()
            child.setText(0,fileInfo.fileName())
            
            if(fileInfo.isFile()):
                child.setText(1,str(fileInfo.size()))
                child.setText(2,fileInfo.filePath())
            if(fileInfo.isDir()):
                child.setIcon(0,self.folder_icon)
                child.setText(2,fileInfo.filePath())
            item.addChild(child)
            
        pass
            
    def getSelectedItems(self):
        self.selectedList=[]
        selectedList = self.selectedItems()
        for item in selectedList:
            self.selectedList.append(item.text(2))
        return self.selectedList


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
    tree = DirTreeWidget(centralWidget,None)
    tree.setFixedSize(395,395)
    

        # Set window title
    tree.setWindowTitle("DirTreeWidget")

        # Show window
    tree.show()

    sys.exit(a.exec_())


if __name__ == "__main__":
    main()
