import random

class Player:
    def __init__(self) -> None:
        self.groups = 0
        pass
        
    def diceroll(self):
        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        dice3 = random.randrange(1,7)
        dice4 = random.randrange(1,7)

        groups = [sorted([dice1+dice2, dice3+dice4]), sorted([dice1+dice3,dice2+dice4]), sorted([dice1+dice4,dice2+dice3])]

        print("주사위: {0} {1} {2} {3}".format(dice1, dice2, dice3, dice4))
        print("조합: {0}".format(groups))
        
        self.groups = groups
        return groups

    def choice(self, groups):
        n = int(input("조합을 선택하시오: "))
        choice = groups[n-1]
        print(choice)
        return choice

class Map:
    def __init__(self) -> None:
        self.map = {2:[[],[],[]], 
                    3:[[],[],[],[],[]], 
                    4:[[],[],[],[],[],[],[]], 
                    5:[[],[],[],[],[],[],[],[],[]], 
                    6:[[],[],[],[],[],[],[],[],[],[],[]], 
                    7:[[],[],[],[],[],[],[],[],[],[],[],[],[]], 
                    8:[[],[],[],[],[],[],[],[],[],[],[]],
                    9:[[],[],[],[],[],[],[],[],[]], 
                    10:[[],[],[],[],[],[],[]], 
                    11:[[],[],[],[],[]], 
                    12:[[],[],[]]}

    def showmap(self):
        for i in self.map:
            print(map[i])
        pass

    def addplayer(self, choice, player):
        for i in choice:
            for j in self.map[i]:
                if j.count(player) == 0:
                    j.append(player)
                    break
                else:
                    continue



class Game:
    def __init__(self, player1, player2, player3, map) -> None:
        print("Can't stop\n\n\n")

        self.p1 = player1
        self.p2 = player2
        self.p3 = player3
        self.map = map
        r = random.randrange(1,4)
        print("Player {0}이 선공입니다.\n".format(r))
        self.first = r
        pass

    def main(self):
        now_player = self.first

        while True:
            print("현재 플레이어는 Player {0}입니다.\n".format(now_player))

            if now_player == 1:
                groups = self.p1.diceroll()
                choice = self.p1.choice(groups)
                self.map.addplayer(choice, now_player)
                self.map.showmap()

                now_player = 2
            elif now_player == 2:
                groups = self.p2.diceroll()
                choice = self.p2.choice(groups)
                self.map.addplayer(choice, now_player)
                self.map.showmap()
                
                now_player = 3
            else:
                groups = self.p3.diceroll()
                choice = self.p3.choice(groups)
                self.map.addplayer(choice, now_player)
                self.map.showmap()
                
                now_player = 1

            

player1 = Player()
player2 = Player()
player3 = Player()
map = Map()

game = Game(player1, player2, player3, map)

game.main()