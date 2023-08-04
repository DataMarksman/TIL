# BOJ. 20040 사이클 게임
# 설계 의도: 크루스칼에서 했던 유니온 그대로 가져왔슴다
# 개선점:
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = 0

# 부모 테이블 초기화
parent = [i for i in range(N)]


# find 연산
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


# union 연산
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for check in range(1, M+1):
    a, b = map(int, input().split())
    if ans == 0:
        if find_parent(a) == find_parent(b):
            ans = check
        else:
            union_parent(a, b)
    else:
        continue

print(ans)
