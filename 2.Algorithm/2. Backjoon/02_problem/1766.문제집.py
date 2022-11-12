# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


class Graph:
    indegree = None
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        self.indegree = [0] * n
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.indegree[dest] = self.indegree[dest] + 1


def doTopologicalSort(graph, n):
    L = []
    indegree = graph.indegree
    S = deque([i for i in range(n)])
    while S:
        n = S.pop()
        L.append(n+1)
        for m in graph.adjList[n]:
            indegree[m] = indegree[m] - 1
            if indegree[m] == 0:
                S.append(m)
    for i in range(n):
        if indegree[i]:
            return None
    return L


N, K = map(int, input().split())
# edges = [set() for _ in range(N+1)]
# for roots in range(K):
#     A, B = map(int, input().split())
#     edges[A].add(B)
edges = []
for roots in range(K):
    A, B = map(int, input().split())
    edges.append((B-1, A-1))

graph = Graph(edges, N)
L = doTopologicalSort(graph, N)
print(*L[::-1][:N])