# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

T = int(input())
for case_num in range(1, T + 1):
    N, M_O = tuple(map(int, input().split()))
    M = M_O - 1
    board = [list(map(int, input().split())) for _ in range(N)]
    sum_set = set()
    for x in range(N):
        for y in range(N):
            vc_sum = int(board[x][y])
            cr_sum = int(board[x][y])
            for vc_check in range(4):
                px = int(x)
                py = int(y)
                for repeat in range(M):
                    px += dx[vc_check]
                    py += dy[vc_check]
                    if 0 <= px < N and 0 <= py < N:
                        vc_sum += board[px][py]

            for cr_check in range(4, 8):
                cx = int(x)
                cy = int(y)
                for repeat_c in range(M):
                    cx += dx[cr_check]
                    cy += dy[cr_check]
                    if 0 <= cx < N and 0 <= cy < N:
                        cr_sum += board[cx][cy]
            sum_set.add(vc_sum)
            sum_set.add(cr_sum)
    print(f'#{case_num} {max(sum_set)}')
