# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# import heapq
# input = sys.stdin.readline
#
#
# N, E = map(int, input().split())
# H_queue = []
# for edges in range(E):
#     A, B, C = map(int, input().split())
#     heapq.heappush(H_queue, (C, A, B))
#
# visited = set()
# ans = 0
# max_edge = 0
# while len(visited) < N:
#     value, X, Y = heapq.heappop(H_queue)
#     if X in visited and Y in visited:
#         pass
#     else:
#         visited.add(X)
#         visited.add(Y)
#         ans += value
#         if value > max_edge:
#             max_edge = int(value)
# print(ans - max_edge)


import sys
import heapq
input = sys.stdin.readline


def kruskal(x, y):
    global p
    if x == y:
        if p[x] != x:
            p[x] = kruskal(p[x], p[x])
        return p[x]
    elif p[kruskal(y, y)] != kruskal(x, x):
        p[kruskal(y, y)] = kruskal(x, x)
        return True
    else:
        return False


V, E = map(int, input().split())
H_queue = []
for edges in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(H_queue, (C, A, B))
p = list(range(V + 1))
answer = 0
cnt = 0
max_Z = 0
for pick_up in range(E):
    z, x, y = heapq.heappop(H_queue)

    if x > y:
        if kruskal(y, x):
            answer += z
            cnt += 1
    elif y > x:
        if kruskal(x, y):
            answer += z
            cnt += 1
    if cnt == V-2:
        break
print(answer)