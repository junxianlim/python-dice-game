from dice import Dice
from player import Player
from time import sleep

class Game(object):
    @classmethod
    def start(cls, player_numbers):
        players = []
        winners = []
        round = 1

        for i in range(player_numbers):
            new_player = Player(str(i))
            print(new_player.name + " has joined the game.")
            players.append(new_player)

        sleep(1)
        print("Game is about to start!")
        sleep(2)

        while len(winners) < 1:

            sleep(1)
            print("---------- ROUND " + str(round) + " ----------")
            for player in players:
                results = []
                for i in range(player.dice):
                    result = Dice.roll()
                    results.append(result)
                    if result == 6:
                        player.dice -= 1

                print(player.name + " rolled the numbers " + str(results))
                print(player.name + " has " + str(player.dice) + " dice remaining.")

                if player.dice < 1:
                    winners.append(player)

            round +=1

        print("--------------------------")
        print("Game Over!")
        sleep(1)
        for player in winners:
            print(player.name + " has " + str(player.dice) + " remaining and won the game!")

Game.start(4)
