import unittest

from labs.module06.MqttClientConnector import MqttClientConnector
from labbenchstudios.common.SensorData import SensorData
from tkinter.constants import NO
"""
Test class for all requisite Module06 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class Module06Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		"""set up all the labs and labbenchstudios classes """
		#initialize mqtt and sensor data
		
		self.mqtt_obj = MqttClientConnector()
		self.sensor_obj = SensorData()
		

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		"""set initialize variables as none to destroy/"""
		self.mqtt_obj= None
		self.sensor_obj= None

	"""
	Place your comments describing the test here.
	"""
	def test_connection(self):
		"""check if connection of mqtt is susccess"""
		self.assertTrue(self.mqtt_obj.on_connect("","",0), "connection suceess")
		
	def test_publishing(self):
		"""check if publish is success"""
		self.assertTrue(self.mqtt_obj.publish_sensor_data(self.sensor_obj))
		
	def test_disconnect(self):
		self.assertTrue(self.mqtt_obj.on_disconnect("",0), "its disconnected")
	
	
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()