from sense_hat import SenseHat
import threading,random,logging
import smbus
from datetime import datetime

from labbenchstudios.common import SensorData
import time

from labs.module04  import SensorDataManager




 
"""
get humidity from sensehat libary  on led 
"""
    


class HumiditySensorAdaptorTask(threading.Thread):
    

        
    sense=SenseHat()

        
        
   

    '''
    classdocs
    '''

    """initialize variables globally her
    """
    avg=0.0
    current=0.0
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
    
    sensor= SensorData.SensorData()
    
    
    
    def __init__(self):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
    
    
            
  

    
    def run(self):
#         print("hellorun")
        humiditySensor_from_lib(self)
        
        









    
def humiditySensor_from_lib(self):
    data=self.sensor
    
    for i in range(1,4):
        result=self.sense.get_humidity()
        #result= calculatehumidty(self)
        #print(result)
        
        data.addvalue(float(result))
        
        time.sleep(0.3)
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
    
    
    formatstring="Temperature from library:\n\tTime: "+str(datetime.now().isoformat())+"\n\tCurrent: "+str(current_val)+"\n\tAverage: "+str(avg)+"\n\tSamples :  10\n\tMin: "+str(min)+"\n\tMAX :"+str(max)
    FORMAT = " %(message)s"
    logging.basicConfig(level=logging.INFO,format=FORMAT)
    logging.info(formatstring)
    time.sleep(2)
    
    sensorhandler = SensorDataManager.SensorDataManager
    self.setterSensor(data)
    
    """ callback fuction """
    sensorhandler.manager_humidity(self,data)
    
    return avg,current_val,count,max,min
        
        
        
