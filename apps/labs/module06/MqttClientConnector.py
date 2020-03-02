'''
Created on Feb 29, 2020

@author: amanshah
'''

from labbenchstudios.common.DataUtil import DataUtil
import paho.mqtt.client as mq_client
import time
from numpy.distutils.fcompiler import none


class MqttClientConnector(object):
    '''
    mqtt code that is required to invoke paho library for publishing 
    message on channel
    '''
    
    
    #declare variables
    brokker_add = "broker.hivemq.com"
    port_number = 1883
#     username = "test"
#     passwd = "test"
#     
    def __init__(self):
        '''
        Constructor
        '''
        self.client_obj = mq_client.Client("client_1")
        self.client_obj.on_connect = self.on_connect
        self.client_obj.on_message = self.on_message
        self.client_obj.on_disconnect = self.on_disconnect
        self.client_obj.connect(self.brokker_add, 1883, 65)
        
    """method for establishing connection"""

    def on_connect(self, client_obj_ref, userdata, rc_flag):
        if rc_flag == 0:
            print("successful connection")
            return True
        else:
            print("cannot connect error ")
            return False
        
    
    def on_message(self , client_obj_ref  , message):
        print("message topic  :", message.topic)
        print("QOS : " , message.qos)
        print("retainflag", message.retain)

    """ publish message of sensor data"""

    def publish_sensor_data(self, sensordata_obj):
        dataUtil = DataUtil()
        json_sensor = dataUtil.tojsonfromSensorData(sensordata_obj)
        print(json_sensor)
        self.client_obj.loop_start()
        try:                
            self.client_obj.publish("sensor_test_aman", json_sensor, 2)
            print(json_sensor )
            time.sleep(7)
            return True
        except:
            
            self.client_obj.loop_stop()
            return False
        #disconnect from broker
    def on_disconnect(self,client,rc_flag):
        print("Disconnected the session :"+str(rc_flag))
        try:
            self.client_obj.loop_stop()
            return True
        except:
            return False    
