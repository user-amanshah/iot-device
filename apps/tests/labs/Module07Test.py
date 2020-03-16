import unittest
"""
Test class for all requisite Module07 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
from labs.module07.CoapClientConnector import CoapClientConnector
from labbenchstudios.common.ConfigUtil import ConfigUtil


class Module07Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	
	
	def setUp(self):
		host = '127.0.0.1'
		#port number to connect
		port = 5683
		#resource uri
		path = 'temperature'
		self.coap_client = CoapClientConnector(host,port,path)
	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		#setting to none to destroy
		self.coap_client = None

	"""
 Method to check ping 
	"""
	def test_pinging(self):
		"""start ping test"""
		assert(self.coap_client.ping())	
	"""	Method to check GET	"""
	
	def test_get_method(self):
		"""start get test"""
		assert(self.coap_client.get())
		
	"""
 Method to check PUT
	"""
	def test_put_method(self):
		#demo json data
		jsonData="{'name': 'temperature'}" 
		assert(self.coap_client.put(jsonData))
		
		
	"""
 Method to check POST
	"""
	def test_post_method(self):
		jsonData="{'name': 'temperature'}" 
		assert(self.coap_client.post(jsonData))
				
	"""
 Method to check DELETE	
	"""
	def test_delete_method(self): 
		assert(self.coap_client.delete())
		
			
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
