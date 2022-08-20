# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.
import sys
sys.stdin = open("input_1258.txt", "r")


def find_mat(col, vert):
    global board
    global count
    cut_x = 0
    cut_y = 0
    for r in range(vert, N):
        if (board[col][r] == 0) or (r == (N-1)):
            cut_y = r
            break
    for c in range(col, N):
        if (board[c][vert] == 0) or (c == (N-1)):
            cut_x = c
            break
    for x in range(col, cut_x):
        for y in range(vert, cut_y):
            board[x][y] = 0

    ans = cut_x-col, cut_y-vert
    count += 1
    return ans


T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    wide_list = []
    for dx in range(N):
        for dy in range(N):
            if board[dx][dy] != 0:
                wide_list += [find_mat(dx, dy)]
    ans = sorted(wide_list, key=lambda x: (-(x[0]*x[1]), -x[0], -x[1]))
    print(f'#{case_num} {count}', *ans)

