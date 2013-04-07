'''
    minigame.dice.py

    __author__ = 'kyle roux'
'''
import random

class Die(object):
    def __init__(self, num=None):
        if num is None:
            raise ValueError
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
    

def test():
    x = Die(6)
    x.roll()
    print x
    
if __name__ == '__main__':
    test()
