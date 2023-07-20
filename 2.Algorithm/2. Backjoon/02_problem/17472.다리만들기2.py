# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
island_list = []
visited = set()
ans = -1
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and (i, j) not in visited:
            board[i][j] = 0
            queue = {(i, j), }
            min_x = int(i)
            min_y = int(j)
            max_x = int(i)
            max_y = int(j)
            while queue:
                x, y = queue.pop()
                for direction in range(4):
                    px = x + dx[direction]
                    py = y + dy[direction]
                    if 0 <= px < N and 0 <= py < M and (px, py) not in visited and board[px][py] == 1:
                        visited.add((px, py))
                        queue.add(queue)
                        board[px][py] = 0
                        if px < min_x:
                            min_x = px
                        elif px > max_x:
                            max_x = px
                        if py < min_y:
                            min_y = py
                        elif py > max_y:
                            max_y = py
            island_list.append((min_x, min_y, max_x, max_y))

distance_heapq = []

for check_front in range(len(island_list)-1):
    A_left_X, A_left_Y, A_right_X, A_right_Y= island_list[check_front]
    for check_back in range(check_front+1, len(island_list)):
        B_left_X, B_left_Y, B_right_X, B_right_Y = island_list[check_back]

        if A_left_X < B_right_X:
            pass
        elif A_right_X > B_left_X:






