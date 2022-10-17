# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# direction = 1,2,3,4
#

import sys
from copy import deepcopy
input = sys.stdin.readline


def play(direct, board):
    board = deepcopy(board)
    print('==============', direct, '로 시작===========')
    for printing in range(N):
        print(board[printing])

    if direct == 0:
        for X in range(N):
            top = 0
            value = 0
            for Y in range(N):
                if board[X][Y] != 0:
                    if board[X][Y] == value:
                        board[X][top] += value
                        board[X][Y] = 0
                        value = 0
                    else:
                        board[X][top] = int(board[X][Y])
                        value = int(board[X][Y])
                        if top != Y:
                            board[X][Y] = 0
                    top += 1
    elif direct == 1:
        for X in range(N):
            top = N-1
            value = 0
            for Y in range(N-1, -1, -1):
                if board[X][Y] != 0:
                    if board[X][Y] == value:
                        board[X][top] = value*2
                        board[X][Y] = 0
                        value = 0
                    else:
                        board[X][top] = int(board[X][Y])
                        value = int(board[X][Y])
                        if top != Y:
                            board[X][Y] = 0
                        top -= 1
    elif direct == 2:
        for X in range(N):
            top = 0
            value = 0
            for Y in range(N):
                if board[Y][X] != 0:
                    if board[Y][X] == value:
                        board[top][X] = value*2
                        board[Y][X] = 0
                        value = 0
                    else:
                        board[top][X] = int(board[Y][X])
                        value = int(board[Y][X])
                        if top != Y:
                            board[Y][X] = 0
                        top += 1
    elif direct == 3:
        for X in range(N):
            top = N-1
            value = 0
            for Y in range(N-1, -1, -1):
                if board[Y][X] != 0:
                    if board[Y][X] == value:
                        board[top][X] = value*2
                        board[Y][X] = 0
                        value = 0
                    else:
                        if not value:
                            board[top][X] = int(board[Y][X])
                            value = int(board[Y][X])
                            if top != Y:
                                board[Y][X] = 0
                            top -= 1
                        else:
                            if not value:
                                board[top][X] = int(board[Y][X])
                                value = int(board[Y][X])
                                if top != Y:
                                    board[Y][X] = 0

    print('==============', direct, '로 돌림===========')
    for printing in range(N):
        print(board[printing])
    return board


def searching(depth, platform):
    global ans
    re_board = deepcopy(platform)
    if depth == 5:
        max_value = 0
        for max_search in range(N):
            if max(re_board[max_search]) > max_value:
                max_value = max(re_board[max_search])
        if max_value > ans:
            ans = max_value
    else:
        for direction in range(4):
            searching(depth+1, play(direction, re_board))


N = int(input())
original = [list(map(int, input().split())) for _ in range(N)]
ans = 2
searching(0, original)
print(ans)

"""
5
2 0 0 0 0
2 0 0 0 0
4 0 0 0 0
2 0 0 0 0
2 0 0 0 0
"""