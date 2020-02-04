import unittest
#import labs.module01.SystemCPUUtilTask
#import labs.module01.SystemMemoryUtilTask 
from labs.module01.SystemMemoryUtilTask import SystemMemoryUtilTask
from labs.module01.SystemCPUUtilTask import SystemCPUUtilTask


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
class Module01Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	
	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
 	
	def test_checkfloat(self):
		
		
		"""
		we will use this method to check if the return type from psutils
		are float or some other value
		
		we will instantiate classes 
		the unit test should assert true is the return type  of method are 
		of float type
		else the test should fail 
		
		
		"""
		memvar= SystemMemoryUtilTask()
		cpuvar = SystemCPUUtilTask()
		
		
		
		self.assertTrue(isinstance(memvar.calculateMemory(), float)," its a float")
		self.assertTrue(isinstance(cpuvar.calculatecpuUtil(),float)," it is a float")
		#pass
	
	"""
	Place your comments describing the test here.
	"""
	def test_range(self):				
		
		
		"""
		we are testing if the cpu util and mem util is in range of 0 to 100
		since it is inpercent values it will be below 100
		we will initialize classes which we want to test 
		test cases should return true if conditions are met properly else should
		return test fail
		"""
		
		memvar= SystemMemoryUtilTask()
		cpuvar = SystemCPUUtilTask()
		
		
		self.assertTrue( 0.0 < memvar.calculateMemory()< 100.0 , " it is in range")
		self.assertTrue( 0.0 < cpuvar.calculatecpuUtil() < 100.0 , " it is in range")
		
		
		#self.assertTrue(isinstance(cpuvar.calculatecpuUtil(), float), "it is a float")
		pass

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()