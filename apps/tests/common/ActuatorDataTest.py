import unittest


"""
Test class for all requisite ActuatorData functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
from labs.module04.ActuatorData import ActuatorData


class ActuatorDataTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.actuator_data_command= ActuatorData("increase",0,"").getcommand()
		self.actuator_data_value= ActuatorData("",0.0,"").getValue()
		self.actuator_data_name= ActuatorData("",0,"temperature").getName()

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		self.actuator_data=None
		self.actuator_data_command=None
		self.actuator_data_name=None
		
	
	"""
	Place your comments describing the test here.
	"""
	def test_actuator(self):
		self.assertTrue(isinstance(self.actuator_data_command, str), "command is string")
		self.assertTrue(isinstance(self.actuator_data_name, str), "name is string")
		self.assertTrue(isinstance(self.actuator_data_value, float), "value is float")
		pass

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()