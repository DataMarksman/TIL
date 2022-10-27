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
num_list = [list(map(int, input().split())) for _ in range(N)]

