# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))

N = int(input())
for case_num in range(1,N+1):

    T = int(input())
    for case_num in range(1, T + 1):
