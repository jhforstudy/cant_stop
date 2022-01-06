from player import Player
from game import Game
from logo import printlogo
import time

while True:
    printlogo()
    time.sleep(1)
    player1 = Player(0)
    player2 = Player(1)
    player3 = Player(2)

    game = Game(player1, player2, player3)

    game.main()