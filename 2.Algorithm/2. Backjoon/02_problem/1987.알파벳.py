# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]


def dfs(x, y, point):
    global ans
    global visited
    ans = max(point, ans)
    for direction in range(4):
        px = x + dx[direction]
        py = y + dy[direction]
        if 0 <= px < N and 0 <= py < M and visited[alp_dict[(px, py)]] == 0:
            visited[alp_dict[(px, py)]] = 1
            dfs(px, py, point + 1)
            visited[alp_dict[(px, py)]] = 0


N, M = map(int, input().split())
alp_dict = {}
for alp_x in range(N):
    line = list(input())
    for alp_y in range(M):
        alp_dict[(alp_x, alp_y)] = ord(line[alp_y])-65
visited = [0]*26
visited[alp_dict[(0, 0)]] = 1
ans = 0
dfs(0, 0, 1)
print(ans)
