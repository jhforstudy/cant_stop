import random

class Player:
    def __init__(self, id) -> None:
        self.id = id
        self.score = 0
        self.player_name = input(f"Player {id+1}의 이름을 입력하시오. : ")
        self.basecamp = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
        pass
        
    def diceroll(self):
        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        dice3 = random.randrange(1,7)
        dice4 = random.randrange(1,7)

        groups = [sorted([dice1+dice2, dice3+dice4]), sorted([dice1+dice3,dice2+dice4]), sorted([dice1+dice4,dice2+dice3])]

        for i in groups:
            if groups.count(i) >= 2:
                groups.remove(i)

        print(f"주사위: {dice1} {dice2} {dice3} {dice4}")
        print(f"조합 : {groups}")
        
        choice = int(input("조합을 선택하시오: "))
        your_choice = groups[choice-1]

        return your_choice


def main():
    '''player = Player()
    a = player.diceroll()
    print(a)'''
    pass
    
if __name__ == "__main__":
    main()