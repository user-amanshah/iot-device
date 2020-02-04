'''
Created on Feb 1, 2020

@author: amanshah
'''

#from .TempEmulatorAdaptor import Tempemulator
#from labs.module02.TempEmulatorAdaptor import TempemulatorAdaptor
from labs.module02.TempSensorEmulatorTask import TempSensorEmulator
from labbenchstudios.common.SensorData import SensorData
from labs.module02.TempEmulatorAdaptor import TempemulatorAdaptor
from labbenchstudios.common.ConfigUtil import ConfigUtil


if __name__ == '__main__':
    
    
    obj=TempemulatorAdaptor()
    obj.adaptor()

#     obj=TempSensorEmulator()
#     obj.sensoremulator()
#     
#     obj = SensorData()  
#     obj.calling()
    