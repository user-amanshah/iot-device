import unittest
from labbenchstudios.common import ConfigUtil
from labs.module02.TempSensorEmulatorTask import TempSensorEmulator
"""
Test class for all requisite Module02 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""




class Module02Test(unittest.TestCase):
	
	config_obj = ConfigUtil.ConfigUtil()
	emulator_obj = TempSensorEmulator()
	
	"""
	we load instance of the class modules we are n=gonna use 	"""

	def test_load(self):
		""" test the laod status of config file by checking absolute path and return of key values of data"""
							
		obj=self.config_obj
# 		
		self.assertTrue(obj.loadconfig() is True, "loaded property files")
		self.assertTrue(obj.hasconfig("smtp.cloud", "host") is not None, "config file return cloud parameter")
		
	
	
	def test_temperatur(self):
		""" we use this test case to validate temperature values recieved from the function"""
		
		"""if the values return are vague and out of range it will fail"""
		obj=self.emulator_obj
		#obj=TempSensorEmulatorTask.TempSensorEmulator()
		
		
		[count,avg,max,min,current]=obj.sensoremulator()
		self.assertTrue(0.0<count, "count validated")
		self.assertTrue(0.0<avg<100.0, "average temperature validated")
		self.assertTrue(0.0<max<100.0, "Maximum temperature validated")
		self.assertTrue(0.0<min<100.0, "Maximum temperature validated")
		
		


if __name__ == "__main__":
	# import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
