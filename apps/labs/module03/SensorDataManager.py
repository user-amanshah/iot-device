'''
Created on Feb 9, 2020

@author: amanshah
'''
from datetime import datetime
import time

from labbenchstudios.common.ActuatorData import ActuatorData
from labs.module03.TempSensorAdaptor import TempSensorAdaptor
from labs.module03.TempActuatorAdaptor import TempActuatorAdaptor
from labs.module02.SmtpClientConnector import SMTPemailclass
from labbenchstudios.common.ConfigUtil import ConfigUtil
from asyncio.tasks import sleep
class SensorDataManager(object):
    '''
    classdocs
    '''
    
    
    """
    setters and getters and initialization
    """
    avg=0.0
    count=0
    current_value=0.0
    actuatorAdaptor = TempActuatorAdaptor()
    
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
        
    

   
    
    def __init__(self):
        '''
        Constructor
        '''
        
        
        
    """
     callbacked function
    """   

   
    def manager(self,sensorvalues):
#         print("entered manager")
        avg=sensorvalues.getterAvg()
        #print(avg)
        current_val= sensorvalues.gettercurrent()
        count= sensorvalues.getterCount()
        max= sensorvalues.getterMax()
        self.setteravg(avg)
        self.settercurrent(current_val)
        
        """
        get nominal temp from confg file 
        
        """
        
        nominalTemp=int(ConfigUtil().getvalue("device", "nominalTemp"))
        
        
        min= sensorvalues.getterMin()
        
        formatstring="Temperature:\n\tTime: "+str(datetime.now().isoformat())+"\n\tCurrent: "+str(current_val)+"\n\tAverage: "+str(avg)+"\n\tSamples :  10\n\tMin: "+str(min)+"\n\tMAX :"+str(max)
        time.sleep(0.8)
        #print(formatstring)
        topic="ALert : Sudden Temperature increase above threshold"
        #print(topic)
        
        """
           check if email is to be sent using avg values
        """
        if(abs(avg-current_val)>3):
            email=SMTPemailclass()
#             print(sensorvalues.getterAvg())
           
            
            data=formatstring    #"The temperature has suddenly changed to high percent value from average "+str(avg)+"to a sudden change of "+str(current)+"This is an auto generated email"
            
            
            
            email.sendemailmethod(topic, data)
            
            """
            check if actuator is needed incase temp decreases
            """
        elif(current_val < nominalTemp):
            
#             print(sensorvalues.getterAvg())
            """
            actuation on sensehat
            set command
            """
            latest_actuator= ActuatorData("increase", avg, "temperature")
            print("set increase command")
            recent_command=latest_actuator.getcommand()
            print("enter led")
            
            TempActuatorAdaptor.ledActuator(self, recent_command)    
            print("email sent")
            
            
            """
            check if actuator is needed incase temp increases
            """
        elif(current_val > nominalTemp):
            """
            actuation on sensehat
            set command
            """
            latest_actuator= ActuatorData("decrease", avg, "temperature")
            print("set decrease command")
            recent_command=latest_actuator.getcommand()
            print("enter led")
            
            TempActuatorAdaptor.ledActuator(self, recent_command)
          
            
        
          
            

    def runapplication(self):
        TempSensorAdaptor().adaptor()