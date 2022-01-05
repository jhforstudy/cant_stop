from player import Player
from map import Map
from game import Game


player1 = Player()
player2 = Player()
player3 = Player()
map = Map()

game = Game(player1, player2, player3, map)

game.main()