# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
import heapq
input = lambda: sys.stdin.readline().rstrip('\r\n')

N = int(input())
X_Q = []
Y_Q = []
Z_Q = []
for planet in range(1,N+1):
    X, Y, Z = map(int, input().split())
    heapq.heappush(X_Q, (X, planet))
    heapq.heappush(Y_Q, (Y, planet))
    heapq.heappush(Z_Q, (Z, planet))

heap_Q = []
start_X, planet_X = heapq.heappop(X_Q)
while X_Q:
    next_X, next_planet_X = heapq.heappop(X_Q)
    heapq.heappush(heap_Q, (abs(start_X - next_X), planet_X, next_planet_X))
    start_X, planet_X = next_X, next_planet_X

start_Y, planet_Y = heapq.heappop(Y_Q)
while Y_Q:
    next_Y, next_planet_Y = heapq.heappop(Y_Q)
    heapq.heappush(heap_Q, (abs(start_Y - next_Y), planet_Y, next_planet_Y))
    start_Y, planet_Y = next_Y, next_planet_Y

start_Z, planet_Z = heapq.heappop(Z_Q)
while Z_Q:
    next_Z, next_planet_Z = heapq.heappop(Z_Q)
    heapq.heappush(heap_Q, (abs(start_Z - next_Z), planet_Z, next_planet_Z))
    start_Z, planet_Z = next_Z, next_planet_Z

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, edges):
    parent = list(range(n + 1))
    result = 0
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    return result

print(solution(len(heap_Q), heap_Q))