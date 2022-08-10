# 6808. 규영이와 인영이의 카드게임

# 조건 정리
# 한쪽이 이기기 위해서는 86점 이상 취득하는 것이 목표
# 총점이 171점이기 때문에 비기는 경우도 없다.

# 여기서 조금 더 효율화 하기 위한 아이디어로
# 필요 승수 개념을 더해보자.
# 만약 9번의 게임 중 인영이의 승리 횟수가 2회라면, 아무리 크게 이겨도 게임은 진다.
# 16 17 18 19 -> 66점, 86점보다 20점 부족
# 반대로 인영이의 승리 횟수가 7,8회 혹은 9회라면 필승이다.
# 그렇다면 인영이의 승리 횟수가 3,4,5,6 번인 케이스만 추출하고
# 그중에 점수가 86점 이상인 것들만 모아보면 된다.


T = int(input())1
for i in range(1,T+1):
    board = [0]*19
    enemy_cards = list(map(int,input().split()))
    my_cards = []
    for enemy_card in enemy_cards:
        board[enemy_card] = 1
    for mycard in range(len(board)):
        if board[mycard] == 0 and mycard != 0:
            my_cards += [mycard]
    print(my_cards)
    
    