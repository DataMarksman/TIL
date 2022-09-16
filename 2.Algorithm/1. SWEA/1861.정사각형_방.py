# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def rooting(x, y):
    global max_length
    global position
    count_A = 1
    x = int(x)
    y = int(y)
    while True:
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if 0 <= px < N and 0 <= py < N:
                if board[px][py] - board[x][y] == 1:
                    count_A += 1
                    x = int(px)
                    y = int(py)
                    break
        else:
            break
    return count_A


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0
    position = 999999999999999999
    for i in range(N):
        for j in range(N):
            result = rooting(i, j)
            if result > max_length:
                max_length = result
                position = board[i][j]
            elif result == max_length and board[i][j] < position:
                position = board[i][j]

    print(f'#{case_num} {position} {max_length}')