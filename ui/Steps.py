# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 00:15:10 2017

@author: matthias
"""


## kann nur mit python3 geöffnet werden, nicht mit python.
import numpy as np
import matplotlib.pyplot as plt
import sys
import json
import PyQt5
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QLineEdit

from PyQt5.QtCore import Qt
import function.step_functions as step_functions
import handler.datLoad as datLoad



class Loop(QWidget):      
    def __init__(self,root):
        QWidget.__init__(self)
        self.root=root
        self.number=0
        self.Steps=[]
        self.initUI()
        self.numerateSteps()
        
    def initUI(self):
	
        self.MainHBox=QHBoxLayout(self)
        self.NumberLabel=QLabel('  ')
        self.MainHBox.addWidget(self.NumberLabel)
        self.StepBox=QVBoxLayout()
        self.StepBox.setSpacing(0)
        self.MainHBox.addLayout(self.StepBox)
        self.addStep()
        self.StepBox.addStretch()
        
        self.setWindowTitle('Loop')
        self.show()


    def addStep(self):
        newStep=ReplaceStep(self)
        self.StepBox.addWidget(newStep)
        self.Steps.append(newStep)

    def insertStep(self,number):
        newStep=ReplaceStep(self)
        self.StepBox.insertWidget(number,newStep)
        self.Steps.insert(number,newStep)
        self.numerateSteps()
    
    def replaceStep(self,OldStep,KindOfStep):
        
        if KindOfStep+'Step' in sys.modules[__name__].__dict__:
            newStep=sys.modules[__name__].__dict__[KindOfStep+'Step'](self)
        else:
            newStep=AbstractStep(self, KindOfStep)
        newStep.KindOfStep=KindOfStep
        self.StepBox.insertWidget(OldStep.number,newStep)
        self.Steps.insert(OldStep.number,newStep)
        self.removeWidget(OldStep)
        self.numerateSteps()
        

    def insertLoop(self,number):
        ILoop=LoopStep(self)
        self.StepBox.insertWidget(number,ILoop)
        self.Steps.insert(number,ILoop)
        self.numerateSteps()

    def numerateSteps(self):
        for i in range(len(self.Steps)):
            self.Steps[i].number=i+1
            self.Steps[i].NumberLabel.setText(str(i+1))

    def removeWidget(self,Widget):
        if len(self.Steps)>1:
            self.StepBox.removeWidget(Widget)
            Widget.hide()
            self.Steps.remove(Widget)
            del Widget
            self.numerateSteps()
            self.adjustSize()
            if self.root is not None:
                 self.root.adjustSize()
        else:
            pass
        
    def savestring(self):
        self.savelist=[]
        for i in range(len(self.Steps)):
            self.savelist.append([self.Steps[i].KindOfStep,self.Steps[i].savestr()])
        self.savestr=json.dumps(self.savelist)
        return(self.savestr)      
        
    def load_from_string(self,savestring):
        print(type(self),savestring)
        

class MainLoop(Loop): ## like Loop but containing Lists with all usable Datasets, Lists, Variables, 
    def __init__(self, root=None):
        Loop.__init__(self,root)
        self.MainLoop=self
        self.renewLists()

    def renewLists(self):
        self.Datasets={}
        self.Datasets['Dataset1']=self.root.data_viewer.get_selectedPaths() ## so far only one data viewer, there will be some changes when more datasets are implemented
        #self.C ## TODO: set choice of column names
        print(self.Datasets)
        for Step_i in self.Steps:
            Step_i.renew()
        
    def mousePressEvent(self,e):
         self.renewLists()
    def mouseReleaseEvent(self,e):
         self.renewLists() 
        
    def load_from_string(self,savestring):
        for Step in self.Steps:
            self.removeWidget(Step)
        savelist=json.loads(str(savestring))
        for i in range(len(savelist)-1):
            self.insertStep(i)
        for i in range(len(savelist)):
            self.replaceStep(self.Steps[i],savelist[i][0])
            self.Steps[i].load_from_string(savelist[i][1])


class Step(QWidget):
    def __init__(self, root):
        QWidget.__init__(self)
        self.root=root
        checkroot=self.root
        while(True):
             if str(type(checkroot))=='<class \'ui.Steps.MainLoop\'>':
                 self.MainLoop=checkroot
                 break
             else:
                 checkroot=checkroot.root
        self.number=0
        self.function=step_functions.choose_function(self)


        self.HBox=QHBoxLayout(self)

        self.NumberLabel=QLabel(str(len(root.Steps)+1))

        self.StepLabel=QLabel('Abstract Step')

        self.AddStepButton=QPushButton('+')
        self.AddStepButton.clicked.connect(self.insertStep)
        textWidth = self.AddStepButton.fontMetrics().boundingRect(self.AddStepButton.text()).width()
        self.AddStepButton.setMaximumWidth(textWidth+15)

        self.RemoveButton=QPushButton('-')
        self.RemoveButton.clicked.connect(self.remove)
        textWidth = self.RemoveButton.fontMetrics().boundingRect(self.RemoveButton.text()).width()
        self.RemoveButton.setMaximumWidth(textWidth+15)
	
        self.HBox.addWidget(self.NumberLabel)
        self.HBox.addWidget(self.StepLabel)
        self.HBox.addStretch()
        self.HBox.addWidget(self.AddStepButton)
        self.HBox.addWidget(self.RemoveButton)
    

    def addStep(self):
        self.root.addStep()

    def insertStep(self):
        self.root.insertStep(self.number)

    def insertLoop(self):
        self.root.insertLoop(self.number)
        
    def remove(self):
        self.root.removeWidget(self)
        del self

    def renew(self):
        pass
    
    def savestr(self):
        savedict={}
        for attr in self.__dict__:
            if(type(getattr(self,attr))==QLineEdit):
                savedict[attr]=['QLineEdit',getattr(self,attr).text()]
            if(type(getattr(self,attr))==Loop) and attr!='root':
                savedict[attr]=['Loop',getattr(self,attr).Steps[0].savestr()]
        return(json.dumps([self.KindOfStep,json.dumps(savedict)]))
        
    def load_from_string(self,savestring):
        print(type(self),savestring)

class LoopStep(Step):
    def __init__(self, root):
        Step.__init__(self, root)
        self.function=step_functions.Loop(self)        
        self.Loop=Loop(root)
        self.HBox.insertWidget(2,self.Loop)
        self.StepLabel.setText('Loop over')
        self.WhichLoop=QComboBox()
        self.HBox.insertWidget(2,self.WhichLoop)
        self.WhichLoop.addItems(list(self.MainLoop.Datasets.keys())) # TODO Dataset1 should be replaced with the names of all Datasets, when there are more
    def renew(self):
        self.WhichLoop.clear()
        self.WhichLoop.addItems(list(self.MainLoop.Datasets.keys()))
        for step_i in self.Loop.Steps:
            step_i.renew()
            


class ReplaceStep(Step):
    def __init__(self, root):
        Step.__init__(self, root)
        self.KindOfStep='Replace'
        self.MenuButton=QComboBox()
        ## find names of functions (all classes in step_functions.py)
        FunctionNames=[]
        for dictitem in step_functions.__dict__:
            if type(step_functions.__dict__[dictitem])==type(step_functions.__dict__['choose_function']):
                FunctionNames.append(dictitem)
        self.MenuButton.addItems(FunctionNames)
        self.HBox.insertWidget(2,self.MenuButton)
        self.HBox.removeWidget(self.StepLabel)
        self.MenuButton.activated.connect(self.ReplaceSelf)

    def ReplaceSelf(self):
        self.root.replaceStep(self,self.MenuButton.currentText())

class AbstractStep(Step):
    def __init__(self, root, KindOfStep):
        Step.__init__(self, root)
        self.KindOfStep=KindOfStep
        self.StepLabel.setText(self.KindOfStep)
        self.function=step_functions.__dict__[self.KindOfStep](self)

        for Arg in self.function.ArgumentList[::-1]:
            if Arg[1]=='str':
                setattr(self,Arg[0]+'_Edit',QLineEdit())
                self.HBox.insertWidget(3,getattr(self,Arg[0]+'_Edit'))
                if len(Arg)>2:
                    getattr(self,Arg[0]+'_Edit').setText(Arg[2])
                setattr(self,Arg[0]+'_Label',QLabel(Arg[0]))
                self.HBox.insertWidget(3,getattr(self,Arg[0]+'_Label'))

            if Arg[1]=='Columnname':
                setattr(self,Arg[0]+'_Combo',QComboBox())
                if len(self.MainLoop.Datasets['Dataset1'])>0:
                    Columnnames=datLoad.datLoad(self.MainLoop.Datasets['Dataset1'][0]).headerList ## TODO change such that more datasets are possible and check if all files have the same headers
                    getattr(self,Arg[0]+'_Combo').addItems(Columnnames)
                    self.HBox.insertWidget(3,getattr(self,Arg[0]+'_Combo'))
                setattr(self,Arg[0]+'_Label',QLabel(Arg[0]))
                self.HBox.insertWidget(3,getattr(self,Arg[0]+'_Label'))


            
if __name__=='__main__':
    
    app=QApplication(sys.argv)
    ex = Loop()
    sys.exit(app.exec_())
