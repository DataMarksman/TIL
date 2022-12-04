# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
DP = [[0]*N for _ in range(N)]
DP[0][0] = 1
for first in range(1, N):
    if board[0][first] == (board[0][first-1] + 1)%3:
        DP[0][]
for i in range(1, N):
    for j in range(N):
        if j == 0:



