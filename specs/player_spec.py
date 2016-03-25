import unittest
import sys

sys.path.insert(0, "../lib")
from player import Player

class PlayerSpec(unittest.TestCase):
    def test(self):
        player_one = Player("Adam")
        player_two = Player("Sarah")

        self.assertTrue(player_one.name == "Adam")
        self.assertTrue(player_two.name == "Sarah")
        self.assertTrue(player_one.dice == 6 and player_two.dice == 6)
