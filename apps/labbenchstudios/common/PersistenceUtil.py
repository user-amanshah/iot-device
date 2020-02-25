'''
Created on Feb 23, 2020

@author: amanshah
'''


from labbenchstudios.common.DataUtil import DataUtil
from labbenchstudios.common.ActuatorData import ActuatorData
from labbenchstudios.common.ActuatorDataListener import ActuatorDataListener
from labs.module05.TempActuatorAdaptor import TempActuatorAdaptor
from asyncio.tasks import sleep
import time
import redis, uuid
class PersistenceUtil(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.dataUtil = DataUtil()
       
        
        
        
    def writeSensorDataToDB(self,sensor_obj,id):
        json_sensor=self.dataUtil.tojsonfromSensorData(sensor_obj)
        
         
        connection = self.connection()
        #pubsub_obj = connection.pubsub()
        
        connection.set(id,json_sensor)
        
        #subscribe to actuator
        
    def writeSensorToPubSub(self,id):
        connection=self.connection()
        r=connection.pubsub()
        connection.publish("sensorchannel",id)
        
        
       
        
    """
    get command and actuation data and do actuation
    """    
    def registerActuatorDbListener(self):
        connection = self.connection()
        sub_obj=connection.pubsub()
        subscibed = sub_obj.subscribe("actuationchannel")
        for m in subscibed.listen():
            message_id= sub_obj.get_message()['data']
#         message_id=subscibed.get_message()
            if(message_id['data'] !=1):
                time.sleep(0.6)
               
                data=subscibed.get_message()['data']
                print(data)  
        
                command=data.get("command")
                value=data.get("value")
                
                ActuatorData(command, value, "temperture")
                
                
        
    
        
        
    
        
    def writeActuatorDataToDbms(self):
        redis_subscribe = self.redis_connection.pubsub()
        redis_subscribe.subscribe("ActuatorData_Channel")
        
        for m in redis_subscribe.listen():
            msg = redis_subscribe.get_message()['data']
            if(msg['data'] !=1):
                sleep(0.5)
                data=redis_subscribe.get_message()['data']
                print(data)  
                
        self.registerActuatorDataDbmsListener()
        redis_subscribe.unsubscribe("ActuatorData_Channel")
        self.redis_connection.close()
    
        
   
       
       
    def registerActuatorSensorListener(self,actuation):
        return ActuatorDataListener.onMessage_connected(self, actuation)
        
        
        
        
    
    
    