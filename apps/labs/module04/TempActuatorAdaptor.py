'''
Created on Feb 10, 2020

@author: amanshah
'''

from sense_hat import SenseHat
from labs.module04 import SenseHatLed
class TempActuatorAdaptor(object):
    '''
    classdocs
    '''
    
     
    def __init__(self):
        '''
        Constructor
        '''
         
    def ledActuator(self,command,value):
        #pattern=SenseHatLed()
        pattern=SenseHatLed.SenseHatLed()
        if command=="increase":
            pattern.increasePattern()
            #print("command increase")
        elif command=="decrease":
            pattern.decreasePattern()
            #print("command decrease")
        elif command=="showhumidity":
            pattern.humidityPattern(value)
            