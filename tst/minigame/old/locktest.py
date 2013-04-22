'''
    minigame.testlocker.py
'''
from locker import FileLocker as TestLocker
from maintest import testCount
import unittest


class LockTest(unittest.TestCase):
    def setUp(self):
        global testCount
        testCount += 1
        print 'Running test #{0}'.format(testCount)
        self.tester = TestLocker()
        self.tester.lock_item('test')

    def tearDown(self):
        self.tester = ''

    def testLockCount(self):
        self.assertEqual(self.tester.lock_number(), 1)

    def testLockQuery(self):
        self.assertEqual(self.tester.lock_number('test'), 0)

if __name__ == "__main__":
    unittest.main()
        
    

