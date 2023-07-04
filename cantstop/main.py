from player import Player
from game import Game
from logo import printlogo
import time

while True:
    printlogo()
    time.sleep(1)

    while True:
        player_num = int(input("플레이어 수를 입력하시오(2 ~ 4) : "))
        
        if 2 <= player_num <= 4:
            break
        
        print("다시 입력하시오.\n")
    
    print()

    if player_num == 2:
        players = [Player(0), Player(1)]
    elif player_num == 3:
        players = [Player(0), Player(1), Player(2)]
    else:
        players = [Player(0), Player(1), Player(2), Player(3)]

    game = Game(player_num, players)

    game.main()