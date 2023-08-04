# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip('\r\n')

answer = sys.maxsize
dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

def recur_fire(K, x, y):
    global answer
    if K >= answer:
        return

    if y >= 10:
        x += 1
        y = 0
        if x >= 10:
            if sum(board[8]) + sum(board[9]) == 0:
                answer = min(K, answer)
                return
            else:
                return
        elif x >= 2:
            if sum(board[x-2]) > 0:
                return
    elif x >= 1 and y >= 1:
        if board[x-1][y-1]:
            return
    if x == 0 or board[x-1][y] == 0:
        recur_fire(K, x, y+1)
    if x == 0 or board[x-1][y]:
        for direction in range(5):
            px = x + dx[direction]
            py = y + dy[direction]
            if 0 <= px < 10 and 0 <= py < 10:
                board[px][py] = (board[px][py] + 1)%2
        recur_fire(K+1, x, y+1)
        for direction in range(5):
            px = x + dx[direction]
            py = y + dy[direction]
            if 0 <= px < 10 and 0 <= py < 10:
                board[px][py] = (board[px][py] + 1)%2


board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
for get_info in range(10):
    line = input()
    for check in range(10):
        if line[check] == "O":
            board[get_info][check] = 1

recur_fire(0, 0, 0)
if answer == sys.maxsize:
    answer = -1
print(answer)

"""
O########O
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
O########O

100
"""