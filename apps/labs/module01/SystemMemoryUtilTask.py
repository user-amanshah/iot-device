'''
Created on Jan 24, 2020

@author: amanshah
'''
import psutil

class SystemMemoryUtilTask(object):
    '''
    psutil is used to calculate hardware memory used at present 
    '''
    def calculateMemory(self):
        memorycalc = psutil.virtual_memory()
        percent_mem=memorycalc.percent # to calculate percent of mem utilized
        #print(percent_mem)
        return percent_mem
        
        


    
    #def __init__(self, params):
       