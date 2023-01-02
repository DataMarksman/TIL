# BOJ. 2176. 합리적인 이동경로
# 문제 이해:
# 요컨데, 여기에서 말하는 합리적인 이동경로는 순수한 거리 개념이 아니다.
# 위상의 개념이다.
# 각 정점을 차원별로 분류하여, 순서를 그렸을때,
# 그 위상의 계층 순서에서 역순으로 가지 않는 루트를 찾는 것이 목표다.
# 그렇기에, 순수한 거리 상으로는 돌아갈 수도 있고, 역주행 할수도 있다. 이걸 이해하면 문제는 바로 풀린다.
# 설계 의도: 일단 뒤부터 구현. ver2에서는 앞에서부터 구현 2Track으로 운용된다.
# < 1st track >
# 1. 이번 버전은 뒤에서 부터 온다. 뒤에서부터 각 정점들 까지의 최단거리를 도출
# 2. 힙큐로 먼저 빠지는 최단 거리들에 의해 2부터 각 정점들까지의 최단거리가 먼저 깔린다.
# 3. 이후로 후진입하는 idx들은 무조건 이전 것들보다 크다(다익스트라의 기본 가정)
# 4. 이렇게 먼저 판을 깔아놓으면서 동시에 2track인 DP를 가동시킨다.

# < 2nd track >
# 1. 일전에 깔아놓은 최단거리에서 각 점들 까지의 거리가 최단거리일 때만 큐에 넣었다. 이렇게 넣은 큐에서 뽑아온다.
# 2. 이렇게 구한 최단거리 정점에서 전체 탐색을 하면, 반드시 이전 점도 다시 걸린다. (간선에 방향성이 없으므로)
# 3. 이렇게 역탐색을 하면, 이전에 밟았던 정점의 value가 더 낮을 수 밖에 없으므로, 이전 간선의 dp값을 가져올 수 있다.
# 4. 물론 다른 최단거리에서 진행했던 또 다른 간선의 값도 마찬가지로 가져올 수 있다.
# 5. 이 때, 로직상 현재까지의 누적 value가 더 작은 쪽이 먼저 깔리므로, 나보다 더 상위에 있는 정점의 개수를 가져오는 것이다.
# 6. 나보다 낮은 위상은 아직 깔리지 않았으므로, 해당 정점에 가중치를 더해서 큐에 넣어준다.
#    (이 누적합이 최소값이 아니라면 알아서 걸러진다.)

# 개선점:
# 1. import sys 해서, sys.stdin.readline() 쓰고 안쓰고 차이가 6배 이상 난다....
import sys
import heapq
INF = sys.maxsize
N, M = map(int, sys.stdin.readline().split())
connection = [[] for _ in range(N+1)]
value_list = [0, INF, 0] + [INF]*(N-2)
for put_in in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    connection[A].append([C, B])
    connection[B].append([C, A])
H_queue = [(0, 2), ]
dp_list = [0, 0, 1] + [0]*(N-2)
while H_queue:
    now_value, now_idx = heapq.heappop(H_queue)
    if value_list[now_idx] >= now_value:
        for searching in range(len(connection[now_idx])):
            next_idx = connection[now_idx][searching][1]
            next_value = connection[now_idx][searching][0]
            if value_list[next_idx] > now_value + next_value:
                value_list[next_idx] = now_value + next_value
                heapq.heappush(H_queue, (now_value + next_value, next_idx))
            if now_value > value_list[next_idx]:
                dp_list[now_idx] += dp_list[next_idx]
print(dp_list[1])
