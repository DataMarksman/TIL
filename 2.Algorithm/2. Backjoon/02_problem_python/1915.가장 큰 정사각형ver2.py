# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
max_size = 0
N, M = map(int, input().split())
if M == 1:
    for check in range(N):
        if int(input()) == 1:
            max_size = 1
    print(max_size)
elif N == 1:
    board = set(map(int, input().rstrip()))
    if 1 in board:
        print(1)
    else:
        print(0)
else:
    board = [list(map(int, input().rstrip())) for i in range(N)]
    for first_y in range(M):
        if board[0][first_y]:
            max_size = 1
    for first_x in range(1, N):
        if board[first_x][0]:
            max_size = 1
    for x in range(1, N):
        for y in range(1, M):
            if board[x][y]:
                board[x][y] = min(board[x - 1][y], board[x][y - 1], board[x - 1][y - 1]) + 1
                if board[x][y] > max_size:
                    max_size = int(board[x][y])
    print(max_size**2)


"""
4 4
0100
0111
1111
0011


4 4
0100
0111
1111
1110


4 4
1111
0111
1110
0010


4 4
0000
0000
0000
0000

4 4
1010
0101
1010
0101



"""