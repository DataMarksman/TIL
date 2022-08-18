# 
import sys
sys.stdin = open("input_sudoku.txt", "r")

T = int(input())
for case_num in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ans = 1
    for dx in range(9):
        list_ver = []
        list_col = []
        list_box = []
        for dy in range(9):
            list_ver += [board[dx][dy]]
            list_col += [board[dy][dx]]
            list_box += [board[(dy//3)+3*(dx//3)][(dy%3)+3*(dx%3)]]
        else:
            ver = sorted(list_ver)
            col = sorted(list_col)
            box = sorted(list_box)
            if ver == num_list and col == num_list and box == num_list:
                pass
            else:
                ans = 0
                break
        
    print(f'#{case_num} {ans}')
