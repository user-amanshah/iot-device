'''
Created on Feb 1, 2020

@author: amanshah
'''
 
import datetime
import numpy as np
import random
#from test.test_audioop import minvalues


class SensorData(object):
    '''
    classdocs
    '''
    time1=0
    count=0
    name = ""
    currentval = 0.0
    
    averageval = 0.0
    total = 0.0
    sample = 0
    maxval=0.0
    minvalue=1000.0
#     
   

    def __init__(self):
        '''
        Constructor
        '''
        self.time=datetime.datetime.now().isoformat()
                
    def getterMin(self):
        return self.minvalue
     
    def setterMin(self,min):
        self.minvalue=min
         
    def getterMax(self):
        return self.maxval
         
    def setterMax(self,max):
        self.maxvalue=max
         
    def getterCount(self):
        return self.count
     
    def settercount(self,count):
        self.count=count
         
         
#         
    def getterAvg(self):
        return self.averageval
     
    def setterAvg(self,avg):
        self.averageval=avg
     
    def getterTotal(self):
        return self.total
    def setterTotal(self,total):
        self.total=total
        
    def gettercurrent(self):
        return self.currentval
    
    def settercurrent(self,current):
        self.currentval=current
        
            
    def addvalue(self,newvalue):
        self.count=self.count+1
        self.currentval=newvalue
        self.time= datetime.datetime.now().isoformat()

        self.total=self.total+newvalue
        self.averageval=0
        self.currentval=newvalue
         
        if(newvalue > self.maxval):
            self.maxval=newvalue
            
            
        #print(str(self.maxval)+"max")
#         else:
#             self.minvalue= newvalue
#             
            #self.setterMax(newvalue)
             
             
        if(newvalue < self.minvalue):
            self.minvalue=newvalue
#         print(str(self.minvalue)+"small")
             
        if(self.count>0 and newvalue>0):
            #print("-----"+str(self.total))
            self.averageval=(self.total)/(self.count)
            #print("-----"+str(self.averageval))

          
             
            