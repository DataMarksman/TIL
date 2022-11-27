# 문제 설계:
# 1. 그냥 탐색 문제구나...
import heapq
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dpboard = [[9999999]*N for _ in range(N)]

    Queue = [(0, 0, 0)]
    while Queue:
        pick = heapq.heappop(Queue)
        current = pick[0]
        x = pick[1]
        y = pick[2]
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if 0 <= px < N and 0 <= py < N:
                if board[x][y] > board[px][py]:
                    temp_value = int(current)
                    if dpboard[px][py] > temp_value:
                        dpboard[px][py] = temp_value
                        heapq.heappush(Queue, (temp_value, px, py))
                elif board[x][y] == board[px][py]:
                    temp_value = int(current) + 1
                    if dpboard[px][py] > temp_value:
                        dpboard[px][py] = temp_value
                        heapq.heappush(Queue, (temp_value, px, py))
                else:
                    temp_value = int(current) + ((board[px][py] - board[x][y]) * 2)
                    if dpboard[px][py] > temp_value:
                        dpboard[px][py] = temp_value
                        heapq.heappush(Queue, (temp_value, px, py))
    print(f"#{tc} {dpboard[N-1][N-1]}")

"""
5
4
9 5 7 9
8 4 2 5
7 6 5 4
8 8 9 5
6
1 1 1 1 1 1
9 9 9 9 9 1
9 9 1 1 1 1
9 9 1 9 9 9
9 9 1 9 9 9
9 9 1 1 1 1
"""