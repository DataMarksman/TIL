# BOJ. 1202. 보석 도둑
# 설계 의도: logN 짜리 그리디 알고리즘을 만들어보자.
# 개선점: 음... Bag 을 관리하는 것도 heap Q로 했더니 오히려  속도가 내려갔습니다.
# 구조적으로는 이득이니까 일단 이대로 놔두겠습니다.
import sys
import heapq
input = lambda: sys.stdin.readline().rstrip('\r\n')

N, K = map(int, (input().split()))
J_heap_Q = []
bag_list = []
answer = 0
# 보석을 받으면서 무게단위로 오름차순 정렬 해봅시다.
for jewelry in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(J_heap_Q, (weight, -value))
# 가방 값도 받으면서 heapQ에 넣어줍니다.
for bags in range(K):
    heapq.heappush(bag_list, int(input()))
# 각 가방이 뽑을 수 있는 최선의 값을 저장해둘 겁니다.
heap_value_Q = []

for _ in range(K):
    # 가방을 오름차순으로 정렬하고 heapQ로 빼다보니 작은것부터 빠집니다.
    bag = heapq.heappop(bag_list)
    # 이번 가방이 넣을 수 있는 Maximum까지 보석을 죄다 뺍니다.
    while J_heap_Q and J_heap_Q[0][0] <= bag:
        heapq.heappush(heap_value_Q, heapq.heappop(J_heap_Q)[1])
    # 그리고 가방에 넣을 수 있는 것들 중에서 가장 비싼 걸 뽑아서 갑니다.
    if heap_value_Q:
        answer -= heapq.heappop(heap_value_Q)
print(answer)
