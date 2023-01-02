import sys
sys.setrecursionlimit(10 ** 8)


def solution(edges, roots):
    N = len(edges)+1
    T = len(roots)
    idx_dict = {(0, 0): -1, }
    rooting = set()
    board = [[0] * (N + 1) for _ in range(N + 1)]
    answer = [0] * (N-1)
    for checking in range(N-1):
        A = edges[checking][0]
        B = edges[checking][1]
        board[A][B] = 1
        board[B][A] = 1
        idx_dict[(min(A, B), max(A, B))] = checking
        rooting.add((A, B))

    def find_root(pre_idx, idx):
        for finding in range(1, N+1):
            if board[idx][finding] == 1 and finding != pre_idx:
                if (finding, idx) in rooting:
                    rooting.discard((finding, idx))
                    rooting.add((idx, finding))
                    answer[idx_dict[(min(idx, finding), max(idx, finding))]] += 1
                find_root(idx, finding)
    find_root(0, 1)
    for turns in range(T):
        root_number = roots[turns]
        find_root(0, root_number)
    return answer


edges = [[1,3],[1,2],[2,4],[2,5]]
roots = [2,3]
print(solution(edges, roots))