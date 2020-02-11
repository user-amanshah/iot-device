'''
Created on Feb 9, 2020

@author: amanshah
'''

import threading,random,time,logging
from labbenchstudios.common import SensorData
from datetime import datetime
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
    """
    setters and getters
    """
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
        
    
    """
    initiate thread in constructor
    """
    
    def __init__(self):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        
    """
    default method overriding run
    """
    def run(self):
        calculateSensorValue(self)
        
        
        # we start thread to run method continuously 
        
"""
calculate temperature from sensehate
"""

def calculateSensorValue(self):
    data=self.sensor

    for i in range(1,4):
#             temp=self.sense.get_temperature()
        temp=random.uniform(15.0,30.0)
        #print(temp)
        data.addvalue(float(temp))
        
        time.sleep(0.2)
        i+1
        
    avg=data.getterAvg()
    #print(avg)
    current_val= data.gettercurrent()
    #print(current_val)
    count= data.getterCount()
    max= data.getterMax()
    min= data.getterMin()
    
    self.setteravg(avg)
    self.settercurrent(current_val)
    
    
    


    """
    outputing file to console using logging
    """
    

    formatstring="Temperature:\n\tTime: "+str(datetime.now().isoformat())+"\n\tCurrent: "+str(current_val)+"\n\tAverage: "+str(avg)+"\n\tSamples :  10\n\tMin: "+str(min)+"\n\tMAX :"+str(max)
    FORMAT = " %(message)s"
    logging.basicConfig(level=logging.INFO,format=FORMAT)
    logging.info(formatstring)
    time.sleep(0.8)
    
    sensorhandler = SensorDataManager.SensorDataManager
    self.setterSensor(data)
    
    """ callback fuction """
    sensorhandler.manager(self,data)
    
    return avg,current_val,count,max,min