from labs.module04.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module04.HI2CSensorAdaptorTask import HI2CSensorAdaptorTask
from labs.module04.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
import logging,time,math
from datetime import datetime

#from labs.module02 import TempSensorEmulatorTask
#from labs.module03 import TempSensorAdaptor
class MultiSensorAdaptor(object):
    '''
    classdocs
    '''

    """
    call tempsensordaptortask class
    """ 
    diff=0
    
    def setterdiff(self,value):
        self.diff=value
    
    def getterdiff(self):
        return self.diff

    def __init__(self):
        '''
        Constructor
        '''

    def adaptor(self):
        
        result= TempSensorAdaptorTask()
        result.run()
#         time.sleep(1)
#         print("helloadaptor")
        time.sleep(1)
        humidity = HI2CSensorAdaptorTask()
        humidity.run()
        time.sleep(1)
        library_humidity = HumiditySensorAdaptorTask()
        library_humidity.run()
        
        diff=humidity.getteravg() - library_humidity.getteravg()
        diff=abs(diff)
        self.setterdiff(diff)
        formatstring="Temperature difference from lib and i2c is:  "+str(diff)
        FORMAT = " %(message)s"
        logging.basicConfig(level=logging.INFO,format=FORMAT)
        logging.info(formatstring)