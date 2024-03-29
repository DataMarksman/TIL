# PRG.
# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 설계 의도: 트리는 사실 루트 노드가 딱히 고정되어있지 않아도 된다.
# 위상 정렬 + 트리

# 로직의 Main 개념: 트리의 특성을 가지고 놀아보자.
# 트리의 루트를 마음대로 정하고 거기에서 리프 노드를 정해서 올라오면서 카운팅 해주자.
# 리프노드부터 루트 까지 올라오기 때문에 딱 한번만 살펴보면 각 노드에서 리프까지 몇개가 연결 되어있는지 한번에 알 수 있다.
# 이번 문제에서는 루트 노드를 무조건 1로 가정할 겁니당~ 이해를 돕기 위해서 이므로 굳이 이렇게 풀어야 할 필요는 없습니다.


# [Tip!] 위상정렬에 대해 알아보자!
# 단, 이 문제에서는 진입 차수가 1이면 진입하는 방식을 채용한다. (자신의 부모 노드가 살아있기 때문에 1이 기준이 된다.)
import sys
from collections import deque

def solution(n, wires):
    answer = sys.maxsize
    root_list = [[] for _ in range(n+1)]        # 각 idx 에 idx에 해당하는 노드와 연결된 노드들의 정보가 저장됩니다
    # ex) [[], [2, 3], ...] -> 0번 노드는 무시하고, 1번 노드에 2, 3번 노드가 연결되어있음을 의미합니다.
    # target_answer = n%2                       # 백트래킹을 위해 최적의 답을 먼저 배정해두는 것도 가능하다.
    root_entering = [0] * (n+1)                 # 각 노드의 진입차수를 의미합니다.
    root_count = [1]*(n+1)                      # 각 노드의 위를 잘랐을 때, 그 간선 아래로 남는 노드의 개수를 적어주는 리스트입니다.
                                                # 무조건 자기 자신은 남기 때문에 1을 기본값으로 줍니다.
    for [A, B] in wires:
        root_list[A].append(B)                  # 연결되어 있는 노드를 올려줍니다.
        root_list[B].append(A)                  # 연결되어 있는 노드를 올려줍니다.
        root_entering[A] += 1                   # 진입 차수 += 1
        root_entering[B] += 1                   # 진입 차수 += 1

    pick_Q = deque()                            # 진입 차수가 1 이면 넣을 Q 입니다.
    for reap_check in range(2, n+1):            # 1을 루트노드로 가정합니다. 1은 거르고 2부터 확인해서 리프 노드에서 제외시켜줍니다.
        if root_entering[reap_check] == 1:      # 진입 차수가 1인 리프노드들을 우선적으로 넣어줍니다.
            pick_Q.append(reap_check)

    while pick_Q:                               # 올려 놓은 위치 값을 하나씩 뽑아 옵니다.
        pick = pick_Q.popleft()                 # 가장 왼쪽, 즉 가장 먼저 넣은 노드부터 빼줍니다.
        for rooting in root_list[pick]:         # 해당 노드에 연결되어있는 노드들을 하나씩 순회합니다.
            root_count[rooting] += root_count[pick]
            root_list[rooting].remove(pick)     # 이미 밟은 자식 노드는 부모 노드의 자식 리스트에서 제외해줍니다.
            root_entering[rooting] -= 1         # 부모 노드의 진입 차수를 1 줄여줍니다.

            if root_entering[rooting] == 1:     # 진입차수가 1이라면 pick_Q 에 넣어줍니다.
                pick_Q.append(rooting)
                # if root_count[rooting] == target_answer: # 최적의 해를 발견하면 먼저 return 하는 백트래킹용 코드다.
                #     return target_answer

    for answer_check in range(1, n+1):          # 각 서브 루트 노드에 연결되어있는 노드들의 개수들을 순회하면서 최적의 값을 경신해준다.
        answer = min(abs(n - (root_count[answer_check]*2)), answer)
    return answer
# print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))