import time
import unittest
from Reption import Repetion
from ddt import ddt,data,unpack
@ddt
class MyTestCase(unittest.TestCase):
    def steUp(self) ->None:
        
        time.sleep(0.01)

    def tearDown(self) -> None:
        time.sleep(0.01)

    @data([5,6,11],[-5,6,1],[5,-6,-1],[-5,-6,-10])
    @unpack
    def testadd(self,num1,num2,s):
        r = Repetion()
        sum=r.TestAdd(num1,num2)
        self.assertEqual(sum, s)
    @data([5,6,-1],[-5,6,-11],[5,-6,11],[-5,-6,1])
    @unpack
    def testsubtract(self,num1,num2,s):
        r = Repetion()
        sum=r.TestSubtract(num1,num2)
        self.assertEqual(sum, s)
    @data([5,6,30],[-5,6,-30],[5,-6,-30],[-5,-6,3])
    @unpack
    def testmultiply(self,num1,num2,s):
        r = Repetion()
        sum=r.TestMultiply(num1,num2)
        self.assertEqual(sum, s)
    @data([10,5,2],[-10,5,-2],[10,-5,-2],[-10,-5,20])
    @unpack
    def testdivide(self,num1,num2,s):
        r = Repetion()
        sum=r.TestDivide(num1,num2)
        self.assertEqual(sum, s)

if __name__ == '__main__':
    unittest.main()
