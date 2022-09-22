# SWEA. 5188. 최소합
# 설계 목적:
# 1. 그냥 씀

T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    for first_line in range(1, N):
        board[0][first_line] += board[0][first_line-1]
    for x in range(1, N):
        for y in range(N):
            B, C = 999999999, 999999999
            A = board[x][y]
            if 0 <= x - 1:
                B = board[x-1][y]
            if 0 <= y - 1:
                C = board[x][y-1]
            board[x][y] = A + min(B, C)
    print(f'#{case_num} {board[N-1][N-1]}')