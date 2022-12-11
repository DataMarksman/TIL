# BOJ. 18430. 무기공학
# 설계 의도: 조건에 맞는 실행
# 개선점:
# 1. DP 가능하지 않을까????
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def brute(start_x, start_y, visited, point):
    visited = set(visited)
    for x in range(start_x, N):
        if x != start_x:
            start_y = 0
        for y in range(start_y, M):
            if (x, y) not in visited:
                px = x + 1
                mx = x - 1
                py = y + 1
                my = y - 1
                if



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
if min(N, M) == 1:
    print(0)
else:




