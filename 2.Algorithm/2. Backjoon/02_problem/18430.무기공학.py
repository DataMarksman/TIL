# BOJ. 18430. 무기공학
# 설계 의도: 그냥 백트래킹 없이 브루트 포스로 돌려도 가능은 한데요?
# 개선점:
# 1. DP 가능하지 않을까???? 근데 이렇게 돌려도 python3 기준 4등이네엽
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def brute(start_x, start_y, visited, point):
    global ans
    visited = set(visited)
    if point > ans:
        ans = point
    stop_count = 0
    for x in range(start_x, N):
        if x != start_x:
            start_y = 0
        for y in range(start_y, M):
            if (x, y) not in visited:
                px = x + 1
                mx = x - 1
                py = y + 1
                my = y - 1
                if px < N and py < M and (px, y) not in visited and (x, py) not in visited:
                    brute(x, y, visited | {(x, y), (px, y), (x, py)}, point + 2*board[x][y] + board[px][y] + board[x][py])
                if px < N and 0 <= my and (px, y) not in visited and (x, my) not in visited :
                    brute(x, y, visited | {(x, y), (px, y), (x, my)}, point + 2*board[x][y] + board[px][y] + board[x][my])
                if 0 <= mx and py < M and (mx, y) not in visited and (x, py) not in visited:
                    brute(x, y, visited | {(x, y), (mx, y), (x, py)}, point + 2*board[x][y] + board[mx][y] + board[x][py])
                if 0 <= mx and 0 <= my and (mx, y) not in visited and (x, my) not in visited:
                    brute(x, y, visited | {(x, y), (mx, y), (x, my)}, point + 2*board[x][y] + board[mx][y] + board[x][my])



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
if min(N, M) == 1:
    print(0)
else:
    ans = 0
    brute(0, 0, set(), 0)
    print(ans)




