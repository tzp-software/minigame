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

    def add_to_all(self, oneOrFive, num):
        '''first set score'''
        if oneOrFive == 1:
            score = 100
        else:
            score = 50
        self.scores.append(score)
        self.scoringRolls.append(oneOrFive,)
        if num == 2:
            self.scores.append(score*2)
            self.scoringRolls.append((oneOrFive, oneOrFive))

    def add_to_scores(self, item):
        self.scores.append(item)

    def add_to_rolls(self, item):
        self.scoringRolls.append(item)

    def check_ones(self):
        if self.ones >= 1:
            self.add_to_all(1, self.ones)
        if self.ones >=3:
            if self.ones == 3:
                self.add_to_scores(1000)
                self.add_to_rolls((1,1,1))
            elif self.ones == 4:
                self.add_to_scores(2000)
                self.add_to_rolls((1,1,1,1))
            elif self.ones == 5:
                self.add_to_scores(4000)
                self.add_to_rolls((1,1,1,1,1))
            else:
                self.add_to_scores(8000)
                self.add_to_rolls((1,1,1,1,1,1))
            
    def check_twos(self):
        if self.twos >= 3:
            if self.twos == 3:
                self.add_to_scores(200)
                self.add_to_rolls((2,2,2))
            elif self.twos == 4:
                self.add_to_scores(400)
                self.add_to_rolls((2,2,2,2))
            elif self.twos == 5:
                self.add_to_scores(800)
                self.add_to_rolls((2,2,2,2,2))
            else:
                self.add_to_scores(1600)
                self.add_to_rolls((2,2,2,2,2,2))

    def check_threes(self):
        if self.threes >= 3:
            if self.threes == 3:
                self.add_to_scores(300)
                self.add_to_rolls((3,3,3))
            elif self.threes == 4:
                self.add_to_scores(600)
                self.add_to_rolls((3,3,3,3))
            elif self.threes == 5:
                self.add_to_scores(1200)
                self.add_to_rolls((3,3,3,3,3))
            else:
                self.add_to_scores(2400)
                self.add_to_rolls((3,3,3,3,3,3))


    def check_fours(self):
        if self.fours >= 3:
            if self.fours == 3:
                self.add_to_scores(400)
                self.add_to_rolls((4,4,4))
            elif self.fours == 4:
                self.add_to_scores(800)
                self.add_to_rolls((4,4,4,4))
            elif self.fours == 5:
                self.add_to_scores(1600)
                self.add_to_rolls((4,4,4,4,4))
            else:
                self.add_to_scores(3200)
                self.add_to_rolls((4,4,4,4,4,4))

    def check_fives(self):
        if self.fives >= 1:
            self.add_to_all(5, self.fives)
        if self.fives >= 3:
            if self.fives == 3:
                self.add_to_scores(500)
                self.add_to_rolls((5,5,5))
            elif self.fives == 4:
                self.add_to_scores(1000)
                self.add_to_rolls((5,5,5,5))
            elif self.fives == 5:
                self.add_to_scores(2000)
                self.add_to_rolls((5,5,5,5,5))
            else:
                self.add_to_scores(4000)
                self.add_to_rolls((5,5,5,5,5,5))

    def check_sixs(self):
        if self.sixs >= 3:
            if self.sixs == 3:
                self.add_to_scores(600)
                self.add_to_rolls((6,6,6))
            elif self.fives == 4:
                self.add_to_scores(1200)
                self.add_to_rolls((6,6,6,6))
            elif self.fives == 5:
                self.add_to_scores(2400)
                self.add_to_rolls((6,6,6,6,6))
            else:
                self.add_to_scores(4800)
                self.add_to_rolls((6,6,6,6,6,6))
    #
    #def check_strait(self):
    #    ones = 0
    #    for i in ['Ones','Twos','Threes','Fours','Fives','Sixes']:
    #        if self.__dict__[i] == 1:
    #            ones += 1
    #    if ones == 6:
    #        self.add_to_scores(1000)
    #        self.add_to_rolls((1,2,3,4,5,6)
    #
    #def check_doubles(self):
    #    return 0
    #
    def check_scores(self):
        self.check_ones()
        self.check_twos()
        self.check_threes()
        self.check_fours()
        self.check_fives()
        self.check_sixs()
        #self.check_strait()
        #self.check_doubles()


    def make_return(self):
        ret = []
        for i in range(len(self.scoringRolls)):
            ret.append((self.scoringRolls[i],self.scores[i]))
        ''' This is data to be requested by the control and sent to a view '''
        return tuple(ret)

def test():
    testDict = {'One': 2, 'Two': 2, 'Three': 1, 'Four': 0, 'Five': 0, 'Six': 1}
    sc = ScoreCard(testDict)
    sc.check_scores()
    x = sc.make_return()
    print x
    print x[1]
    print 'the score is {0}'.format(x[1][1])
    print 'The dies to be locked are {0}'.format(x[1][0])


if __name__ == "__main__":
    test()
