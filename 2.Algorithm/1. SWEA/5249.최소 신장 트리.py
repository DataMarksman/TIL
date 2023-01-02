# SWEA 5249 최소신장트리 풀이
# 설계 목적: 크루스칼 재귀로 풀기
# 1. 재귀로 풀린다구요?
# 개선점:
# 1.
# 재귀 하나로 뭉쳐놓기
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


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])
    p = list(range(V+1))
    answer = 0
    cnt = 0
    print(edges)
    print(p)
    for x, y, w in edges:
        if kruskal(x, y):
            answer += w
            cnt += 1
            print(cnt, x, y, w, p)
        if cnt == V:
            break
    print(f'#{tc} {answer}')
