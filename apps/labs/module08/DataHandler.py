'''
Created on Mar 20, 2020

@author: aman shah
'''

from labs.module08 import Mqttclientconnector
from time import sleep


class Datahandler(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def mqttconnector(self):  
                
        # MqttClientConnector instance
        connector = Mqttclientconnector.Mqttclientconnector()
        # Connecting to broker
        connector.connect(None, None)
        #subscribing to a topic
        connector.subscibetoTopic("mqtt_topic")
        sleep(6)
        # unsubscribe 
        connector.unsubscibefromTopic("mqtt_topic")
        # disconnecting
        connector.disconnect()
    
