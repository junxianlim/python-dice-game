from dice import Dice
from player import Player
from time import sleep

class Game(object):

    def __init__(self, player_numbers):
        self.players = []
        for i in range(player_numbers):
            new_player = Player(str(i))
            print(new_player.name + " has joined the game.")
            self.players.append(new_player)
        self.winners = []
        self.round = 1

    def start(self):

        sleep(1)
        print("Game is about to start!")
        sleep(2)

        while len(self.winners) < 1:

            sleep(1)
            print("---------- ROUND " + str(self.round) + " ----------")
            for player in self.players:
                results = []
                for i in range(player.dice):
                    result = Dice.roll()
                    results.append(result)
                    if result == 6:
                        player.dice -= 1

                print(player.name + " rolled the numbers " + str(results))
                print(player.name + " has " + str(player.dice) + " dice remaining.")

                if player.dice < 1:
                    self.winners.append(player)

            self.round +=1

        print("--------------------------")
        print("Game Over!")
        sleep(1)
        for player in self.winners:
            print(player.name + " has " + str(player.dice) + " remaining dice and won the game!")
