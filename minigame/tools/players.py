'''
    __name__ = 'minigame.tools.players.py'
    __author__ = 'Kyle Roux'

'''

class Player(object):
    _count = 0
    _currentPlayer = 1
    _playerList = []

            
    def __init__(self, name=None):
        Player.inc_count()
        self.name = name
        self.orderNumber = Player.get_player_count()
        Player.add_player(self)

    def get_name(self):
        return self.name

    @staticmethod
    def get_current():
        return Player._currentPlayer
        
    @staticmethod
    def add_player(player):
        Player._playerList.append(player)
        

    @staticmethod
    def inc_count():
        Player._count += 1
        return Player._count
    


    #@staticmethod
    #def set_order(players=[]):
    #    num = 1
    #    if players is []:
    #        pass
    #    else:
    #        for player in players:
    #            player.orderNumber = num
    #            num += 1

    @staticmethod 
    def get_player(playerNumber):
        for player in Player._playerList:
            if player.orderNumber == int(playerNumber):
                return player
    
    @staticmethod
    def get_player_name(playerNumber):
        aPlayer  = Player.get_player(playerNumber)
        return aPlayer.get_name()

    @staticmethod
    def get_player_count():
        return Player._count

    @staticmethod
    def next_player():
        if Player.get_current() == Player.get_player_count():
            Player._currentPlayer = 1
        else:
            Player._currentPlayer += 1

        
    @staticmethod
    def prev_player():
        if int(Player.get_current()) == 1:
            Player._currentPlayer = Player.get_player_count()
        else:
            Player._currentPlayer -= 1


