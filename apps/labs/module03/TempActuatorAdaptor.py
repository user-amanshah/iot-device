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
        if command=="increase":
            #self.pattern.increasePattern()
            print("incled")
        elif command=="decrease":
            #self.pattern.decreasePattern()
            print("decled")