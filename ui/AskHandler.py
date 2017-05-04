# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:33:12 2015

@author: tobias
"""

import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
import PyQt5

    
class AskHandler(QDialog):
    
    def __init__(self,root):
        
        QWidget.__init__(self,root)
                
        self.closed = PyQt5.QtCore.pyqtSignal
        self.setModal(True)

        
        self.resize(500,180)
        self.setWindowTitle('Handler')
        self.root = root
        self.root.hide()
        self.main_layout = QGridLayout(self)        
        self.main_layout.addWidget(QLabel('Choose Data handler: ',self),0,0,1,2)        
        dir_button1 = QPushButton(self,text='path')
        
        self.finish_button = QPushButton(self,text='finish')
        self.finish_button.setSizeIncrement(1,1)
        
        #self.finish_button.
        self.workdir_reader = QLineEdit(self)
        self.workdir_reader.setText(self.cfg.get('Directories','working_directory'))
        
        
        self.main_layout.addWidget(self.workdir_reader,1,1,1,1)
        self.main_layout.addWidget(dir_button1,1,2,1,1)

        self.main_layout.addWidget(self.finish_button,4,1,1,1)
        #button.show()    
        
        def work_directory():
            self.ask_directory(self.workdir_reader)
        def save_directory():
            self.ask_directory(self.savedir_reader)
            
        self.connect(dir_button1, SIGNAL('clicked()'), work_directory)
        self.connect(dir_button2, SIGNAL('clicked()'), save_directory)
        self.connect(self.finish_button, SIGNAL('clicked()'), self.finish)
        
        self.show()

    def __del__(self):        
        pass
            
    def ask_directory(self, qobject):    
        
        Dir = QFileDialog.getExistingDirectory(self, "Open Directory",qobject.text(),QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        qobject.setText(Dir)
                
    def finish(self):
        
        work_dir=self.workdir_reader.text()
        save_dir=self.savedir_reader.text()
        
        if os.path.isdir(work_dir) and os.path.isdir(save_dir): 
            self.cfg.set('Directories','working_directory',work_dir)
            self.cfg.set('Directories','saving_directory',save_dir)
            with open('setup.cfg', 'wb') as configfile:
                self.cfg.write(configfile)
            try:
                #self.root.set_workingDir(work_dir)
                #self.root.set_savingDir(save_dir)
                
                self.is_set=True
                self.destroy()
                self.emit(SIGNAL('closed()'))                
            except:
                print 'second'
                self.error()
        else:
            print 'first'
            self.error()
            
    def error(self):
        message = QErrorMessage(self)
        message.setWindowTitle('I am Error')
        message.showMessage('no valid directory chosen!')