'''
Created on Feb 9, 2020

@author: amanshah
'''



class ActuatorData(object):
    '''
    classdocs
    '''

    value_var=0
    command_var=""
    name=""
      
    """ overrideing default constructor
    """
    def __init__(self,command_var,value_var,name):
        
        '''
        Constructor
        '''
        self.command_var=command_var
        self.value_var=value_var
        self.name=name
          
    #def updateActuatorData(self,command_var,value_var,name):
      
      
    """
    getters and setters
    """
    def getcommand(self):
        return self.command_var
      
    def setcommand(self,command_str):
        self.command_var=command_str
          
    def setName(self,name_str):
        self.name=name_str
          
    def getName(self):
        return self.name
      
    def getValue(self):
        return self.value_var
      
    def setValue(self,value):
        self.value_var=value