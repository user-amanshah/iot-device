'''
Created on Feb 9, 2020

@author: amanshah
'''

import threading,random,time
from labbenchstudios.common import SensorData
from labs.module03 import SensorDataManager
from sense_hat import SenseHat
#from labbenchstudios.common.SensorData import SensorData

class TempSensorAdaptorTask(threading.Thread):
    '''
    classdocs
    '''
    sense=SenseHat()
    avg=0.0
    current=0.0
    sensor=SensorData.SensorData()
    
    def getteravg(self):
        return self.avg
    
    def setteravg(self,avg):
        self.avg=avg
        
    def gettercurrent(self):
        return self.current
    def settercurrent(self,currentval):
        self.current=currentval
        
    def setterSensor(self,sensordataobj):
        self.sensor=sensordataobj
        
    def getterSensor(self):
        return self.sensor
        
    
    
    
    def __init__(self):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        
    
    def run(self):
        
        # we start thread to run method continuously 
        
        data=self.sensor
    
        for i in range(1,4):
            #temp=self.sense.get_temperature()
            temp=random.uniform(10.0,20.0)
            print(temp)
            data.addvalue(float(temp))
            
            time.sleep(0.2)
            i+1
            
        avg=data.getterAvg()
        current_val= data.gettercurrent()
        count= data.getterCount()
        max= data.getterMax()
        min= data.getterMin()
        
        self.setteravg(avg)
        self.settercurrent(current_val)
        
        
        
        #returning data object that contains all temperature paramters
        print("enterhandleer")
        print(avg)
        sensorhandler = SensorDataManager.SensorDataManager
        self.setterSensor(data)
        sensorhandler.manager(self,data)
        
        return avg,current_val,count,max,min