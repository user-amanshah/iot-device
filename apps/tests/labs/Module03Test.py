import unittest


"""
Test class for all requisite Module03 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""

#from labs.module04.TempSensorAdaptorTask import TempSensorAdaptorTask
#from labs.module04.TempSensorAdaptor import TempSensorAdaptor
from labs.module03.SensorDataManager import SensorDataManager
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module03.TempSensorAdaptor import TempSensorAdaptor



class Module03Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		#self.adaptor= TempSensorAdaptorTask.getteravg()
		self.datamanager_avg= SensorDataManager().getteravg()
		self.datamanager_current= SensorDataManager().gettercurrent()
		self.datamanager_count= SensorDataManager().gettercount()
		self.adaptorTask_sensor= TempSensorAdaptorTask()
		self.sensorAdaptor= TempSensorAdaptor()
	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		self.adaptorTask_sensor=None
		self.datamanager_avg=None
		self.datamanager_current=None
		self.datamanager_count=None
		self.sensorAdaptor=None
		
	"""
	Place your comments describing the test here.
	"""
	def test_avg(self):
		self.assertTrue(isinstance(self.datamanager_avg, float), "avg is float")
		
	def test_current(self):
		self.assertTrue(isinstance(self.datamanager_current, float), "current value is float")
		
		
	def test_count(self):
		self.assertTrue(isinstance(self.datamanager_count, int), "current value is float")
	
	
	def test_sensorAdaptortask(self):
		self.assertTrue(self.adaptorTask_sensor.sensor, "Sensor instance created")

# 	
		
	

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()