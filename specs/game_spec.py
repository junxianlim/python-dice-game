import unittest
import sys

sys.path.insert(0, "../lib")
from game import Game

class GameSpec(unittest.TestCase):
    def test(self):

        game = Game(4)
        game.start()
        for winner in game.winners:
            self.assertTrue(winner.dice == 0)
