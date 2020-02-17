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
    """
    show +  on led 
    """
    
    def increasePattern(self):
        self.sense.show_letter("+",text_colour=[255,0,0])
        print("+ sign print")
           
    """
    show - on led 
    """
    def decreasePattern(self):
        self.sense.show_letter("-",text_colour=[0,0,255])
        print("- sign print")
        
    def humidityPattern(self,value):
         self.sense.show_message(str(value),scroll_speed=0.01)