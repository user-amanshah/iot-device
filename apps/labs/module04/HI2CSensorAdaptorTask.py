'''
Created on Feb 16, 2020

@author: amanshah
'''
import threading,random,logging
import smbus
from datetime import datetime
#from labbenchstudios.common import SensorData
import SensorData
import time
#from labs.module03 import SensorDataManager
import SensorDataManager



i2Cobj=smbus.SMBus(1)
# hts221 address on the I2C bus
i2c_humidity_hts211 = 0x5F
start_address_lsb= 0x28
start_address_msb= 0x29
controlreg=0x2D
measurereg =0x08

class HI2CSensorAdaptorTask(threading.Thread):
    '''
    classdocs
    '''

    """initialize variables globally her
    """
    avg=0.0
    current=0.0
    def getteravg(self):
        return self.avg
    
    def setteravg(self,avg):
        self.avg=avg
        
    def gettercurrent(self):
        return self.current
    def settercurrent(self,currentval):
        self.current=currentval
        
    def setterSensor(self,sensordataobj):
        self.sensor=sensordataobj
        
    def getterSensor(self):
        return self.sensor
    
    sensor= SensorData.SensorData()
    def __init__(self):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
    
    
    def convertsign_to_unsign_16bit(self,msb,lsb):
        value = (msb << 8 ) | lsb
        if value & (1 << 15 ):
            value = value - (1<<16)
            
        return value
            
  

    
    def run(self):
#         print("hellorun")
        humiditySensor(self)
        
        

      
        
def calculatehumidity(self):
    print("enter1")
    
    
    #Read H0_rH and H1_rH coefficients
    H0coeff=i2Cobj.read_byte_data(i2c_humidity_hts211,0x30)
    H1coeff=i2Cobj.read_byte_data(i2c_humidity_hts211,0x31)
    
    H0_RH=H0coeff/2  >>2
    H1_RH=H1coeff/2
    
    #Read the value of H0_T0_OUT from registers 0x36 & 0x37
    
    H0_T0_x36 = i2Cobj.read_byte_data(i2c_humidity_hts211,0x36)
    H0_T0_x37 = i2Cobj.read_byte_data(i2c_humidity_hts211,0x37)
    H0_TO_out = self.convertsign_to_unsign_16bit(H0_T0_x37,H0_T0_x36)
    
    #Read the value of H1_T0_OUT from registers 0x3A & 0x3B.
    
    H1_T0_x3A = i2Cobj.read_byte_data(i2c_humidity_hts211,0x3A)
    H1_T0_x3B = i2Cobj.read_byte_data(i2c_humidity_hts211,0x3B)
    H1_TO_out = self.convertsign_to_unsign_16bit(H1_T0_x3B, H1_T0_x3A)
    
        
    # Read the humidity value in raw counts H_T_OUT from registers 0x28 & 0x29
    
    H_T_OUT_0x28 = i2Cobj.read_byte_data(i2c_humidity_hts211,start_address_lsb)
    H_T_OUT_0x29 = i2Cobj.read_byte_data(i2c_humidity_hts211, start_address_msb)
    H_T_out = self.convertsign_to_unsign_16bit(H_T_OUT_0x29, H_T_OUT_0x28)
    
    
    #Compute the RH [%] value, by linear interpolation, applying the formula 
    
    humidty_rh = (H1_RH - H0_RH)*(H_T_out-H0_TO_out)
    percent_humidity = (humidty_rh/(H1_TO_out-H0_TO_out)) +H0_RH
    
#         writex= i2Cobj.read_i2c_block_data(i2c_humidity_hts211,start_address_lsb,6)
#         writey= i2Cobj.read_i2c_block_data(i2c_humidity_hts211,start_address_msb,6)
     
    
    print("percentage of humidity via i2c bus is :" + str(percent_humidity))
    return percent_humidity










    
def humiditySensor(self):
    data=self.sensor
    
    for i in range(1,4):
    #   temp=self.sense.get_temperature()
        #result= calculatehumidty(self)
        #print(result)
        result=calculatehumidity(self)
        data.addvalue(float(result))
        
        time.sleep(0.3)
        i+1
        
    avg=data.getterAvg()
    #print(avg)
    current_val= data.gettercurrent()
    #print(current_val)
    count= data.getterCount()
    max= data.getterMax()
    min= data.getterMin()
    
    self.setteravg(avg)
    self.settercurrent(current_val)
    
    
    
    
    
    """
    outputing file to console using logging
    """
    
    
    formatstring="Humidity:\n\tTime: "+str(datetime.now().isoformat())+"\n\tCurrent: "+str(current_val)+"\n\tAverage: "+str(avg)+"\n\tSamples :  10\n\tMin: "+str(min)+"\n\tMAX :"+str(max)
    FORMAT = " %(message)s"
    logging.basicConfig(level=logging.INFO,format=FORMAT)
    logging.info(formatstring)
    time.sleep(2)
    
    sensorhandler = SensorDataManager.SensorDataManager
    self.setterSensor(data)
    
    """ callback fuction """
    sensorhandler.manager_humidity(self,data)
    
    return avg,current_val,count,max,min
        
        
        