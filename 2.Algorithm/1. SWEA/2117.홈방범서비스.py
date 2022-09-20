# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T + 1):
    N, K = map(int, input().split())
    houses = 0
    board = []
    for _ in range(N):
        lines = list(map(int, input().split()))
        houses += sum(lines)
        board += [lines]
    ans = 0
    flag = True
    distance = 2 * N - 1
    while flag:
        if houses * K < distance**2 + (distance-1)**2:
            distance -= 1
        else:
            for





        distance -= 1








    print(f'#{case_num} {ans}')