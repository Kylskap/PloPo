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

import ui.DirTreeWidget as DirTreeWidget
import ui.Steps as Steps

import configparser

class MainFramework(QMainWindow):
    
    
    def __init__(self,parent=None):
        QMainWindow.__init__(self, parent)        
        
        self.config = configparser.RawConfigParser()
        self.config.read(os.name+'_config.cfg')
        self.home = self.config.get('dirs','home_directory')
        self.icon_directory = self.config.get('dirs','icon_directory')
        print(self.home)
       
        self.setMinimumSize(300,250)
        self.root = QWidget(self)        
        self.root.show()    
        
        self.tool_tab_dict = {}
        self.working_dir=self.config.get('dirs','working_directory')
        self.saving_dir=self.config.get('dirs','saving_directory')
        self.dockiterator = 1
        
        self.list_stepWindows = []
        
        self.init_Menubar() 
        self.init_Gui() 
        self.init_Toolbar()
        
        #self.dir_popup = AskWindow.AskWindow(self)
        #self.dir_popup.closed.connect(self.init_Data)
        #self.connect(self.dir_popup,SIGNAL('closed()'),self.init_Data)  
        
        self.settings = QSettings("last_session", "PloPoV0.1")
        
        
    def init_Menubar(self):
        def hello():
            pass
            
        self.menubar = QMenuBar(self)
        
        # create a pulldown menu, and add it to the menu bar
        filemenu = QMenu('File', self.menubar)
        filemenu.addAction(self.add_MenuAction(self.menubar,'Open',hello))
        filemenu.addAction(self.add_MenuAction(self.menubar,'Save',hello))
        filemenu.addAction(self.add_MenuAction(self.menubar,'Export',hello))
        filemenu.addSeparator()
        filemenu.addAction(self.add_MenuAction(self.menubar,'Quit',self.close))
        self.menubar.addMenu(filemenu)
        
        
        # create pulldown menus for analysis choices:
        modemenu = QMenu('Mode', self.menubar)
        eventanalysismenu = QMenu('Event Analysis', self.menubar)

        modemenu.addMenu(eventanalysismenu)

        self.menubar.addMenu(modemenu)
        
        viewmenu = QMenu('View', self.menubar)
        viewmenu.addAction(self.add_MenuAction(self.menubar,'reset',hello))        
        
        self.menubar.addMenu(viewmenu)
        self.setMenuBar(self.menubar)
        self.menubar.show()
        
    def add_MenuAction(self, menu, actionString, function, shortcut = '', statusTip = ''):
        
        newAction = QAction(  actionString, menu)
        newAction.setShortcut( shortcut )
        newAction.setStatusTip( statusTip ) 
        newAction.triggered.connect(function)
        #self.connect( newAction, SIGNAL('triggered()'), function )
        
        return newAction
    
    def init_Toolbar(self):
        
        def set_AnaMode():
            pass
            #if self.anamode_box.currentText() == '  generic analysis':
            #    self.set_Mode('Generic Analysis')
            #if self.anamode_box.currentText() == '  spike analysis':
            #    self.set_Mode('Spike Analysis')
            #if self.anamode_box.currentText() == '  step analysis':
            #    self.set_Mode('Step Analysis')
            #if self.anamode_box.currentText() == '  modesplit analysis':
            #    self.set_Mode('ModeSplitAnalysis')
        
        self.toolbar = QToolBar(self)
        self.toolbar.setObjectName("toolbar")
        
        self.anamode_box = QComboBox(self.toolbar)
        self.anamode_box.addItem('Event Analysis')
        self.anamode_box.model().item(0).setEnabled(False)
        self.anamode_box.addItem('  generic analysis')
        self.anamode_box.addItem('  spike analysis')
        self.anamode_box.addItem('  step analysis')
        self.anamode_box.addItem('  modesplit analysis')
        self.anamode_box.insertSeparator(5)
        self.anamode_box.setCurrentIndex(1)
        
        self.read_button = QPushButton(QIcon(self.home+self.icon_directory+'Play-64.png'),'Play',self)
        self.read_button.setMinimumSize(10,10)
        #self.read_button.clicked.connect(self.compute)
        open_button = QPushButton(QIcon(self.home+self.icon_directory+'Open-Folder-64.png'),'Open',self)
        open_button.setMinimumSize(10,10)
        #self.open_button.clicked.connect(self.ask_WorkingDirectory)
        save_button = QPushButton(QIcon(self.home+self.icon_directory+'Save-64.png'),'Save',self)
        save_button.setMinimumSize(10,10)
        #self.connect(save_button, SIGNAL('clicked()'),self.save)   
        export_button = QPushButton(QIcon(self.home+self.icon_directory+'Export-64.png'),'Export',self)
        export_button.setMinimumSize(10,10)
        #self.connect(export_button, SIGNAL('clicked()'),self.export)    
        import_button = QPushButton(QIcon(self.home+self.icon_directory+'Import-64.png'),'Export',self)
        import_button.setMinimumSize(10,10)
        #self.root.connect(self.anamode_box, SIGNAL('activated()'), self.set_AnaMode)
        #self.anamode_box.currentIndexChanged.connect(set_AnaMode)
        #self.root.connect(self.anamode_box,SIGNAL('currentIndexChanged(int)'),set_AnaMode)
        self.label_directory = QLabel(self.working_dir)
        self.toolbar.addWidget(open_button)
        self.toolbar.addWidget(save_button)
        self.toolbar.addWidget(export_button)
        self.toolbar.addWidget(import_button)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.anamode_box)
        self.toolbar.addWidget(self.read_button)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.label_directory)
        

        self.addToolBar(self.toolbar)
        
    def init_Gui(self):
        
        self.tooltabdock = QWidget()
        self.tooltabdock.setAccessibleName("tools")  
        
        self.list_stepWindows.append(Steps.Loop())
                
        self.data_viewer = DirTreeWidget.DirTreeWidget(self,self.working_dir)
        self.data_viewer.setAccessibleName("data")
        self.data_viewer.setMaximumWidth(350)
        self.data_viewer.setSelectionMode(QAbstractItemView.MultiSelection)
        
        self.info_frame = QTextEdit(self)
        self.info_frame.setAccessibleName("info")
        self.info_frame.setMaximumWidth(350)      
        
        dockWidget = self.add_WidgettoDock(Qt.LeftDockWidgetArea, self.data_viewer)
        dockWidget = self.add_WidgettoDock(Qt.LeftDockWidgetArea, self.tooltabdock)
        dockWidget = self.add_WidgettoDock(Qt.LeftDockWidgetArea, self.info_frame,dockWidget)
        
        self.add_WidgettoDock(Qt.RightDockWidgetArea, self.list_stepWindows[0])
        
    def add_WidgettoDock(self,position,Widget,prevDock=None):
        
        dockWidget = QDockWidget(Widget.accessibleName())
        dockWidget.setWidget(Widget)
        self.addDockWidget(position,dockWidget)
        if prevDock:
            self.tabifyDockWidget(prevDock,dockWidget)
        return dockWidget