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
from function.routine import routine

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
        
        newAction = QAction(actionString,menu)
        newAction.setShortcut( shortcut )
        newAction.setStatusTip( statusTip ) 
        newAction.triggered.connect(function)
        #self.connect( newAction, SIGNAL('triggered()'), function )
        
        return newAction
    
    def add_MenuButton(self, toolbar, icon, function=None, tooltip=None):
        
        button = QPushButton(icon,'',parent=self)
        button.setMinimumSize(20,20)
        if tooltip:
            button.setToolTip(tooltip)
        if function:
            button.clicked.connect(function)
        toolbar.addWidget(button)
        
    
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
       
        # open button
        self.add_MenuButton(self.toolbar,QIcon(self.home+self.icon_directory+'Open-Folder-64.png'),tooltip='Open')
        # save button
        self.add_MenuButton(self.toolbar,QIcon(self.home+self.icon_directory+'Save-64.png'),tooltip='Save')
        # Export button
        self.add_MenuButton(self.toolbar,QIcon(self.home+self.icon_directory+'Export-64.png'),tooltip='Export')
        # import button
        self.add_MenuButton(self.toolbar,QIcon(self.home+self.icon_directory+'Import-64.png'),tooltip='Import')

        #self.root.connect(self.anamode_box, SIGNAL('activated()'), self.set_AnaMode)
        #self.anamode_box.currentIndexChanged.connect(set_AnaMode)
        #self.root.connect(self.anamode_box,SIGNAL('currentIndexChanged(int)'),set_AnaMode)
        self.label_directory = QLabel(self.working_dir)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.anamode_box) 
        # read button
        self.add_MenuButton(self.toolbar,QIcon(self.home+self.icon_directory+'Play-64.png'),tooltip='Play',function=self.do_routine)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.label_directory)
        

        self.addToolBar(self.toolbar)
        
    def init_Gui(self):
        
        self.tooltabdock = QWidget()
        self.tooltabdock.setAccessibleName("tools")  
        
        self.list_stepWindows.append(Steps.Loop())
                
        self.data_viewer = DirTreeWidget.DirTreeWidget(self,self.working_dir)
        self.data_viewer.setAccessibleName("data")
        self.data_viewer.setMinimumSize(50,50)

        self.data_viewer.setSelectionMode(QAbstractItemView.MultiSelection)
        
        self.info_frame = QTextEdit(self)
        self.info_frame.setAccessibleName("info")
        self.info_frame.setMinimumSize(50,50)      
        
        dockWidget = self.add_WidgettoDock(Qt.LeftDockWidgetArea, self.data_viewer,size=QSize(500,500))
        dockWidget = self.add_WidgettoDock(Qt.LeftDockWidgetArea, self.tooltabdock,size=QSize(500,500))
        dockWidget = self.add_WidgettoDock(Qt.LeftDockWidgetArea, self.info_frame,dockWidget,size=QSize(500,500))
        
        self.add_WidgettoDock(Qt.RightDockWidgetArea, self.list_stepWindows[0])
        
    def add_WidgettoDock(self,position,Widget,prevDock=None,size=None):
        
        dockWidget = QDockWidget(Widget.accessibleName())
        dockWidget.setWidget(Widget)
        self.addDockWidget(position,dockWidget)
        if size:
            dockWidget.setMaximumSize(size)
        if prevDock:
            self.tabifyDockWidget(prevDock,dockWidget)
        return dockWidget
        

    def do_routine(self):        
        list_data = routine(self)
        
