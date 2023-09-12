# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

dx = [2, 0, -2, 0]
dy = [0, -2, 0, 2]

N, K = map(int, input().split())
dababa_set = set()
visited = set()
for case in range(K):
    x, y = map(int, input().split())
    dababa_set.add((x, y))
work_set = set(dababa_set)
while work_set:
    x, y = work_set.pop()
    for direction in range(4):
        px = x + dx[direction]
        py = y + dy[direction]
        if (px, py) not in dababa_set and 1 <= px <= N and 1 <= py <= N:
            visited.add((px, py))
print(len(visited))