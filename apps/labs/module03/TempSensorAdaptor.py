'''
Created on Feb 9, 2020

@author: amanshah
'''

from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
import logging,time
from datetime import datetime

#from labs.module02 import TempSensorEmulatorTask
#from labs.module03 import TempSensorAdaptor
class TempSensorAdaptor(object):
    '''
    classdocs
    '''
    avg=0.0
    current_val=0.0
    count=0
    max=0.0
    min=0.0
    
    

    def __init__(self):
        '''
        Constructor
        '''

    def adaptor(self):
        
        result= TempSensorAdaptorTask()
        result.run()
        
#         print(self.count)
#         #formatstring="Temperature:\n\tTime: "+str(datetime.now().isoformat())+"\n\tCurrent: "+str(current)+"\n\tAverage: "+str(avg)+"\n\tSamples :  10\n\tMin: "+str(min)+"\n\tMAX :"+str(max)
#         formatstring="Temperature:\n\tTime: "+str(datetime.now().isoformat())+"\n\tCurrent: "+str(self.current_val)+"\n\tAverage: "+str(self.avg)+"\n\tSamples :  10\n\tMin: "+str(self.min)+"\n\tMAX :"+str(self.max)
#         FORMAT = " %(message)s"
#         logging.basicConfig(level=logging.INFO,format=FORMAT)
#         logging.info(formatstring)
#         time.sleep(0.8)
#         
        
        
        