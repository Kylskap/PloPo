import os 
import numpy as np
from PyQt5.QtWidgets import *


class routine:
    def __init__(self,parent):
        self.parent=parent
        self.parent.list_stepWindows[0].renewLists()
        self.Datasets=parent.list_stepWindows[0].Datasets
        for step in self.parent.list_stepWindows[0].Steps:
             step.function.function(self) # die Funktionen sollen innerhalb der routine laufen und unabhaengig von der UI funktionieren.
            
