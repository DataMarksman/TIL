import sys
from copy import deepcopy as dp
sys.setrecursionlimit(10 ** 8)


def solution(edges, roots):
    N = len(edges)+1
    T = len(roots)
    idx_dict = {(0, 0): -1, }
    pre_rooting = [set() for _ in range(N + 1)]
    post_rooting = [set() for _ in range(N + 1)]
    board = [[0] * (N + 1) for _ in range(N + 1)]
    answer = [0] * (N-1)
    for checking in range(N-1):
        A = edges[checking][0]
        B = edges[checking][1]
        board[A][B] = 1
        board[B][A] = 1
        idx_dict[(min(A, B), max(A, B))] = checking

    def find_root(pre_idx, idx):
        for finding in range(1, N+1):
            if board[idx][finding] == 1 and finding != pre_idx:
                post_rooting[idx].add(finding)
                find_root(idx, finding)
    find_root(0, 1)
    for turns in range(T):
        root_number = roots[turns]
        find_root(0, root_number)
        for comparing in range(1, N + 1):
            while pre_rooting[comparing]:
                pick = pre_rooting[comparing].pop()
                if comparing in post_rooting[pick]:
                    answer[idx_dict[(min(comparing, pick), max(comparing, pick))]] += 1
        pre_rooting = dp(post_rooting)
        post_rooting = [set() for _ in range(N + 1)]
    return answer


edges = [[1,3],[1,2],[2,4],[2,5]]
roots = [2,3]
print(solution(edges, roots))