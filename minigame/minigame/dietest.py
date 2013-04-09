'''
Created on Apr 9, 2013

@author: kyleroux
'''
import unittest, sys
from dice import Die

# set debug with --debug from the command line
DEBUG = False
if len(sys.argv) > 1:
    if sys.argv[1] == '--debug':
        DEBUG = True


class DieTest(unittest.TestCase):
    testCount = 0

    def setUp(self):
        Dietest.testCount += 1
        if (DEBUG):
            print 'Running test #{0}'.format(DieTest.testCount)
        self.die = Die()

    def testRollLessThanSeven(self):
        self.assertEquals(self.die.roll(6).value < 7, True)

    def testRollGreaterThanZero(self):
        self.assertEquals(self.die.roll(6).value > 0, True)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()