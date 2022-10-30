# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def doTopologicalSort(graph, n):
    L = []
    S = deque([i for i in range(n)])
    while S:
        n = S.pop()
        L.append(n)
        for m in graph.adjList[n]:
            indegree[m] = indegree[m] - 1
            if indegree[m] == 0:
                S.append(m)
    for i in range(n):
        if indegree[i]:
            return None
    return L


if __name__ == '__main__':
    N, K = map(int, input().split())
    edges = [set() for _ in range(N+1)]
    for roots in range(K):
        A, B = map(int, input().split())
        edges[A].add(B)
    L = doTopologicalSort(graph, N)
    print(L)