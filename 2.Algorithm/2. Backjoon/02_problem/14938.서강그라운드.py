# BOJ. 14938 서강그라운드
# 설계 의도: DFS로 탐색
# 개선점:
# 1. 깡 DFS라서 시간이 간당간당 합니당
def collecting(idx, dist):
    global visited
    if dist <= M:
        visited.add(idx)
        for checking in range(1, N + 1):
            if distance[idx][checking] > 0:
                if dist + distance[idx][checking] <= M:
                    collecting(checking, dist + distance[idx][checking])


import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
value_list = [0] + list(map(int, input().split()))
distance = [[0] * (N+1) for _ in range(N+1)]
ans = 0

for put_in in range(R):
    A, B, C = map(int, input().split())
    distance[A][B] = C
    distance[B][A] = C

for searching in range(1, N+1):
    visited = set()
    temp_ans = 0
    collecting(searching, 0)
    while visited:
        pick = visited.pop()
        temp_ans += value_list[pick]
    if ans < temp_ans:
        ans = temp_ans
print(ans)
