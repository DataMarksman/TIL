# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    board = []
    location = set()
    count = 0
    for put_in in range(N):
        lines = list(map(int, input().split()))
        for write_in in range(N):
            if lines[write_in] == 1:
                if {put_in, write_in} & {0, N-1}:
                    lines[write_in] = 2
                else:
                    location.add((put_in, write_in))
    for
    while location:




    print(f'#{case_num} {ans}')