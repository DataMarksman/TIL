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


# import sys
# import heapq
# input = sys.stdin.readline
#
#
# def kruskal(x, y):
#     global p
#     if x == y:
#         if p[x] != x:
#             p[x] = kruskal(p[x], p[x])
#         return p[x]
#     elif p[kruskal(y, y)] != kruskal(x, x):
#         p[kruskal(y, y)] = kruskal(x, x)
#         return True
#     else:
#         return False
#
#
# V, E = map(int, input().split())
# H_queue = []
# for edges in range(E):
#     A, B, C = map(int, input().split())
#     heapq.heappush(H_queue, (C, A, B))
# p = list(range(V + 1))
# answer = 0
# cnt = 0
# max_Z = 0
# for pick_up in range(E):
#     z, x, y = heapq.heappop(H_queue)
#
#     if x > y:
#         if kruskal(y, x):
#             answer += z
#             cnt += 1
#     elif y > x:
#         if kruskal(x, y):
#             answer += z
#             cnt += 1
#     if cnt == V-2:
#         break
# print(answer)


import sys
from heapq import *
input = sys.stdin.readline

V, E = map(int, input().split())
cost_dict = dict()
connected = [[] for _ in range(V+1)]
min_cost = 1001
min_root = (0, 0)

for edges in range(E):
    A, B, C = map(int, input().split())
    A, B = min(A,B), max(A,B)
    cost_dict[(A, B)] = C
    connected[A].append(B)
    connected[B].append(A)
    if C < min_cost:
        min_cost = C
        min_root = (A, B)

heapQ = []
x, y = min_root
visited = {x, }
cost_sum = 0
max_cost = 0
heappush(heapQ, (min_cost, y))
for next_idx in connected[x]:
    s_idx = min(x, next_idx)
    l_idx = max(x, next_idx)
    heappush(heapQ, (cost_dict[(s_idx, l_idx)], next_idx))
while len(visited) < V:
    cost, idx = heappop(heapQ)
    if idx not in visited:
        # print('visited:',visited)
        # print('idx:', idx, ' & cost:', cost)
        visited.add(idx)
        cost_sum += cost
        max_cost = max(max_cost, cost)

        for next_idx in connected[idx]:
            if next_idx not in visited:
                s_idx = min(idx, next_idx)
                l_idx = max(idx, next_idx)
                heappush(heapQ, (cost_dict[(s_idx, l_idx)], next_idx))

print(cost_sum - max_cost)