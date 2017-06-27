import os 
import numpy as np
from PyQt5.QtWidgets import *


class routine:
    def __init__(self,parent):
        self.parent=parent
        print(parent.data_viewer.get_selectedPaths())
            
