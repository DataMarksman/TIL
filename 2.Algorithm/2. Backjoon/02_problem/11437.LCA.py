# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
import math
input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.setrecursionlimit(10**6)  # 파이썬의 재귀 깊이 제한을 늘립니다.(1)

# 입력
V = int(input())  # 정점의 수 입력받기
graph = [[] for _ in range(V + 1)]  # 각 노드의 연결 상태를 나타내는 그래프 초기화(2)
for _ in range(V - 1):
    a, b = map(int, input().split())  # 간선 정보 입력받기(3)
    graph[a].append(b)
    graph[b].append(a)

# 필요한 변수 선언
depth = [-1] * (V + 1)  # 각 노드의 깊이를 저장할 리스트 초기화(4)
parent = [[-1] * (V + 1) for _ in range(int(math.log2(V) + 1))]  # 각 노드의 2^i번째 부모 노드를 저장할 리스트 초기화(5)

# DFS 함수
def dfs(v, d):
    depth[v] = d
    for w in graph[v]:
        if depth[w] == -1:
            parent[0][w] = v
            dfs(w, d + 1)

# 모든 노드에 대해 DFS를 수행한 후
dfs(1, 0)

# 2^i 번째 부모 노드 설정
for i in range(1, int(math.log2(V) + 1)):
    for v in range(1, V + 1):
        parent[i][v] = parent[i - 1][parent[i - 1][v]]

# LCA 함수
def lca(a, b):
    # 먼저 깊이가 더 깊은 노드를 a로 설정(9)
    if depth[a] < depth[b]:
        a, b = b, a
    # a와 b의 깊이를 같게 만듦(10)
    for i in range(int(math.log2(V)), -1, -1):
        if depth[a] - (1 << i) >= depth[b]:
            a = parent[i][a]
    # a와 b가 같다면(부모가 같다면) 반환(11)
    if a == b:
        return a
    # a와 b의 깊이를 동시에 올리며 LCA를 찾음(12)
    for i in range(int(math.log2(V)), -1, -1):
        if parent[i][a] != parent[i][b]:
            a = parent[i][a]
            b = parent[i][b]
    return parent[0][a]  # 부모가 같아진 지점 반환(13)

# 초기화 및 DFS 수행
depth[1] = 0  # 루트 노드의 깊이는 0(14)
dfs(1, 0)  # DFS 실행(15)

# LCA 계산
M = int(input())  # LCA를 구할 노드 쌍의 수 입력받기
for _ in range(M):
    a, b = map(int, input().split())  # LCA를 구할 두 노드 입력받기
    print(lca(a, b))  # LCA 출력
