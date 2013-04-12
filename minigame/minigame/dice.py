'''
    minigame.dice.py

    __author__ = 'kyle roux'
'''
import random
from locker import FileLocker as DieLocker

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
    ''' Represents a roll of n number of dice'''
    def __init__(self, numberOfDice=6):
        ''' you can create a Roll with a number
        ie: Roll(4) to roll 4 dice, or it will
        just roll 6 dice by default.'''
        if numberOfDice <= 0:
            raise ValueError
        self.dieNum = numberOfDice
        self.roll()
        
    def __len__(self):
        ''' return how many dice were rolled '''
        return len(self.dice)

    def roll(self, num=None):
        ''' you can roll n number of dice,
        Roll.roll(n) or just Roll.roll() for
        the original number of dice rolled.'''
        if num is None:
            rollNum = self.dieNum
        else:
            rollNum = num
        self.dice = [0]*rollNum
        for i in range(len(self.dice)):
            self.dice[i] = Die()
        self._reset()
        
    def _reset(self):
        ''' actually roll each die in roll '''
        if self.dice:
            for i in self.dice:
                i.roll()
            
    
    def print_roll(self):
        ''' pretty print all dies in roll '''
        string = ''
        for i in self.dice:
            print str(i) + string,

    def return_roll(self):
        '''public api access to Die.value'''
        tmpRoll = [][:]
        for i in self.dice:
            tmpRoll.append(int(i.value))
        return tuple(tmpRoll)


class DieCounter(object):
    ''' use to pass around die counts(for scoring) '''
    def __init__(self):
        pass
    
    def reset_count(self):
        ''' needed internally'''
        self._faces = {'One' : 0, 'Two' : 0, 'Three' : 0, 'Four' : 0, 'Five' : 0, 'Six' : 0}.copy()
        self._faceMap = [None, 'One', 'Two', 'Three', 'Four', 'Five' ,'Six'][:] 
    
    def count_roll(self, roll):
        ''' counting algorithm'''
        self.reset_count()
        for die in roll:
            face = self._faceMap[die]
            self._faces[face] += 1
        count = self._faces.copy()
        return count
    
    def check_three_or_more(self, roll):
        ''' scoring (maybe move)'''
        count = self.count_roll(roll)
        save = [][:]
        for i in count:
            if count[i] >= 3:
                print "{0} {1}'s".format(count[i],i)
                save.append(i)
        '''if a number had 3 or more'''
        if len(save) > 0:
            '''return it'''
            return self._faceMap.index(str(save[0]))
        else:
            return None
            
        
def test():
    x = Die(6)
    x.roll()
    print x
    y = Roll()
    y.print_roll()
    print
    #print y.dice[3]
    
    print y.return_roll()[2]
    c = DieCounter()
    print c.count_roll(y.return_roll())
    print c.check_three_or_more(y.return_roll())
    print c._faceMap
    lock = DieLocker()
    lock.lock_item(y.dice[1])
    lock.lock_item(y.dice[1])
    print lock

if __name__ == '__main__':
    test()
