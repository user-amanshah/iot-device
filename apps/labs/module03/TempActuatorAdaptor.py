'''
Created on Feb 10, 2020

@author: amanshah
'''

from sense_hat import SenseHat
from labs.module03.SenseHatLed import SenseHatLed
class TempActuatorAdaptor(object):
    '''
    classdocs
    '''
    pattern=SenseHatLed()
     
    def __init__(self):
        '''
        Constructor
        '''
         
    def ledActuator(self,command):
        pattern=SenseHatLed()
        if command=="increase":
            pattern.increasePattern()
            #print("command increase")
        elif command=="decrease":
            pattern.decreasePattern()
            #print("command decrease")