# SWEA.5105 미로의 거리
# 설계 목적: BFS로 최단 거리 구하기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    board = []
    start = []
    for i in range(N):
        in_list = list(input())
        if '2' in in_list:
            start = [i, in_list.index('2')]
        board += [in_list]
    # print(board)
    # print(start)
    ans = 0
    count = 0
    queue = [start]
    visited = set()
    flag = False
    while queue:
        size = len(queue)
        for popping in range(size):
            if queue:
                A = queue.pop(0)
                for dirt in range(4):
                    px = A[0] + dx[dirt]
                    py = A[1] + dy[dirt]
                    # print(px, py, queue, visited)
                    if px < 0 or px >= N or py < 0 or py >= N:
                        continue
                    elif board[px][py] == '3':
                        ans = count
                        queue.clear()
                        break
                    elif board[px][py] == '0' and (px, py) not in visited:
                        queue.append((px, py))
                        visited.add((px, py))
        count += 1

    print(f'#{case_num} {ans}')

