'''
    minigame.player.py
    
        player logic for minigame
'''

class Player(object):
    _players = [][:]
    _playerCount = 0 # Use this to give player numbers and such
    
    
    def print_scores():
        for player in Player._players:
            print player
    print_scores = staticmethod(print_scores)
    
    def __init__(self, name=None):
        Player._playerCount += 1
        self.playerNumber = Player._playerCount
        if name is None:
            self.name = 'Player #{0}'.format(self.playerNumber)
        else:
            self.name = name
        self.score = 0
        Player._players.append(self)
        
    def __str__(self):
        return self.name + ' : ' + str(self.score)
    
    def print_stats(self):
        print self

    def add_points(self, points):
        if points > 0:
            self.score += points
        else:
            raise ValueError
        
        
        
kyle = Player('kyle')
kyle.add_points(800)
#tkyle.print_stats()
jill = Player('jill')
jill.add_points(100)
Player.print_scores()