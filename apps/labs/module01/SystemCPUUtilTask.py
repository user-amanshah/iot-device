'''
Created on Jan 24, 2020

@author: amanshah
'''

import psutil



"""
psutil librbary is ussed to calculate hardware utilization 
"""

class SystemCPUUtilTask(object):
    '''
    classdocs
    '''
    def calculatecpuUtil(self):
        utilization=psutil.cpu_percent(2)
        #print(utilization)
        return utilization

   # def __init__(self, params):
      
        