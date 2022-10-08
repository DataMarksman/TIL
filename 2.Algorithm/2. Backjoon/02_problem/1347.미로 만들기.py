# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

N = int(input())
arr = list(input())

d = 0
s = 50
e = 50
miro = [['#']*100 for _ in range(100)]
visited = []

miro[s][e] = '.'
visited.append((s, e))
for i in range(N):
    if arr[i] == 'R':
        d = (d+1) % 4
    elif arr[i] == 'L':
        d = (d+3) % 4

    elif arr[i] == 'F':
        miro[s+dr[d]][e+dc[d]] = '.'
        s = s+dr[d]
        e = e+dc[d]
        visited.append((s, e))

# print(miro)
# print(visited)

min_r = 100
max_r = 0
min_c = 100
max_c = 0

for i in range(len(visited)):
    if min_r >= visited[i][0]:
        min_r = visited[i][0]

    if max_r <= visited[i][0]:
        max_r = visited[i][0]

    if min_c >= visited[i][1]:
        min_c = visited[i][1]

    if max_c <= visited[i][1]:
        max_c = visited[i][1]

for i in range(min_r, max_r+1):
    print(''.join(miro[i][min_c: max_c+1]))