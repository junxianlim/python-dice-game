from random import randint

class Dice(object):
    @classmethod
    def roll(cls):
        return randint(1,6)
