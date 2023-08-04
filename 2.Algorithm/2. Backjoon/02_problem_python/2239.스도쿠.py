# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
from copy import deepcopy as dp
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def godoku(start_x, start_y, row_pick, col_pick, box_pick, re_board, k):
    global flag
    global ans
    if flag:
        return
    else:
        row_pick = dp(row_pick)
        col_pick = dp(col_pick)
        box_pick = dp(box_pick)
        re_board = dp(re_board)
        y = start_y
        x = start_x
        while x <= 8 and y <= 8:
            if board[x][y] == '0':
                for checking in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    if checking not in row_pick[x] and checking not in col_pick[y] \
                            and checking not in box_pick[(y//3)+(x//3)*3]:
                        row_pick[x].add(checking)
                        col_pick[y].add(checking)
                        box_pick[(y // 3) + (x // 3) * 3].add(checking)
                        re_board[x][y] = checking
                        if k == 1:
                            ans = re_board
                            flag = True
                            return
                        else:
                            px = x
                            py = y + 1 if y < 8 else 0
                            if not py:
                                px += 1
                            if 0 <= px <= 8 and 0 <= py <= 8:
                                godoku(px, py, row_pick, col_pick, box_pick, re_board, k-1)
                            else:
                                return
                            row_pick[x].remove(checking)
                            col_pick[y].remove(checking)
                            box_pick[(y // 3) + (x // 3) * 3].remove(checking)
                return
            else:
                if y < 8:
                    y += 1
                else:
                    y = 0
                    x += 1


row_set = [set() for _ in range(9)]
col_set = [set() for _ in range(9)]
box_set = [set() for _ in range(9)]
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
if remain == 0:
    ans = board
else:
    godoku(0, 0, row_set, col_set, box_set, board, int(remain))
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





