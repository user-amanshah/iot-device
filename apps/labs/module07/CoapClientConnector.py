from coapthon.client.helperclient import HelperClient

# from coapthon
class CoapClientConnector(object):
    '''
    connects to the CoAP server
    '''
    def __init__(self, host, port, path):
        '''
        constructor
        initialize client_obj
        set up host port and path name
        '''
        self.host = host
        self.port = port
        self.path = path
        self.client_obj = HelperClient(server=(host, port))
    
    def ping(self):
        '''
        pinging the server
        '''    
        self.client_obj.send_empty("")
        return True
        
        
    def get(self):
        '''
        declaring GET request of Coap
        '''
        response = self.client_obj.get(self.path)
        print(response.pretty_print())
        return True
    
    def post(self, jsonData):
        '''
        function to POST request of Coap
        '''
        response = self.client_obj.post(self.path, jsonData)
        #use pretty print to display json
        print(response.pretty_print())
        return True
    
    def put(self, jsonData):
        '''
        function for the PUT action of Coap
        '''
        response = self.client_obj.put(self.path, jsonData)
        print(response.pretty_print())
        return True
    def delete(self):
        '''function to DELETE  request of Coap''' 
        response = self.client_obj.delete(self.path)
        #use pretty print for json display
        print(response.pretty_print())
        return True
        
    def stop(self):
        '''function to terminting'''  
        self.client_obj.stop()  
        return True      