# BOJ. 1197. MST 최소 스패닝 트리
# 설계 의도: 크루스칼 한방에 구현
# 개선점:
# 1. 역시 재귀함수 하나에 때려박으니 효율은 좋지 못하다.
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def kruskal(x, y):
    global p
    if x == y:
        if p[x] != x:
            p[x] = kruskal(p[x], p[x])  # path compression
        return p[x]
    elif p[kruskal(y, y)] != kruskal(x, x):
        p[kruskal(y, y)] = kruskal(x, x)
        return True
    else:
        return False


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])
p = list(range(V + 1))
answer = 0
cnt = 0
for x, y, w in edges:
    if kruskal(x, y):
        answer += w
        cnt += 1
    if cnt == V:
        break
print(answer)