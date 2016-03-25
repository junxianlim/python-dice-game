import unittest
import sys

sys.path.insert(0, "../lib")
from dice import Dice

class DiceSpec(unittest.TestCase):
    def test(self):
        rolls = []
        for i in range(100):
            rolls.append(Dice.roll())
        self.assertFalse(0 in rolls and 7 in rolls)
