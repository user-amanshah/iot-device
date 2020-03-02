'''
Created on Feb 29, 2020

@author: amanshah
'''
from labs.module06.TempSensorAdaptorTask import TempSensorAdaptorTask
class MultiSensorAdaptor(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    
    """calling run function to continuosly pusbhlish messages"""
    def adaptor(self):
        while True:
            running = TempSensorAdaptorTask()
            running.run()