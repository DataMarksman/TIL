# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline


height, wide, M = map(int, input().split())


for sharks in range(M):


num_list = list(map(int, input().split()))


