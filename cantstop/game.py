import random
import time
import os
from player import Player

class Game:
    def __init__(self, player1, player2, player3) -> None:
        self.p1 = player1
        self.p2 = player2
        self.p3 = player3
        self.map = {2: [0,0,0], 
                    3: [0,0,0], 
                    4: [0,0,0], 
                    5: [0,0,0], 
                    6: [0,0,0],
                    7: [11,0,0], 
                    8: [0,0,0], 
                    9: [0,0,0], 
                    10: [0,0,0],
                    11: [0,0,0],
                    12: [0,0,0]
                    }

        self.now_p = {  2:0,
                        3:0,
                        4:0,
                        5:0,
                        6:0,
                        7:0,
                        8:0,
                        9:0,
                        10:0,
                        11:0,
                        12:0,
                        }

        self.score = 0

        print("Can't stop\n\n\n")
        #time.sleep(1)

        self.firstplayer = random.randrange(1,3)
        print(f"첫 번째 플레이어는 Player {self.firstplayer}입니다.\n\n\n")
        #time.sleep(1)

        print("게임을 시작하겠습니다.\n\n")
        #time.sleep(1)

    def oneloop(self, player: Player):
        #before game

        start_position = {2:True,
                        3:True,
                        4:True,
                        5:True,
                        6:True,
                        7:True,
                        8:True,
                        9:True,
                        10:True,
                        11:True,
                        12:True,
                        }

        while True:
            print("\n\n주사위를 굴립니다.")
            time.sleep(1)

            choice = player.diceroll()  # [3,7]

            # 다 넣었다고 가정했을 때 모든 개수들을 세어봄
            temp = []
            for i in choice:
                temp.append(i)
            for i in self.now_p:
                if self.now_p[i] != 0:
                    temp.append(i)

            temp = set(temp)

            # temp의 개수가 3 이하이면, 무조건 넣어야함
            if len(temp) <= 3:
                for i in choice: #now_p 에 +1
                    if start_position[i]:
                        self.now_p[i] += self.map[i][player.id] + 1
                        start_position[i] = False
                    else:
                        self.now_p[i] += 1

            # 만약 temp의 개수가 4개이면, 선택해야함
            elif len(temp) == 4:
                if self.numberofp() == 2: # 말의 개수가 2개이면, 둘 중 하나를 선택해서 놔야 함
                    print("2개 이상의 말을 놓을 수 없습니다. 어떤 말을 선택하시겠습니까?")
                    time.sleep(1)
                    c = int(input(f"{choice[0]} = 0 입력, {choice[1]} = 1 입력: "))
                    if start_position[choice[c]]:
                        self.now_p[choice[c]] += self.map[i][player.id] + 1
                    else:
                        self.now_p[choice[c]] += 1

                elif self.numberofp() == 3: # 말의 개수가 3개이면, 둘 중 있는 말을 자동으로 놔야 함
                    cnt = 0
                    for i in choice:
                        if self.now_p[i] != 0:
                            if start_position[i]:
                                self.now_p[i] += self.map[i][player.id] + 1
                                start_position[i] = False
                            else:
                                self.now_p[i] += 1
                            cnt += 1
                        else:
                            continue

                    if cnt == 0:
                        print("더 이상 말을 놓을 수 없습니다. 턴이 종료됩니다.")
                        time.sleep(1)
                        break
                
            # temp의 개수가 5개 이상이면, 더이상 진행 불가한 조합
            elif len(temp) >= 5:
                print("더 이상 말을 놓을 수 없습니다. 턴이 종료됩니다.")
                time.sleep(1)
                break

            self.showmap()

            if self.checktop():

                #self.score 가 꼭대기
                #player.id
                break

            print("계속 진행하시겠습니까? 아니면 베이스캠프를 세우시겠습니까?")
            gostop = int(input("GO = 1, STOP = 0 : "))

            if gostop == 1:
                continue
            else: 
                print("베이스캠프를 세우고 턴을 종료합니다.")
                time.sleep(1)
                # make a basecamp
                for i in self.now_p: #map 리스트 에 now_p의 값으로 변경
                    if self.now_p[i] != 0:
                        self.map[i][player.id] = self.now_p[i]
                break

        #after 1 round

        for i in self.now_p: #now_p 초기화
            self.now_p[i] = 0
        
        self.showmap()

    def showmap(self):
        
        os.system('cls')    # 화면 클리어
        for i in range(2,8):
            print(f"{i}\t: ", end='')
            n = 2 * (i-1)
            for j in range(n):
                # if j번째에 플레이어가 있으면 플레이어를 출력해야됨 j=0,1,2,3,4,...
                if self.map[i][0] == j+1:
                    print("A", end='')
                if self.map[i][1] == j+1:
                    print("B", end='')
                if self.map[i][2] == j+1:
                    print("C", end='')
                if self.now_p[i] == j+1:
                    print("P", end='')

                if j+1 not in self.map[i] and self.now_p[i] != j+1:
                    print("_", end='')

                print(end='\t')

            print("◎\n")

        for i in range(8,13):
            print(f"{i}\t: ", end='')
            n = 2 * (13-i)
            for j in range(n):
                # if j번째에 플레이어가 있으면 플레이어를 출력해야됨 j=0,1,2,3,4,...
                if self.map[i][0] == j+1:
                    print("A", end='')
                if self.map[i][1] == j+1:
                    print("B", end='')
                if self.map[i][2] == j+1:
                    print("C", end='')
                if self.now_p[i] == j+1:
                    print("P", end='')

                if j+1 not in self.map[i] and self.now_p[i] != j+1:
                    print("_", end='')

                print(end='\t')
            
            print("◎\n")

    def numberofp(self):
        cnt = 0
        for i in self.now_p:
            if self.now_p[i] != 0:
                cnt += 1

        return cnt

    def checktop(self):
        for i in range(2,7):
            top = 2 * i - 1 # 3
            if self.now_p[i] >= top:
                print("정상에 도달했습니다.")
                self.score = i

                return True

        for i in range(8,13):
            top = 2 * (14-i) - 1 # 3
            if self.now_p[i] >= top:
                print("정상에 도달했습니다.")

                return True

        return False


    def main(self):
        now_player = self.firstplayer

        while True:
            print(f"\n\n현재 플레이어는 Player {now_player}입니다.\n\n")
            time.sleep(1)
            
            if now_player == 1:
                self.oneloop(self.p1)
                now_player += 1
            
            elif now_player == 2:
                self.oneloop(self.p2)
                now_player += 1
            
            else:
                self.oneloop(self.p3)
                now_player = 1

            


def main():
    p1 = Player(0)
    p2 = Player(1)
    p3 = Player(2)

    game = Game(p1,p2,p3)
    game.main()
    #game.showmap()
         
if __name__ == "__main__":
    main()