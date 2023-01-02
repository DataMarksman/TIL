# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def sum_bi(k):
    if k == 0:
        return 1
    elif k == 1:
        return 3
    elif k == 2:
        return 8
    result = sum_bi(k-1)*2 + 2**(k-1)
    return result


def count_bi(depth, idx):
    result = count_bi(depth-1, idx)

    return


N, M = map(int, input().split())
idx_N = -1
idx_M = -1
idx = 0
while idx_N < 0 or idx_M < 0:
    if 2**idx > N and idx_N < 0:
        idx_N = idx - 1
    if 2**idx > M and idx_M < 0:
        idx_M = idx - 1







