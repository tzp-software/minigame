'''
Created on Apr 9, 2013

@author: kyleroux
'''
import unittest, sys
from dice import Die
from dice import Roll
from maintest import testCount

# set debug with --debug from the command line
DEBUG = True
if len(sys.argv) > 1:
    if sys.argv[1] == '--debug':
        DEBUG = True


class DieTest(unittest.TestCase):
    

    def setUp(self):
        global testCount
        testCount += 1
        if (DEBUG):
            print 'Running test #{0}'.format(testCount)
        self.die = Die()

    def testRollLessThanSeven(self):
        self.assertEquals(self.die.value < 7, True)

    def testRollGreaterThanZero(self):
        self.assertEquals(self.die.value > 0, True)
        
class RollTest(unittest.TestCase):
    
    def setUp(self):
        global testCount 
        testCount += 1
        print 'Running test #{0}'.format(testCount)
        self.roll = Roll(6)
    
    def tearDown(self):
        self.roll = None
        
    def testDieOne(self):
        self.assertEquals(self.roll.return_roll()[0] < 7, True)
        self.assertEquals(self.roll.return_roll()[0] > 0, True)
        
    def testDieTwo(self):
        self.assertEquals(self.roll.return_roll()[1] < 7, True)
        self.assertEquals(self.roll.return_roll()[1] > 0, True)
        
    def testDieThree(self):
        self.assertEquals(self.roll.return_roll()[2] < 7, True)
        self.assertEquals(self.roll.return_roll()[2] > 0, True)

    def testDieFour(self):
        self.assertEquals(self.roll.return_roll()[3] < 7, True)
        self.assertEquals(self.roll.return_roll()[3] > 0, True)
    
    def testDieFive(self):
        self.assertEquals(self.roll.return_roll()[4] < 7, True)
        self.assertEquals(self.roll.return_roll()[4] > 0, True)    
        
    def testDieSix(self):
        self.assertEquals(self.roll.return_roll()[5] < 7, True)
        self.assertEquals(self.roll.return_roll()[5] > 0, True)
        
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()