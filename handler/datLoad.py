## a function which gets a path as argument and returns the data 

import numpy as np 
import matplotlib.pyplot as plt

class datload:
    def __init__(self,dirpath):
        self.dirpath=dirpath
        self.data={}

## lese jetzt Daten ein
        with open (self.dirpath, 'r') as dirfile:
            
            dirstringlines=dirfile.readlines()
            dirstring=dirfile.read()
        ## finde delimiter String heraus:
        delimiterStrings=['\t',',',';']
        columnNumberList=[]
        rowNumberList=[]
        delimiter=delimiterStrings[0]
        for i in range(len(delimiterStrings)):
            columnlist=[]
            allcolumnlist=[]
            for j in range(len(dirstringlines)):
                columns=len(dirstringlines[j].split(delimiterStrings[i]))
                if not columns ==1:
                     columnlist.append(columns)
                allcolumnlist.append(columns)
            rowNumberList.append(len(columnlist))
            columnNumberList.append(allcolumnlist)
        delimiterIndex=np.argmax(rowNumberList)
        self.delimiter= delimiterStrings[delimiterIndex]
        ## Header Zeilen unter der Annahme, dass sie weniger Delimiter enthalten, als die anderen Zeilen.
        self.HeaderLines=np.argmax(columnNumberList[delimiterIndex])

        print('Header: ')
        for i in range(0,self.HeaderLines):
            print(dirstringlines[i])
        print('Daten: ')
        for i in range(self.HeaderLines,len(dirstringlines)):
            print(dirstringlines[i])
        
	   
        
	## lese Daten unter Benutzung des Delimiter Strings



def main():
    dirpath = 'Testdaten/testdata1.dat'
    datloadObject=datload(dirpath)
    

if __name__ == "__main__":
    main()






