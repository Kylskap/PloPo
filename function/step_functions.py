import handler.datLoad as datLoad
import numpy as np
import matplotlib.pyplot as plt


class choose_function:
    def __init__(self,step):

        self.step=step
    def function(self,routine):
        print(self)
        self.routine=routine
        print('Testfunktion von',self.step)




class Loop: # Schleife über - Liste, pandas, dict...   
# macht eigentlich das gleiche, wie routine, es könnte aber nützlich sein, routine immer als namespace zu benutzen, um Variablennamen sinnvoll zu nutzen.


    def __init__(self,step):

        self.step=step

    def function(self,routine):
        self.routine=routine
        print(self.routine.Datasets['Dataset1'])
        for data_i in self.routine.Datasets['Dataset1']:
            print('data_i',data_i)
            for step_i in self.step.Loop.Steps:
                 step_i.function.function(self.routine)

class create_Array_Variable:
    def __init__(self,step):

        self.step=step
        self.ArgumentList=[['Variable_Name','str','x'],['Column','Columnname']] ## List in order to keep ordering
    def function(self,routine):
        self.routine=routine
        print(datLoad.datLoad(self.step.MainLoop.Datasets['Dataset1'][0]).data[self.step.Column_Combo.currentText()])
        
        setattr(self.routine,self.step.Variable_Name_Edit.text(),np.array(datLoad.datLoad(self.step.MainLoop.Datasets['Dataset1'][0]).data[self.step.Column_Combo.currentText()]))
        #print(getattr(self.step,'Variable_Name_Edit').currentText(),getattr(self.routine,getattr(self.step,'Variable_Name_Edit').text()))
       


class Plot:
    def __init__(self,step):
        self.step=step
        self.ArgumentList=[['X_Var','str','x'],['Y_Var','str','y'],['Figure','str','1'],['SubPlt','str','111']]

    def function(self,routine):
        self.routine=routine
        plt.figure(self.step.Figure_Edit.text())
        plt.subplot(self.step.SubPlt_Edit.text())
        plt.plot(getattr(self.routine,self.step.X_Var_Edit.text()),getattr(self.routine,self.step.Y_Var_Edit.text()))

class Show_Plots:
    def __init__(self,step):
        self.step=step
        self.ArgumentList=[]

    def function(self,routine):
        self.routine=routine
        plt.show()

class fit_Function:
    def __init__(self,step):
        self.step=step
        self.ArgumentList=[['Function','str','x**2'],['List of initial values','str','[1,1]']] ## List in order to keep ordering
    def function(self,routine):
        self.routine=routine
        print('Not implemented so far')

