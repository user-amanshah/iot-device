'''
Created on Feb 9, 2020

@author: amanshah
'''
from datetime import datetime

from labs.module03.ActuatorData import ActuatorData
from labs.module03.TempSensorAdaptor import TempSensorAdaptor
from labs.module03.TempActuatorAdaptor import TempActuatorAdaptor
from labbenchstudios.common.ConfigUtil import ConfigUtil
from asyncio.tasks import sleep
class SensorDataManager(object):
    '''
    classdocs
    '''
    
    avg=0.0
    count=0
    current_value=0.0
   
        
    def getteravg(self):
        return self.avg
    
    def setteravg(self,avg):
        self.avg=avg
        
    def gettercount(self):
        return self.count
    
    def settercount(self,count):
        self.count=count
        
    def gettercurrent(self):
        return self.current_value
    def settercurrent(self,currentval):
        self.current_value=currentval
        
    

    actuatorAdaptor = TempActuatorAdaptor()
    
    def __init__(self):
        '''
        Constructor
        '''
        

   
    def manager(self,sensorvalues):
        print("entered")
        avg=sensorvalues.getterAvg()
        print(avg)
        current_val= sensorvalues.gettercurrent()
        count= sensorvalues.getterCount()
        max= sensorvalues.getterMax()
        self.setteravg(avg)
        self.settercurrent(current_val)
        
        
        nominalTemp=int(ConfigUtil().getvalue("device", "nominalTemp"))
        
        
        min= sensorvalues.getterMin()
       
        if(abs(avg-current_val)>5):
            print("senshat")
            print(sensorvalues.getterAvg())
            formatstring="Temperature:\n\tTime: "+str(datetime.now().isoformat())+"\n\tCurrent: "+str(current_val)+"\n\tAverage: "+str(avg)+"\n\tSamples :  10\n\tMin: "+str(min)+"\n\tMAX :"+str(max)
            topic="ALert : Sudden Temperature increase above threshold"
#             data=formatstring    #"The temperature has suddenly changed to high percent value from average "+str(avg)+"to a sudden change of "+str(current)+"This is an auto generated email"
#             self.email.sendemailmethod(topic, data)
            print("email sent")
        elif(current_val > nominalTemp):
            latest_actuator= ActuatorData("decrease", avg, "temperature")
            print("decrease command")
            recent_command=latest_actuator.getcommand()
            print("enter led")
            self.actuatorAdaptor.ledActuator(recent_command)
            TempActuatorAdaptor.ledActuator(self, recent_command)
          
            
        elif(current_val <nominalTemp):
            print("senshat")
            print(sensorvalues.getterAvg())
#             formatstring="Temperature:\n\tTime: "+str(datetime.now().isoformat())+"\n\tCurrent: "+str(current_val)+"\n\tAverage: "+str(avg)+"\n\tSamples :  10\n\tMin: "+str(min)+"\n\tMAX :"+str(max)
#             topic="ALert : Sudden Temperature increase above threshold"
#             data=formatstring    #"The temperature has suddenly changed to high percent value from average "+str(avg)+"to a sudden change of "+str(current)+"This is an auto generated email"
#             self.email.sendemailmethod(topic, data)
            print("email sent")
            latest_actuator= ActuatorData("increase", avg, "temperature")
            print("increase command")
            recent_command=latest_actuator.getcommand()
            print("enter led")
            TempActuatorAdaptor.ledActuator(self, recent_command)
          
            

    def runapplication(self):
        TempSensorAdaptor().adaptor()