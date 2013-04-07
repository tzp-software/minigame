'''
    minigame.dice.py

    __author__ = 'kyle roux'
'''
import random

class Die(object):
    def __init__(self, num=None):
        if num is None:
            self.num = 6
        else:
            self.num = num
        self.roll()
    
    def roll(self, num=None):
        if num is None:
            num = self.num
        self.value = random.randrange(1, num)
    
    def __str__(self):
        return str(self.value)
    
    def __int__(self,):
        return self.value

class Roll(object):
    def __init__(self, numberOfDice=6):
        if numberOfDice <= 0:
            raise ValueError
        self.dieNum = numberOfDice
        self.roll()
        
    def roll(self, num=None):
        if num is None:
            rollNum = self.dieNum
        else:
            rollNum = num
        self.dice = [0]*rollNum
        for i in range(len(self.dice)):
            self.dice[i] = Die()
        self._reset()
        
    def _reset(self):
        if self.dice:
            for i in self.dice:
                i.roll()
            
    
    def print_roll(self):
        string = ''
        for i in self.dice:
            print str(i) + string,

def test():
    x = Die(6)
    x.roll()
    print x
    y = Roll()
    y.print_roll()
    print
    print y.dice[3]
if __name__ == '__main__':
    test()
