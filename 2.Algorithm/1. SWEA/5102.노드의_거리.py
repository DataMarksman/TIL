# SWEA.5102 노드의 거리
# 설계 목적:
# 1. 그냥 평범한 BFS
# 개선점:
# 1. 양방향성인지 단방향인지 꼭 ! 확인하자.... 단방향인줄알고 맞왜틀 하고 있었음

T = int(input())
for case_num in range(1, T+1):
    V, E = tuple(map(int, input().split()))
    board = [[0]*(V+1) for _ in range(V+1)]
    for write_in in range(E):
        A, B = tuple(map(int, input().split()))
        board[A][B] = 1
        board[B][A] = 1
    S, G = tuple(map(int, input().split()))
    n_queue = [S]
    visited = set()
    count = 0
    ans = 0
    while n_queue:
        count += 1
        size = len(n_queue)
        for pick in range(size):
            C = n_queue.pop(0)
            if board[C][G] == 1:
                ans = count
                n_queue.clear()
                break
            else:
                for searching in range(1, V+1):
                    if board[C][searching] == 1 and searching not in visited:
                        visited.add(searching)
                        n_queue.append(searching)
    print(f'#{case_num} {ans}')


