# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def re_cur(start, visited, idx, stock):
    global ans
    visited = set(visited)
    if len(visited) == N:
        if board[idx][start] > 0:
            if ans > stock + board[idx][start]:
                ans = stock + board[idx][start]
    else:
        for checking in range(N):
            if board[idx][checking] > 0 and checking not in visited:
                if stock + board[idx][checking] < ans:
                    re_cur(start, visited | {checking, }, checking, stock + board[idx][checking])


N = int(input())
ans = 99999999999999999
board = [list(map(int, input().split())) for _ in range(N)]
for re_cursion in range(N):
    re_cur(re_cursion, {re_cursion, }, re_cursion, 0)
print(ans)
