'''
    minigame.scorescard.py

    most scoring logic in minigame for 
    my dice game

    by: kyle roux
'''

class ScoreCard(object):
    ''' scores a roll. 
    input:  dict - a pre-counted roll {'one': 2} == 1, 1
    return tuple of scoring rolls or None
    ie:
        if 1, 2, 1, 5, 1, 6
        return:
        ((1, 1, 1, 1000), (1, 100), (1, 1, 200), 
        (1, 5, 150), (5, 50), (1, 1, 1, 5, 1050))
    '''
    def __init__(self, rollDict=None):
        if rollDict is None or type(rollDict) != type(dict()):
            raise ValueError('Need a roll as a dict')
        else:
            self.roll = rollDict.copy()
            self.ones = rollDict['One']
            self.twos = rollDict['Two']
            self.threes = rollDict['Three']
            self.fours = rollDict['Four']
            self.fives = rollDict['Five']
            self.sixs = rollDict['Six']
        self.scoringRolls = []
        self.scores = []
        self.tmp = 0

    def make_return(self):
        ret = []
        for i in range(len(self.scoringRolls)):
            ret.append((self.scoringRolls[i],self.scores[i]))
        return tuple(ret)

def test():
    testDict = {'One': 2, 'Two': 2, 'Three': 1, 'Four': 0, 'Five': 0, 'Six': 1}
    sc = ScoreCard(testDict)
    sc.scoringRolls = [(1,),(1,1)]
    sc.scores = [100,200]
    print sc.make_return()[0]
    print 'the score is {0}'.format(sc.make_return()[0][-1])

if __name__ == "__main__":
    test()
