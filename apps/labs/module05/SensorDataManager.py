'''
Created on Feb 9, 2020

@author: amanshah
'''
from datetime import datetime
import time,uuid


from labbenchstudios.common.PersistenceUtil import PersistenceUtil
from labs.module04.MultiSensorAdaptor import MultiSensorAdaptor
from labbenchstudios.common.ActuatorData import ActuatorData
from labs.module04.TempActuatorAdaptor import TempActuatorAdaptor

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
        
        
        a=PersistenceUtil()
        id_var= uuid.UUID().hex()
        a.writeSensorDataToDB(sensorvalues, id_var)
        a.writeSensorToPubSub(id_var)
        
        
            

    def runapplication(self):
        MultiSensorAdaptor().adaptor()
        
        #TempSensorAdaptor().adaptor()