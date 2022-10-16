# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
import heapq
input = sys.stdin.readline


N, E = map(int, input().split())
H_queue = []
for edges in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(H_queue, (C, A, B))

visited = set()
ans = 0
max_edge = 0
while len(visited) < N:
    value, X, Y = heapq.heappop(H_queue)
    if X in visited and Y in visited:
        pass
    else:
        visited.add(X)
        visited.add(Y)
        ans += value
        if value > max_edge:
            max_edge = int(value)
print(ans - max_edge)