# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
sys.setrecursionlimit(10**4)
input = lambda: sys.stdin.readline().rstrip('\r\n')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y, point):
    global ans
    global visited
    ans = max(point, ans)
    for direction in range(4):
        px = x + dx[direction]
        py = y + dy[direction]
        if visited[alp_list[px][py]] == 0:
            visited[alp_list[px][py]] = 1
            dfs(px, py, point + 1)
            visited[alp_list[px][py]] = 0


N, M = map(int, input().split())
alp_list = [[26]*(M+2)]
for alp_x in range(N):
    line = list(input())
    for alp_y in range(M):
        line[alp_y] = ord(line[alp_y])-65
    alp_list += [[26] + line + [26]]
alp_list += [[26]*(M+2)]
visited = [0]*26 + [1]
visited[alp_list[1][1]] = 1
ans = 0
dfs(1, 1, 1)
print(ans)
