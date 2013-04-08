'''
    minigame.dice.py

    __author__ = 'kyle roux'
'''
import random

class Die(object):
    ''' A Die is a six sided die unless you give it a number.
    a Die automaticlly rolls itself.'''
    def __init__(self, num=None):
        '''you can give it an inital number for sides or not. self.value
        will be a random int from 1 to 6(or th given number'''
        if num is None:
            self.num = 6
        else:
            self.num = num
        self.roll()
    
    def roll(self, num=None):
        ''' give a number to roll a new N sided die'''
        if num is None:
            num = self.num
        self.value = random.randrange(1, num)
    
    def __str__(self):
        '''returns self.value'''
        return str(self.value)
    
    def __int__(self):
        '''returns self.value'''
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

    def return_roll(self):
        '''public api access to Die.value'''
        tmpRoll = [][:]
        for i in self.dice:
            tmpRoll.append(int(i.value))
        return tuple(tmpRoll)

def test():
    x = Die(6)
    x.roll()
    print x
    y = Roll()
    y.print_roll()
    print
    #print y.dice[3]
    
    print y.return_roll()[2]
    
if __name__ == '__main__':
    test()
