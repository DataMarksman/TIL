# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

N, L = tuple(map(int, input().split()))
o_list = [list(map(int, input().split())) for _ in range(N)]
r_list = list(map(list, zip(*o_list)))
ans = 0

for x in range(N):
    flag_A = True
    flag_B = True
    for y in range(N):




