# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]



N, M = map(int, sys.stdin.readline().strip().split())

board = [list(sys.stdin.readline().strip()) for _ in range(N)]
value_board = [[0]*M for _ in range(N)]
visited = set()


for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            temp_visited = {(i, j), }
            stack = {(i, j), }
            while stack:
                pick = stack.pop()
                X = pick[0]
                Y = pick[1]
                for direction in range(4):
                    PX = X + dx[direction]
                    PY = Y + dy[direction]
                    if 0 <= PX < N and 0 <= PY < M and (PX, PY) not in visited:
                        if board[PX][PY] == 0:
                            temp_visited.add((PX, PY))
                            visited.add((PX, PY))
                            stack.add((PX, PY))
            Step_count = int(len(temp_visited))
            while temp_visited:
                pick_step = temp_visited.pop()
                R = pick_step[0]
                C = pick_step[1]
                value_board[R][C] = Step_count

for x in range(N):
    for y in range(M):
        if int(board[x][y]) > 0:
            temp_value = 1
            for direction in range(4):
                px = x + dx[direction]
                py = y + dy[direction]
                if (px, py) in visited:
                    temp_value += value_board[px][py]
            else:
                board[x][y] = str(int(temp_value//10))
print(value_board)
print(board)



