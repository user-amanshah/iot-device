'''
Created on Feb 1, 2020
 
@author: amanshah
'''
import configparser
from distutils.command.config import config
import os
 
class ConfigUtil(object):
    '''
    classdocs
    '''
    config = configparser.ConfigParser()
    config.read("A:\git-repos\workspace\iot-device\config\ConnectedDevicesConfig.props")
    pathvar="A:\git-repos\workspace\iot-device\config\ConnectedDevicesConfig.props"
       
#     config['smtp.cloud']['port']
#                

    def __init__(self):
        return

          
    def getdirectory(self):
        
        return self.pathvar
    
    
    def getSMTPhost(self):
        config = configparser.ConfigParser()
        config.read(self.pathvar)
        smtp_host=config['smtp.cloud']['host']
        return str(smtp_host)
     
    def getSMTPport(self):
        config = configparser.ConfigParser()
        config.read(self.pathvar)
        smtp_port=config['smtp.cloud']['port']
        return str(smtp_port)
         

         
    def getSMTPfromAddr(self):
        config = configparser.ConfigParser()
        config.read(self.pathvar)
        smtp_from=config['smtp.cloud']['fromAddr']
        return str(smtp_from)
     
    def getSMTPtoAddr(self):
        config = configparser.ConfigParser()
        config.read(self.pathvar)
        smtp_toaddress=config['smtp.cloud']['toAddr']
        return str(smtp_toaddress)
     
    def getSMTPtoken(self):
        config = configparser.ConfigParser()
        config.read(self.pathvar)
        token=config['smtp.cloud']['token']
        return token    
          
          
    def getpassword(self):
        config = configparser.ConfigParser()
        config.read(self.pathvar)
        smtp_password=config['smtp.cloud']['password']
        return str(smtp_password)
                   
    
    def getvalue(self,key,value):
        config = configparser.ConfigParser()
        config.read(self.pathvar)
        smtp_para=config[key][value]
        return smtp_para
    
    
    def loadconfig(self):
        path_var="A:\git-repos\workspace\iot-device\config\ConnectedDevicesConfig.props"
        load=os.path.isfile(path_var)
        if load is True:
            return True
        else:
            return False
        
  
    def hasconfig(self,key,value):
        load=self.getvalue(key, value)
        if load is not None:
            return True
        else:
            return False
        
        
     