import os 
import numpy as np
from PyQt5.QtWidgets import *
from handler.datLoad import datLoad
import matplotlib.pyplot as plt

class routine:
    def __init__(self,parent):
        self.parent=parent
        list_Data = parent.data_viewer.get_selectedPaths()
        for iDir in list_Data:
            datLoad(iDir)
        
        
            
            
