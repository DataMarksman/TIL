# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]


def dfs(x, y, point):
    global ans
    ans = max(point, ans)
    for direction in range(4):
        px = x + dx[direction]
        py = y + dy[direction]
        if 0 <= px < N and 0 <= py < M and board[px][py] not in visited:
            visited.add(board[px][py])
            dfs(px, py, point + 1)
            visited.discard(board[px][py])


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = {board[0][0], }
ans = 0
dfs(0, 0, 1)
print(ans)
