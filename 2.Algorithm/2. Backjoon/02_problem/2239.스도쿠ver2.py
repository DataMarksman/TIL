# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
from copy import deepcopy as dp
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def sudoku(start_x, start_y, row_pick, col_pick, box_pick, re_board, k):
    global flag
    global board
    if flag:
        return
    else:
        x = start_x
        y = start_y
        if board[x][y] != 0:
            if y < 8:
                y += 1
            elif x < 8:
                y = 0
                x += 1
        else:


row_set = [set() for _ in range(9)]
col_set = [set() for _ in range(9)]
box_set = [set() for _ in range(9)]
compare_list = []
original_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
board = [['0']*9 for _ in range(9)]
flag = False
remain = 0
ans = []
for get_numbers in range(9):
    line = input()
    for numbers in range(9):
        if int(line[numbers]) > 0:
            row_set[get_numbers].add(line[numbers])
            col_set[numbers].add(line[numbers])
            box_set[(numbers//3)+(get_numbers//3)*3].add(line[numbers])
            board[get_numbers][numbers] = line[numbers]
        else:
            remain += 1
            compare_list.append((get_numbers, numbers))
if remain == 0:
    ans = board
else:
    sudoku(0, 0, [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)], board, 0)
for printing in range(9):
    print(''.join(ans[printing]))


"""

003000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000100


000000000
000000000
000000000
000000000
000000000
000000000
000000000
000000000
000000000

"""





