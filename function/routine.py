import os 
import numpy as np


class routine:
    def __init__(self,root):
        self.root=root
        for root,dirs,files in os.walk('./__testcase/Testdaten'):
            for file in files:
                print(os.path.join(root, file))
