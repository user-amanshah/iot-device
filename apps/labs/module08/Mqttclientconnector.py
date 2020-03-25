'''
Created on Mar 20, 2020

@author: aman shah
'''

import time
import paho.mqtt.client as mqttClient
from labbenchstudios.common import ConfigUtil
from labbenchstudios.common import SensorData
from labbenchstudios.common import DataUtil



class Mqttclientconnector(object):
    '''
    mqtt connector
    Functions to connect to broker, subscribe message , publish message
    disconnect from broker 
    all this function are related to mqtt only 
   
    '''
    port_number = None
    broker_address=""
    broker_keep_alive = None
    mqttClient=None
    config = None
    
    
    '''
    Constructor
    '''

    def __init__(self):

        self.mqttClient = mqttClient.Client("Python_Client")
        self.pemfile = 'industrial.pem'   
        self.password = ''
        self.config = ConfigUtil.ConfigUtil()
        self.sensoData = SensorData.SensorData()
        self.datautil = DataUtil.DataUtil()
        self.broker_keep_alive = 65
        self.connected_flag = False
        self.authToken = 'BBFF-DDJefJiPLcbNPpQHcfbGDM8Z4vJWiU'
        self.port_number = 1883
        self.broker_address = 'mqtt.eclipse.org'

    '''
    method to connect to mqtt broker eclipse
    '''
    def connect(self, connectionCallback = None , msgCallback = None):

        #Setting the right callbacks
        if(connectionCallback!=None):
            self.mqttClient.on_connect = connectionCallback
        else:
            self.mqttClient.on_connect = self.onConnect
            
        if(msgCallback !=None) :
            self.mqclient.on_disconnect = msgCallback
        else :
            self.mqttClient.on_disconnect = self.onMessage
        #callback when message arrives
        self.mqttClient.on_message = self.onMessage    
        print("Connecting to broker_ connect",self.broker_address)
        self.mqttClient.connect(self.broker_address, self.port_number, self.broker_keep_alive)
        self.mqttClient.loop_start() 
        while not self.connected_flag:
            print("Attempting to connect to broker :",self.broker_address)
            time.sleep(1)
            
            

    
    '''
    callback reply when the connection is made with broker 
    to check if connection is sucessful or not
    '''
    def onConnect(self , client ,userData , flags , rc):

        if rc == 0:
            self.connected_flag = True
            print("Connected OK returned Code:" , rc)
        else:
            print("Bad connection Returned Code:", rc)
    
 
 
    '''
    method to subscribe to a topic  
    '''
    def subscibetoTopic(self , topic_name ,connnectionCallback = None, qos=2):

        if connnectionCallback != None:
            self.mqttClient.on_subscribe = (connnectionCallback)
            self.mqttClient.on_message = (connnectionCallback)
        self.mqttClient.subscribe(topic_name , qos)           
            
    '''
    callback reply when message arrivesin arrays
    to be decoded
    '''
    def onMessage(self , client ,userdata , message):

        print("Recieved Message: " + str(message.payload.decode("utf-8")))
        payload = str(message.payload).split("'")
        value = payload[0]
       
      
    '''
    method to publish message to broker
    with qos 2
    '''         
    def publishMessage(self , topic , message , qos=2):

        print("Publishing the message with qos 2:",message)
        self.mqttClient.publish(topic, message, qos)
    

        
   
    def unsubscibefromTopic(self , topic_name):
        '''
        method to unsubscribe to a topic_name
        '''       
        print("Unsubscribing from topic_name",topic_name)
        self.mqttClient.unsubscribe(topic_name)
        
        
    '''
    function to disconnect 
    '''   
    def disconnect(self):
        
        print("Disconneting the MQTT  broker connection ")
        self.mqttClient.disconnect()
    
        
    