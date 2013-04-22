'''
    __name__ = 'testtools.player.py'

    __description__ = 'Tests the minigame.tools.players.py module'
    __author__ = 'Kyle Roux'
'''
import minigame.tools.players as players
import unittest

class FuncTest(unittest.TestCase):
    def setUp(self):
        self.test1 = players.Player('test1')
        self.test2 = players.Player('test2')
        self.test3 = players.Player('test3')
        self.testers = [self.test1, self.test2, self.test3]
        #players.Player.set_order(self.testers)

    def tearDown(self):
        del(self.test1)
        del(self.test2)
        del(self.test3)

    def test_next_player(self):
        players.Player.next_player()
        nextPlayer = players.Player.get_player_name(players.Player.get_current())
        #players.Player._currentPlayer = 1
        self.assertEquals('test2', nextPlayer)



    def test_prev_player(self):
        players.Player.prev_player()
        players.Player.prev_player()
        prevPlayer = players.Player.get_player_name(players.Player.get_current())
        self.assertEquals('test3', prevPlayer)

    def test_player_get_name(self):
        pass


if __name__ == "__main__":
    unittest.main()

