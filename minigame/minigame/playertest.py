'''
Created on Apr 10, 2013

@author: kyleroux
'''
import unittest
from player import DicePlayer
from maintest import testCount



class PlayerTest(unittest.TestCase):


    def setUp(self):
        global testCount
        testCount += 1
        self.testPlayer = DicePlayer('Tester')
        print 'Running test #{0}'.format(testCount)


    def tearDown(self):
        self.testPlayer = ''


    def test_print_stats(self):
        self.assertIsNone(self.testPlayer.print_stats())
        
    def test_add_points(self):
        self.testPlayer.add_points(100)
        self.assertEqual(self.testPlayer.score, 100)
        
    def test_print_roll(self):
        self.assertIsNone(self.testPlayer.print_roll())
        
    def test_return_roll(self):
        self.testPlayer.roll(6)
        self.assertEquals(len(self.testPlayer.hand), 6)
        
    
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()