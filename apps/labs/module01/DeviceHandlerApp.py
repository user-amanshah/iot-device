'''
Created on Jan 24, 2020

@author: amanshah
'''
from labs.module01.SystemPerformanceAdaptor import SystemPerformanceAdaptor


if __name__ == '__main__':
    
    
    """
    this is the main function that runs the flow
    
    it will call adapter class , which in turn will call 
    systempercpuuitl and systemmemutil class 
     
    """
    adapterobj = SystemPerformanceAdaptor()         #instantiate classes
    
    adapterobj.adapter_for_memoryandutil()
    