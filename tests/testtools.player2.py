
import minigame.tools.players as players
import unittest

class PlayerTest(unittest.TestCase):
    def setUp (self):
        self.player1 = players.Player("player1")
        self.player2 = players.Player("player2")
        self.player3 = players.Player("player3")
        self.player4 = players.Player("player4")


    def test_last_to_first_player(self):
        for i in range(4):
            players.Player.next_player()
        nextPlayer = players.Player.get_player_name(players.Player.get_current())
        self.assertEquals('player1', nextPlayer)

if __name__ == "__main__":
    unittest.main()  
