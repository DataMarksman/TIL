# BOJ. 2623. 음악프로그램
# 설계 의도: 문제집 문제와 같은 위상정렬 문제죠?
# 개선점:
# 1. 어예 1등이당 40ms!, 빠르게 루프 판단해서 던져주면 36ms 까지 노려봄직 할지도

import sys
input = sys.stdin.readline
import heapq


v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    order_list = list(map(int, input().split()))
    for ordering in range(1, len(order_list)-1):
        graph[order_list[ordering]].append(order_list[ordering+1]) # 정점 A에서 B로 이동 가능
        indegree[order_list[ordering+1]] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    queue = [] # 연산 최적화를 위해 heapq 씁니다. deque 쓰셔도 됩니당

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            heapq.heappush(queue, i)

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 꺼내기
        now = heapq.heappop(queue)
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                heapq.heappush(queue, i)

    # 만약 이렇게 뽑아온 친구들의 길이가 v 즉 정점의 개수와 일치하면 순서대로 출력
    if len(result) == v:
        for printing in range(v):
            print(result[printing])
    # 아니면 그냥 0 출력합니당
    else:
        print(0)

topology_sort()