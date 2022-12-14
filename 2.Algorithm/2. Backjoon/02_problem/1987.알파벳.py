# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, visited):
    global ans
    visited = set(visited)

    if len(reader_board[x][y]) > len(visited) and visited in reader_board[x][y]:
        return
    else:
        if len(visited) > len(reader_board[x][y]):
            reader_board[x][y] = set(visited)
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if 0 <= px < N and 0 <= py < M:
                if board[px][py] not in visited:
                    dfs(px, py, visited | {board[px][py], })
        else:
            if len(visited) > ans:
                ans = len(visited)


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
reader_board = [[set()]*M for _ in range(N)]
ans = 0
dfs(0, 0, {board[0][0], })
print(ans)
