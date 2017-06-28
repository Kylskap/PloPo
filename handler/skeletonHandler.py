# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:17:40 2017

@author: ZechT
"""

import numpy as np

import handler.AbstractHandler as AbstractHandler

class skeletonHandler(AbstractHandler):
    
    def __init__(self,root):
        AbstractHandler.__init__(self)
        
        
        
    
    
def main():
        # Create an PyQT5 application object.
    a = QApplication(sys.argv)

        # The QWidget widget is the base class of all user interface objects in PyQt5.    
    c = QWidget()
    w = skeletonHandler(c)
    w.setFixedSize(395,395)   

        # Set window title
    w.setWindowTitle("Widget")

        # Show window
    w.show()

    sys.exit(a.exec_())


if __name__ == "__main__":
    main()