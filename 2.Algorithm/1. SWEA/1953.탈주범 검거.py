# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
dx = [[0], [0, 0, 1, -1], [1, -1], [0, 0], [-1, 0], [1, 0], [0, 1], [1, 0]]
dy = [[0], [1, -1, 0, 0], [0, 0], [1, -1], [0, 1], [0, 1], [-1, 0], [0, -1]]


def searching(x, y, depth):
    global ans_set
    direct = board[x][y]
    depth = int(depth)
    if depth == time:
        ans_set.add((x, y))
    else:
        for ion in range(len(dx[direct])):
            px = x + dx[direct][ion]
            py = y + dy[direct][ion]
            if 0 <= px < height and 0 <= py < wide:
                searching(px, py, depth + 1)


T = int(input())
for case_num in range(1, T + 1):
    info = list(map(int, input().split()))
    height = info[0]
    wide = info[1]
    start = (info[2], info[3])
    time = info[4]
    board = [list(map(int, input().split())) for _ in range(height)]
    ans_set = set()
    searching(start[0], start[1], 1)
    print(f'#{case_num} {len(ans_set)}')