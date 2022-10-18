# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, K = map(int, input().split())
board = [list(map(int, input().split)) for _ in range(N)]
magic_Q = []
X, Y = (N+1)//2, (N+1)//2
while True:

