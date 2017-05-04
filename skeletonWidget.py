# -*- coding: utf-8 -*-
"""
Created on Thu May 04 19:53:03 2017

@author: ZechT
"""
import sys

import numpy as np

from PyQt5.QtWidgets import *


class AbstractHandler(QWidget):
    
    def __init__(self,parent=None):
        QWidget.__init__(self)
        self.parent=parent
        
        

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
        
    