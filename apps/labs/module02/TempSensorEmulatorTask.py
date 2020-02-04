'''
Created on Feb 1, 2020

@author: amanshah
'''

from labbenchstudios.common.SensorData import SensorData
import random

class TempSensorEmulator(object):
    '''
    classdocs
    '''
#     count
#     avg
#     max
#     min 
#     current
#        
    def __init__(self):
        return
   


    def sensoremulator(self):
        SensorData_obj = SensorData()
      
        for i in range(1,10):
            
            new_value=random.uniform(20.0,30.0)
            #print(new_value)
            SensorData_obj.addvalue(float(new_value))
        
        count=SensorData_obj.count
        avg=SensorData_obj.averageval
        max= SensorData_obj.maxval
        min = SensorData_obj.minvalue
        current = SensorData_obj.currentval
        
        return count,avg,max,min,current
    
            