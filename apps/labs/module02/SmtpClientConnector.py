'''
Created on Feb 1, 2020
 
@author: amanshah
'''
 
from labbenchstudios.common.ConfigUtil import ConfigUtil
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class SMTPemailclass(object):
    '''
    classdocs
    '''
#     def __init__(self):
#         '''
#         Constructor
#         '''



    """
    we use smtplib to send emails when trigger condition is satisfied
    """


         
    def sendemailmethod(self, topic, data):
        
   
        config= ConfigUtil()
        print(config.loadconfig())
        
        logging.info('Configuration data...\n' )
        host = config.getSMTPhost()
        print(host)
        port = config.getSMTPport()
        print(port)
        fromAddr = config.getSMTPfromAddr()
        toAddr = config.getSMTPtoAddr()
        password=config.getpassword()
        
        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic
        msgBody = str(data)
        msg.attach(MIMEText(msgBody))
        msgText = msg.as_string()           #Return the entire message flattened as a string.
        # send e-mail notification
        """
        start smtp server sending instance to send the message 
        """
        smtpServer = smtplib.SMTP(host, port)
        #smtpServer.set_debuglevel(True)        #set true for debbuging process
        smtpServer.ehlo()
        smtpServer.starttls()
        smtpServer.login(fromAddr, password)
        smtpServer.ehlo()
        smtpServer.sendmail(fromAddr,toAddr,msgBody)
        smtpServer.close()
