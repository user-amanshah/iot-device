'''
Created on Feb 23, 2020

@author: amanshah
'''
from datetime import datetime
import labbenchstudios
from labbenchstudios.common.SensorData import SensorData
from labbenchstudios.common.ActuatorData import ActuatorData

import json
class DataUtil (object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
#         self.sensor_obj=SensorData()
       
       
    def tojsonfromSensorData(self,sensor):
        print("values from sensor data")
        json_vr={}
        json_vr["timestamp"]=datetime.utcnow()
        json_vr["avg"]=sensor.getterAvg()
        json_vr["current"]=sensor.gettercurrent() 
        json_vr["max"]=sensor.getterMax()
        json_vr["min"]=sensor.getterMin()
        json_vr["total"]=sensor.getterTotal()
        
        json_from_sensordat=json.dumps(json_vr)
        return json_from_sensordat
    
    
    
       
    def sensorfromjson(self,string_json):
        print("values from json data")
#         json_vr={}
        dict_json = json.loads(string_json)
        sensor_obj= SensorData()
        sensor_obj.setterAvg(dict_json.getData("avg"))
        sensor_obj.setterMax(dict_json.getData("max"))
        sensor_obj.setterMin(dict_json.getData("min"))
        sensor_obj.settercurrent(dict_json.getData("current"))
        sensor_obj.setterTotal(dict_json.getData("total"))
        
        
#         json_from_sensordat=json.loads(json_vr)
        return sensor_obj
    
    def writeSensorDataToFile(self,sensor_obj):
        print("values from sensor data")
        json_vr={}
        json_vr["timestamp"]=datetime.utcnow()
        json_vr["avg"]=sensor_obj.getterAvg()
        json_vr["current"]=sensor_obj.gettercurrent() 
        json_vr["max"]=sensor_obj.getterMax()
        json_vr["min"]=sensor_obj.getterMin()
        
        json_vr["total"]=sensor_obj.getterTotal()
        
        with open('sensordatas.json' ,'a+') as outputfile:
            json.dump(json_vr, outputfile)
        
#         json_from_sensordat=json.loads(json_vr)
#         return json_from_sensordat
        
    
        
        
        
       
    def tojsonfromActuatorData(self,actuator):
        print("values from sensor data")
        json_vr={}
        json_vr["timestamp"]=datetime.utcnow()
        json_vr["command"]=actuator.getcommand()
        json_vr["value"]=actuator.getValue()
        json_vr["name"]=actuator.getName()
        
        json_from_actuator= json.loads(json_vr)
        
        return json_from_actuator   
    
    
       
    def actuatorfromjson(self,string_json):
        print("values from json data")
#         json_vr={}
        dict_json = json.loads(string_json)
        actuator = ActuatorData()
        actuator.setcommand(dict_json.getData("command"))
        actuator.setName(dict_json.getData("name"))
        actuator.setValue(dict_json.getData("value"))
        
        return actuator
    
    
    def writeActuatorDataToFile(self,actuator_obj):
        print("values from actuator data to file")
        json_vr={}
        json_vr["timestamp"]=datetime.utcnow()
        json_vr["command"]= actuator_obj.getcommand()
        json_vr["value"]= actuator_obj.getValue()
        json_vr["name"]= actuator_obj.getName()
        
        
        with open('actuatordata.json' ,'a+') as outputfile:
            json.dump(json_vr, outputfile)
    
    
    
    def readSensorfromFile(self):
        with open('sensordata.json') as f:
            data = json.load(f)
        
        data.get()    
    