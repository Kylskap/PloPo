class choose_function:
    def __init__(self,routine,step):
        self.routine=routine
        self.step=step
    def function(self):
        print('Testfunktion von',self.step)




class Loop: # Schleife über - Liste, pandas, dict...   
# macht eigentlich das gleiche, wie routine, es könnte aber nützlich sein, routine immer als namespace zu benutzen, um Variablennamen sinnvoll zu nutzen.


    def __init__(self,routine,step):
        self.routine=routine
        self.step=step

    def function(self):
        for step_i in self.step.Loop.Steps:
             step_i.function(self.routine,step_i).function()

class create_Array_Variable:
    def __init__(self,routine,step):
        self.routine=routine
        self.step=step
    def function(self):
        print('Not implemented so far')
        #self.ArgumentDict={'Variable Name':'str'}
        #setattr(self.routine,self.step)

class fit_Function:
    def __init__(self,routine,step):
        self.routine=routine
        self.step=step
    def function(self):
        print('Not implemented so far')

class Plot:
    def __init__(self,routine,step):
        self.routine=routine
        self.step=step
    def function(self):
        print('Not implemented so far')

class show_Figure:
    def __init__(self,routine,step):
        self.routine=routine
        self.step=step
    def function(self):
        print('Not implemented so far')

class save_Figure:
    def __init__(self,routine,step):
        self.routine=routine
        self.step=step
    def function(self):
        print('Not implemented so far')

class seve_txt:
    def __init__(self,routine,step):
        self.routine=routine
        self.step=step
    def function(self):
        print('Not implemented so far')
        
        
