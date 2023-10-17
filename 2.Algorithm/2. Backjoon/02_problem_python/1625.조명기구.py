# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip('\r\n')
N, M = map(int, input().split())
INF = sys.maxsize
answer = INF
board = []
board_bulb_cnt = []
target = []
target_bulb_cnt = []
for i in range(N):
    board.append(list(map(int, input().split())))
    board_bulb_on = sum(board[i])
    board_bulb_cnt.append([board_bulb_on, M - board_bulb_on])
for i in range(N):
    target.append(list(map(int, input().split())))
    target_bulb_on = sum(target[i])
    target_bulb_cnt.append([target_bulb_on, M - target_bulb_on])

def light(idx, light_board, bulb_idx):
    for i in range(idx, N):
        if board_bulb_cnt[i][0] == target_bulb_cnt[i][0]:
            if board_bulb_cnt[i][0] == board_bulb_cnt[i][1]:
                light(i + 1, light_board, bulb_idx)
                arr = []
                for j in range(M):
                    if light_board[i][j] == 1:
                        arr.append(0)
                    else:
                        arr.append(1)
                light(i + 1, light_board, bulb_idx | {i+1, })
                return
        else:
            bulb_idx.add(i+1)
            for j in range(M):
                if light_board[i][j] == 1:
                    light_board[i][j] = 0
                else:
                    light_board[i][j] = 1
    spin_board = zip(*light_board[::-1])
    return change(0, spin_board, [i for i in range(M)], [], set(), set(), bulb_idx, len(bulb_idx))

def change(idx, spin_board, new_board, ones, twice, light_visited, steps):
    if steps >= answer:
        return

    for i in range(idx, M):
        idx = new_board[i]
        






""" input example
4 5
0 1 0 0 1
1 0 1 1 0
0 1 1 1 0
1 0 1 0 1
0 0 0 1 1
0 0 0 1 1
1 0 0 0 1
1 0 1 0 1

3
0 2
1 2 4
0 3
"""