# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:33:12 2015

@author: tobias
"""
#import ResonanceData

import sys,os

#sys.path.append(r'C:\Users\ZechT\git\PloPo')

from PyQt5.QtWidgets import *

import ui.MainFramework as MainFramework

import configparser

def main():
    
    version = '0.1'###
        #Create initial config when no config existing
    
    if not os.path.isfile("config.cfg"):
        
        config = ConfigParser.RawConfigParser()
        
        # When adding sections or items, add them in the reverse order of
        # how you want them to be displayed in the actual file.
        # In addition, please note that using RawConfigParser's and the raw
        # mode of ConfigParser's respective set functions, you can assign
        # non-string values to keys internally, but will receive an error
        # when attempting to write to a file or when you get it in non-raw
        # mode. SafeConfigParser does not allow such assignments to take place.
        config.add_section('dirs')
        config.set('dirs','home_directory',r'C:\Users\ZechT\git\PloPo_Init')
        config.set('dirs','working_directory',r'C:\Users\ZechT\git\PloPo_Init')
        config.set('dirs','saving_directory',r'C:\Users\ZechT\git\PloPo_Init')
        
        config.add_section('info')
        config.set('info', 'version', version)
        config.set('info', 'name', 'PloPo')
        config.set('info', 'description', 'Scientific data management and analysis interface with integrated plot generator.')
        config.set('info', 'authors', 'MaPo, ToZe')
        config.set('info', 'copyright', 'GnuCopyright Licence')
        
        # Writing our configuration file to 'example.cfg'
        with open('config.cfg', 'wb') as configfile:
            config.write(configfile)
        
    
        # Create an PyQT4 application object.
    a = QApplication(sys.argv)

        # The QWidget widget is the base class of all user interface objects in PyQt4.
    w = MainFramework.MainFramework()
    #w = QMainWindow()


        # Set window title
    w.setWindowTitle("PloPo V"+version)

        # Show window
    w.show()

    sys.exit(a.exec_())


if __name__ == "__main__":
    main()
