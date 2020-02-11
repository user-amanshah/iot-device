'''
Created on Feb 10, 2020

@author: amanshah
'''

from sense_hat import SenseHat
class SenseHatLed(object):
    '''
    classdocs
    '''
    sense=SenseHat()

    def __init__(self):
        '''
        Constructor
        '''
    
    def increasePattern(self):
        #self.sense.show_letter("+",text_colour=[255,0,0])
        print("increase matrix")
            
    def decreasePattern(self):
        #self.sense.show_letter("-",text_colour=[0,0,255])
        print("decrease matrix")