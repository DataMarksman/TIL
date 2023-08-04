# BOJ.1005
# 설계 의도: 위상 정렬 구현
# 문제 요구 사항:
# 1. 특정 건물을 짓기 위해서는 다른 건물의 건설 여부를 요구할 수 있다.
# 2. 각 건물마다 필요한 타 건물과 건설에 필요한 시간이 다르다.
# 3. 우리가 구하고 싶은 것은 "특정 건물"의 건설을 위해 필요한 최소 시간 이다.



# 개선점:
# import sys
# # sys.setrecursionlimit(10**6)
# input = lambda: sys.stdin.readline().rstrip('\r\n')
#
# # 입력 케이스 개수
# T = int(input())
#
# for case_cnt in range(T):
#     # 건물의 개수 : N, 건물 건설 규칙 개수 : K
#     N, K = map(int, input().split())
#
#     # 각 건물의 건설에 걸리는 시간 리스트
#     time_list = list(map(int, input().split()))
#
#     # index 0은 무시하고 1부터 순서대로 건물 번호를 받아서 자식 노드를 저장할 리스트
#     order_list = [[] for _ in range(N+1)]
#
#     # 마찬가지로 index 0은 무시하고 각 노드에 포함된 자식의 개수를 저장할 리스트
#     child_cnt_list = [0]*(N+1)
#
#     # 공사 순서 K개를 차례로 받아서 start_point가 지어져야 end_point가 지어짐을 나타내준다.
#     for working_order in range(K):
#         # start_point의 index에 해당하는 노드가 지어져있어야 end_point의 index에 해당하는 건물을 지을 수 있다.
#         start_point, end_point = map(int, input().split())
#         # 각 노드에 해당하는 건물을 짓기 위해서 필요한 필수 건물들을 리스트에 넣는다.
#         order_list[end_point].append(start_point)
#         # 각 건물을 짓기 위해 필요한 건물의 개수를 카운팅 한다.
#         child_cnt_list[end_point] += 1
#
#     # 우리가 지어야 할 목표 건물의 index이다.
#     target = int(input())
#
#
#     orderQ = {target, }
#     visited = dict()
#     while orderQ:
#         pick_order = orderQ.pop()
#         if pick_order not in visited.keys():
#             visited[str(pick_order)] = 1
#             orderQ
#         else:
#             visited[str(pick_order)] += 1


import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip('\r\n')
# 입력 케이스 개수
T = int(input())

for case_cnt in range(T):
    # 건물의 개수 : N, 건물 건설 규칙 개수 : K
    N, K = map(int, input().split())

    # 각 건물의 건설에 걸리는 시간 리스트
    time_list = [0] + list(map(int, input().split()))

    # index 0은 무시하고 1부터 순서대로 건물 번호를 받아서 자식 노드를 저장할 리스트
    order_list = [[] for _ in range(N+1)]
    reverse_list = [[] for _ in range(N+1)]

    # 진입 차수 저장 리스트
    in_degrees_list = [0]*(N+1)

    # 공사 순서 K개를 차례로 받아서 start_point가 지어져야 end_point가 지어짐을 나타내준다.
    for working_order in range(K):
        # start_point의 index에 해당하는 노드가 지어져있어야 end_point의 index에 해당하는 건물을 지을 수 있다.
        start_point, end_point = map(int, input().split())
        # 각 노드에 해당하는 건물을 짓기 위해서 필요한 필수 건물들을 리스트에 넣는다.
        order_list[start_point].append(end_point)
        reverse_list[end_point].append(start_point)
        # 각 건물을 짓기 위해 필요한 건물의 개수를 카운팅 한다.
        in_degrees_list[end_point] += 1

    # 우리가 지어야 할 목표 건물의 index이다.
    target = int(input())

    # 각 건물까지의 최소 건설 시간을 저장할 리스트
    min_time = time_list[:]

    queue = deque()
    # 진입 차수가 0인 건물을 큐에 추가
    visited = {target, }
    order_q = {target, }
    while order_q:
        pick = order_q.pop()
        if not reverse_list[pick]:
            queue.append(pick)
        else:
            order_set = set(reverse_list[pick])
            order_q |= order_set - visited
            visited |= order_set

    # 큐가 빌 때까지 반복
    while queue:
        node = queue.popleft()

        # 현재 건물의 자식 노드들을 탐색하며 최소 건설 시간 갱신
        for child_node in order_list[node]:
            in_degrees_list[child_node] -= 1
            min_time[child_node] = max(min_time[child_node], min_time[node] + time_list[child_node])

            # 진입 차수가 0이 되면 큐에 추가
            if in_degrees_list[child_node] == 0:
                if child_node == target:
                    queue = []
                    break
                else:
                    queue.append(child_node)
    # 위상 정렬을 통해 최소 건설 시간 계산
    print(min_time[target])

