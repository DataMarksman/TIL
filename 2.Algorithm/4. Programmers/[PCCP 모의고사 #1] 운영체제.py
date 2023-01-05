# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

import sys
input = sys.stdin.readline
import heapq


def solution(program):
    answer = [0] * 11
    # 자료의 구성은 (점수, 호출 시각, 실행 시간) 순으로 구성된다.
    # program.sort(key=lambda x: (x[1], x[0]))

    Q = []
    for get_heap in range(len(program)):
        # 이러한 자료를 다시 (호출 시각, 점수, 실행 시간) 순으로 바꿔서 heapQ 로 올려준다.
        heapq.heappush(Q, (program[get_heap][1], program[get_heap][0], program[get_heap][2]))

    taskQ = []
    time = 0
    while Q or taskQ:
        if not taskQ:
            pick = heapq.heappop(Q)
            time = max(pick[0], time)
            heapq.heappush(taskQ, (pick[1], pick[0], pick[2]))

        while Q and Q[0][0] <= time:
            pick = heapq.heappop(Q)
            heapq.heappush(taskQ, (pick[1], pick[0], pick[2]))
        heap_pop = heapq.heappop(taskQ)
        answer[heap_pop[0]] += time - heap_pop[1]
        time += heap_pop[2]
    return answer


program = [[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]
print(solution(program))
"""
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
"""