'''
Created on 14-Mar-2020

@author:aman shah
'''
from labs.module07.CoapClientConnector import CoapClientConnector
from labbenchstudios.common.DataUtil import DataUtil
from labbenchstudios.common.ConfigUtil import ConfigUtil
from labbenchstudios.common.SensorData import SensorData



'''initialize variable for ConfigUtil class'''
config = ConfigUtil()
'''initialise variable for DataUtil class'''

data = DataUtil()
#ip/ or hostname direct 
host = '127.0.0.1'  #config.getProperty(ConfigConst.COAP_DEVICE_SECTION, ConfigConst.HOST_KEY)
#port number initialized
port = 5683 #int(config.getProperty(ConfigConst.COAP_DEVICE_SECTION, ConfigConst.PORT_KEY))
#equivalent to channel in mqtt
path = 'temperature'
#instance variable for SensorData class
sensorData = SensorData()

#add new sensordata value
sensorData.addvalue(20.00)
#call the Coapclient connector
coapClient_obj = CoapClientConnector(host, port, path)
'''ping request'''
coapClient_obj.ping()
'''get request'''
coapClient_obj.get()  
'''post request'''
coapClient_obj.post(data.tojsonfromSensorData(sensorData))  
'''add new value to sensor data'''
sensorData.addvalue(15.00)
'''put request'''
coapClient_obj.put(data.tojsonfromSensorData(sensorData))  
'''delete request'''
coapClient_obj.delete()  
'''stop the Coap client'''
coapClient_obj.stop()

