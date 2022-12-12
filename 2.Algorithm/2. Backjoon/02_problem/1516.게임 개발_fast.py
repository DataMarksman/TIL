# BOJ. 1516. 게임 개발
# 설계 의도: DFS 기반의 위상 정렬
# 1. 재귀 함수를 통해, 위상 정렬을 해나가면서 값을 들고 갑니다
# 2. 현재 값과 이미 넣어놓은 값을 비교해서 더 큰 쪽으로 통합 시킵니다.
# 3. 하나가 끝까지 가면, 다시 처음 뽑았던 루트 노드 들 중에 하나 뽑아서 끝까지 진행
# 개선점:
# 1. 자, 이건 DFS 입니다. 재귀입니다. 값 가져갈 때, 갱신 시키는건
#     ans_list 뿐만 아니라 들고 가는 값도 갱신 시켜야 합니다.
import sys
input = sys.stdin.readline
import heapq


v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]
time = [0]
# 방향 그래프의 모든 간선 정보를 입력 받기
for order in range(1, v+1):
    order_list = list(map(int, input().split()))
    time.append(order_list[0])
    for ordering in range(1, len(order_list)-1):
        graph[order_list[order]].append(order_list[ordering]) # 정점 A에서 B로 이동 가능
        indegree[order_list[ordering]] += 1

# 위상 정렬 함수
def topology_sort():
    queue = [] # 연산 최적화를 위해 heapq 씁니다. deque 쓰셔도 됩니당

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            heapq.heappush(queue, i)

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 꺼내기
        now = heapq.heappop(queue)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            time[i] += time[now]
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                heapq.heappush(queue, i)

    # 만약 이렇게 뽑아온 친구들의 길이가 v 즉 정점의 개수와 일치하면 순서대로 출력

    for printing in range(1, v+1):
        print(time[printing])

topology_sort()

"""
4
1 -1
1 1 -1
1 1 -1
1 2 3 -1

3
5 -1
10 -1
5 1 2 -1

4
1 4 3 2 -1
2 4 -1
1 4 -1
1 -1

5
10 -1
20 1 -1
30 2 -1
40 3 5 -1
100 -1
== 10 30 60 140 100

4
20 -1
10 -1
1 1 2 -1
1000 1 2 3 -1
== 20 10 21 1021
"""
