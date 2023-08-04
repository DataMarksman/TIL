# BOJ.
# 설계 의도: 각 간선별로 뻗어나가는 경우의 수를 전부 고려하자.
# 1. 다익스트라는 최선의 경우만 탐색한다. 그러므로 이러한 최선의 수를 먼저 고려한다.
# 2. 최선의 경우의 수 외의 모든 경우의 수도 Queue에 저장해놓고 먼저 밟았던 최선의 수와 비교한다
# 3. 이전 정점까지의 거리가 최선의 수로 진행한 정점까지의 거리보다 짧으면 최적의 이동 경로이다.
# 3.1. 마찬가지로 이전 정점에서 지금 정점까지의 가중치 또한 최선의 수로 진행한 정점까지의 거리보다 짧아야 한다.
# 4. 이렇게 끝 점까지 가서 목표값 2을 만날 수 있으면 통과.
# 개선점:
import sys
import heapq
INF = sys.maxsize
N, M = map(int, input().split())
connection = [[] for _ in range(N+1)]
value_list = [INF]*(N+1)
value_list[2] = 0
for put_in in range(M):
    A, B, C = map(int, input().split())
    connection[A] += [(C, B)]
    connection[B] += [(C, A)]
H_queue = []
heapq.heappush(H_queue, (0, 2))
ans = 0

for rearrange in range(1, N+1):
    connection[rearrange].sort()
# print('first setting')
# print(connection)
# print(value_list)
# print('======start======')
while H_queue:
    dist, idx = heapq.heappop(H_queue)
    # print('ans:', ans)
    # print('idx:', idx, dist)
    if idx == 1:
        ans += 1
    else:
        for searching in range(len(connection[idx])):
            pick = connection[idx][searching][1]
            plus = connection[idx][searching][0]
            # print(' pick: ', pick, plus)
            if value_list[pick] > dist + plus:
                value_list[pick] = dist + plus
            if dist <= value_list[pick]:
                heapq.heappush(H_queue, (dist + plus, pick))
    # print('Queue:', H_queue)
    # print('value: ', value_list)
    # print('============')
print(ans)