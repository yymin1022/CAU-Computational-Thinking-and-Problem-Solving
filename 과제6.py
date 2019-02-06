import random

player1 = str(input('1 플레이어의 이름은? '))
player2 = str(input('2 플레이어의 이름은? '))

# 현재 진행중인 라운드
round = 1

# 두 플레이어의 위치를 출발지점(0)으로 초기화
current1 = 0
current2 = 0

while current1<30 and current2<30:
    # 플레이어의 주사위 값
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
     
    # 각 플레이어의 현재 위치에 주사위 값을 더함
    current1 += dice1
    current2 += dice2
    
    print(player1, '은(는)', dice1, '가 나왔습니다. 현재위치', current1)
    print(player2, '은(는)', dice2, '가 나왔습니다. 현재위치', current2)

    if current1>=30 and current2<30:    # 1 플레이어만 30 이후의 위치에 도달한 경우
        print(round, '라운드만에', player1, '이(가) 이겼습니다.')
        break
    elif current1<30 and current2>=30:    # 2 플레이어만 30 이후의 위치에 도달한 경우
        print(round, '라운드만에', player2, '이(가) 이겼습니다.')
        break
    elif current1>=30 and current2>=30:    # 두 플레이어가 동시에 30 이후의 위치에 도달한 경우
        print(round, '라운드만에 무승부로 게임이 종료되었습니다.')
        break

    # 게임이 종료되지 않은 경우 현재 라운드에 1을 더하고 반복문 다시 실행
    round += 1