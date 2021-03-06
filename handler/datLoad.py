## a function which gets a path as argument and returns the data 

import numpy as np 
import matplotlib.pyplot as plt

class datLoad:
    def __init__(self,dirpath):
        self.dirpath=dirpath
        self.data={}

## lese jetzt Daten ein
        with open (self.dirpath, 'r') as dirfile:
            
            dirstringlines=dirfile.readlines()
            dirstring=dirfile.read()
        ## loesche letzte Zeile, falls leer:
        if not dirstringlines[-1]:
            dirstringlines=dirstringlines[:-1]
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
        self.CommentLines=np.argmax(columnNumberList[delimiterIndex])
        print(columnNumberList[delimiterIndex])
	## lese Daten unter Benutzung des Delimiter Strings
	## zuerst Comment
        self.comment=''
        for i in range(0,self.CommentLines):
            self.comment+=dirstringlines[i]
        ## lese Header, lege Listen mit Headern als Keys an. 
        self.data={}
        self.headerList=[]
        for iheader in dirstringlines[self.CommentLines].split(self.delimiter):
            if iheader.endswith('\n'):
                iheader=iheader[:-1]
            if iheader:
                self.data[iheader]=[]
                self.headerList.append(iheader)
        ## lese Daten und schreibe sie in Listen
        for i in range(self.CommentLines+1,len(dirstringlines)):
            idataList=dirstringlines[i].split(self.delimiter)
            for j in range(len(idataList)):
                if idataList[j].endswith('\n'):
                     idataList[j]=idataList[j][:-1]
                if(idataList[j]):
                    self.data[self.headerList[j]].append(float(idataList[j]))
        for header in self.data:
            self.data[header]=np.array(self.data[header])
        print('headerList:',self.headerList)
        print('data:',self.data)
        print ('comment: ',self.comment)

def main():
    dirpath = 'Testdaten/testdata4.dat'
    datloadObject=datload(dirpath)
    

if __name__ == "__main__":
    main()






