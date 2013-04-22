
'''
    __file__ = 'minigame.games.cards.py'
    __author__ = 'Kyle Roux'
    __author_email__ = 'jstacoder@gmail.com'
    __date__ = 'Mon Apr 22 10:20:54 2013'
    __lisence__ = 'bsd'
    TODO: Deck.shuffle(num=1) Deck.deal(num)-> pop    Deck.make_discard_pile() 
'''
import random

class Card(object):
    ''' a Card is a single playing card, it have a value and suite'''
    def __init__(self, suite, value):
        self.value = value
        self.suite = suite

    def __str__(self):
        rtn = '{0} of {1}'.format(self.value, self.suite)
        return rtn

    def __repr__(self):
        rtn = '{0} of {1}'.format(self.value, self.suite)
        return rtn

    def get_suite(self):
        return self.suite

    def get_value(self):
        return self.value

    def get_tuple(self):
        return (self.get_suite(), self.get_value())


class Deck(object):
    ''' a Deck is a container/manager for Card instances'''

    _values = range(1,11) + 'Jack Queen King'.split()
    _suites = 'Hearts Clubs Diamonds Spades'.split()
    
    def __init__(self):
        self.deck = self.get_deck()

    def get_deck(self):
        rtn = []
        deck = [(v,s) for v in Deck._values for s in Deck._suites]
        for card in deck:
            rtn.append(Card(card[1],card[0]))
        return rtn

    def pprint_(self):
        for i in self.deck:
          print i
          print

if __name__ == "__main__":
    x = Deck()
    x.pprint_()





