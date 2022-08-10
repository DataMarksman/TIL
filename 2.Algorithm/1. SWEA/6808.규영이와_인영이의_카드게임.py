# 6808. 규영이와 인영이의 카드게임

# 조건 정리
# 한쪽이 이기기 위해서는 86점 이상 취득하는 것이 목표
# 총점이 171점이기 때문에 비기는 경우도 없다.

T = int(input())
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