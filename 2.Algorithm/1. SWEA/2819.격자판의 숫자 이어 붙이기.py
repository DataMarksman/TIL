# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def coloring(x, y, k, arr):
    global color_set
    if k >= 7:
        color_set.add(arr)
    else:
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if 0 <= px < 4 and 0 <= py < 4:
                new_str = arr + str(board[px][py])
                coloring(px, py, k+1, new_str)


T = int(input())
for case_num in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(4)]
    flag = True
    color_set = set()
    for r in range(4):
        for c in range(4):
            coloring(r, c, 0, str())
    print(f'#{case_num} {len(color_set)}')
