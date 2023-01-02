# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline



r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]
R_length = 3
C_length = 3

