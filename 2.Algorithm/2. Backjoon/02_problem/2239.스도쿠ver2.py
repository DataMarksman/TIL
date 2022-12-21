# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def sudoku(start_x, start_y):
    global flag
    global board
    if flag:
        return
    else:
        for X in range(start_x, 9):
            for Y in range(start_y, 9):
                if board[X][Y] == '0':
                    pick_list = sorted(original_set - row_set[X] - col_set[Y] - box_set[(numbers//3)+(get_numbers//3)*3])
                    print(X, Y)
                    print(pick_list)
                    if pick_list:
                        for check in range(len(pick_list)):
                            board[X][Y] = pick_list[check]
                            row_set[X].add(pick_list[check])
                            col_set[Y].add(pick_list[check])
                            box_set[(Y // 3) + (X // 3) * 3].add(pick_list[check])
                            sudoku(X, Y)
                            if not flag:
                                board[X][Y] = '0'
                                row_set[X].discard(pick_list[check])
                                col_set[Y].discard(pick_list[check])
                                box_set[(Y // 3) + (X // 3) * 3].discard(pick_list[check])
                        else:
                            return
                    else:
                        return
            start_y = 0
        flag = True
        return


row_set = [set() for _ in range(9)]
col_set = [set() for _ in range(9)]
box_set = [set() for _ in range(9)]
original_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
board = [['0']*9 for _ in range(9)]
flag = False
for get_numbers in range(9):
    line = input()
    for numbers in range(9):
        if int(line[numbers]) > 0:
            row_set[get_numbers].add(line[numbers])
            col_set[numbers].add(line[numbers])
            box_set[(numbers//3)+(get_numbers//3)*3].add(line[numbers])
            board[get_numbers][numbers] = line[numbers]
print(box_set)
sudoku(0, 0)
for printing in range(9):
    print(''.join(board[printing]))


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


103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107
"""





