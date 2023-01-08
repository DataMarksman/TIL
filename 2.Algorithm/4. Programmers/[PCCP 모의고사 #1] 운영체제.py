# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

# 이 문제는 운영체제의 동기, 비동기를 직접 경험해보는 문제 입니다.
# 이 문제에서는 하나의 작업이 끝날 때 까지 다른 작업이 Bloacking 되어있다가
# 진행 중인 작업이 끝나야 다음 작업으로 건너가므로 동기 형식의 작업 임을 알 수 있습니다.
import sys
input = sys.stdin.readline
import heapq


def solution(program):
    answer = [0] * 11
    # 자료의 구성은 (점수, 호출 시각, 실행 시간) 순으로 구성된다.
    # [Tip!] lambda로 정렬하는 방식도 있다는데요?
    # program.sort(key=lambda x: (x[1], x[0]))
    # 이처럼 lambda 의 가상 변수를 활용하여 정렬하는 방식도 사용 가능하다.

    Q = []
    for get_heap in range(len(program)):
        # 이러한 자료를 다시 (호출 시각, 점수, 실행 시간) 순으로 바꿔서 heapQ 로 올려준다.
        heapq.heappush(Q, (program[get_heap][1], program[get_heap][0], program[get_heap][2]))

    # 작업 Q 입니다. 실제로 운영체제를 배울 때, 작업 Q라는 개념을 배우게 되는데,
    # 프로세서가 다음에 처리할 업무를 올려놓는 Q를 의미합니다.
    # 대기열에는 전체 업무들이 전부 들어가 있고, 이것들이 명령에 따라 하나씩 작업 Q로 올라와서 순차적으로 실행됩니다.
    taskQ = []

    # 경과 시간을 저장해놓을 time 변수입니다.
    time = 0

    # 작업 Q로 불러올 후보군들이 남아있거나 작업Q 에 친구들이 남아있으면 계속 반복합니다.
    while Q or taskQ:

        # 현재 작업 Q에 아무것도 없을때, 즉 바로 해야할 일이 없다면?
        if not taskQ:
            # 그냥 바로 대기열에서 다음 업무를 뽑아오고
            pick = heapq.heappop(Q)
            # 배치될 시간과 현재 시간 중에서 더 큰 쪽으로 현재 시간을 맞춰줍니다.
            time = max(pick[0], time)
            # 그리고 대기열에서 뽑아온 업무를 작업 Q에 올려줍니다.
            heapq.heappush(taskQ, (pick[1], pick[0], pick[2]))

        # 대기열 Q에 있는 가장 앞의 친구가 현재 시간에서 뽑아올 수 있는 친구라면,
        while Q and Q[0][0] <= time:
            # 하나를 뽑아옵니다. 만약 그 다음 것도 뽑아올 수 있다면, While 문의 조건에 맞아서 계속 뽑아올 것입니다.
            # 이는 이전에 이미 시간이 충분히 흘러서, 대기열 Q에서 작업 Q로 일들을 많이 불러와야할 경우에 유용한 코드 입니다.
            pick = heapq.heappop(Q)
            heapq.heappush(taskQ, (pick[1], pick[0], pick[2]))

        # 메인 로직입니다.
        # 작업 Q에서 업무를 하나 뽑아옵니다.
        heap_pop = heapq.heappop(taskQ)
        # 우선순위 레벨에 따라서 대기 시간(현재 시간 - 일을 시작할 수 있었던 시간)을 누적합 시켜줍니다.
        answer[heap_pop[0]] += time - heap_pop[1]
        # 현재 시간에, 작업 Q에서 뽑아온 업무를 하기 위한 작업 시간을 더해줍니다.
        time += heap_pop[2]
    # 각 레벨에 따른 대기 시간 리스트의 가장 앞에 현재 시간을 넣어주고 return 해줍니다.
    answer[0] = time
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