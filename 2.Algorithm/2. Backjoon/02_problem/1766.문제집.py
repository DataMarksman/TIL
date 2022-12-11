# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N, K = map(int, input().split())
ans = []
nords = [set() for _ in range(N+1)]
nord_dict = {}
visited = set()
for get_edges in range(K):
    A, B = map(int, input().split())
    nords[B].add(A)
    nord_dict[A] = B

queue = []
for picking in range(1, N+1):
    if len(nords[picking]) == 0:
        visited.add(picking)
        queue.append(picking)
while len(visited) < N:
    temp_queue = []
    while queue:
        pick = queue.pop(0)
        ans.append(pick)
        next_pick = nord_dict[pick]
        nords[next_pick].discard(pick)
        if len(nords[next_pick]) == 0:
            temp_queue.append(next_pick)
    queue = sorted(temp_queue)
print(ans)
