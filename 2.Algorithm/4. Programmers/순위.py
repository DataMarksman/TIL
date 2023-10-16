# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

from collections import deque


def solution(n, results):
    topo_stack = [0] * (n + 1)
    win_stack = [1] * (n + 1)
    visited = set()
    win_list = [[] for _ in range(n+1)]
    leaf_set = {i for i in range(1, n + 1)}
    for winner, looser in results:
        topo_stack[winner] += 1
        leaf_set.discard(winner)
        win_list[looser].append(winner)
    topo_queue = deque(leaf_set)
    while topo_queue:
        pick = topo_queue.popleft()
        for win in win_list[pick]:
            win_stack[win] += win_stack[pick]
            topo_stack[win] -= 1
            if topo_stack[win] == 0:
                topo_queue.append(win)
    answer = 0
    for winning in win_stack[1:]:
        if winning not in visited:
            visited.add(winning)
        else:
            answer += 1

    return answer