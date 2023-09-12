# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
# sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip('\r\n')
N, M = map(int, input().split())
delay, penalty = map(int, input().split())
left_position = int(N)
possible_number = 10
for case in range(M):
    TF, number = map(int, input().split())
    if TF:
        left_position -= 1
    possible_number -= 1
