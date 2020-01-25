'''
Created on Jan 24, 2020

@author: amanshah
'''


from .SystemCPUUtilTask import SystemCPUUtilTask
from .SystemMemoryUtilTask import SystemMemoryUtilTask
#from labs.module01.SystemMemoryUtilTask import SystemMemoryUtilTask
import logging

class SystemPerformanceAdaptor(object):
    '''
    classdocs    
    '''
    def adapter_for_memoryandutil(self):
            objsyscpu= SystemCPUUtilTask()    #instantiate classes to call
            
            objsysmem= SystemMemoryUtilTask()
             
             
             """
             we send out output for 15 times and hence the loop
             """
            
            #objsysmem.dae
            for count in range(15):
                FORMAT = "%(asctime)s %(levelname)s %(message)s"
                """
                this is the format type where asc time returns time and date 
                level name defines the level of message ie warning , info etc
                message is the required string to be sent"
                """
                
                
                
                #logging.basicConfig(format(objsyscpu, '%(asctime)s: %(message)s'))
                logging.basicConfig(level=logging.INFO,format=FORMAT)
                logging.info(' CPU UTILIZATION='+str(objsyscpu.calculatecpuUtil()))
                #logging.info(':INFO: CPU UTILIZATION='+str(objsyscpu.calculatecpuUtil()))
                
                """
                here we need to convert the return type of memory ehich is float"""
                
                
                logging.info('MEMORY UTILIZATION='+str(objsysmem.calculateMemory()))
                                    
                
    
 #   def __init__(self, params):
    
        