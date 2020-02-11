'''
Created on Feb 1, 2020

@author: amanshah
'''
from labs.module02.TempSensorEmulatorTask import TempSensorEmulator
from labs.module02.SmtpClientConnector import SMTPemailclass
import logging
from datetime import datetime
from threading import Thread
from time import sleep

class TempemulatorAdaptor(object):
    '''
    classdocs
    '''
 
#  
#     def __init__(self, params):
#         '''
#         Constructor
#         '''/
    def adaptor(self):
        emulator_obj=TempSensorEmulator()
#         #print("kskdj")
#         for i in range(1,10):
#             [time,currentval,count,averageval,maxval,minval,totalval]=emulator.sensoremulator()
        for i in range(1,8):
            sleep(0.2)
            [count,avg,max,min,current ]=emulator_obj.sensoremulator()  
            
             
            """
                we catch the all the return value parameter from task emulator 
            """
            
            
            #set format string for display
            
            formatstring="Temperature:\n\tTime: "+str(datetime.now().isoformat())+"\n\tCurrent: "+str(current)+"\n\tAverage: "+str(avg)+"\n\tSamples :  10\n\tMin: "+str(min)+"\n\tMAX :"+str(max)
            FORMAT = " %(message)s"
            logging.basicConfig(level=logging.INFO,format=FORMAT)
            logging.info(formatstring)
            smtpobj = SMTPemailclass()
            
            
            
            #the condition that current temp if increases drastically send email
            
            if(abs(avg-current)>4):
                topic="ALert : Sudden Temperature increase above threshold"
                data="\n"+formatstring+"\n"   #"The temperature has suddenly changed to high percent value from average "+str(avg)+"to a sudden change of "+str(current)+"This is an auto generated email"
                smtpobj.sendemailmethod(topic, data)
                print("email sent")
                logging.info("Suddent temperatre change")
    
            
        
            
            
                