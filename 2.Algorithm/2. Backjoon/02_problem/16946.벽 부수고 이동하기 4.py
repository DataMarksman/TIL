# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]



N, M = map(int, sys.stdin.readline().strip().split())

board = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = set()
visited_list = []
value_list = []
for i in range(N):
    for j in range(M):
        if board[i][j] == '0' and (i, j) not in visited:
            temp_visited = {(i, j), }
            visited.add((i, j))
            stack = {(i, j), }
            while stack:
                pick = stack.pop()
                X = pick[0]
                Y = pick[1]
                for direction in range(4):
                    PX = X + dx[direction]
                    PY = Y + dy[direction]
                    if 0 <= PX < N and 0 <= PY < M and (PX, PY) not in visited:
                        if board[PX][PY] == '0':
                            temp_visited.add((PX, PY))
                            stack.add((PX, PY))
            visited_list.append(set(temp_visited))
            value_list.append(int(len(temp_visited)))

for x in range(N):
    for y in range(M):
        if board[x][y] == '1':
            value_set = set()
            for direction in range(4):
                px = x + dx[direction]
                py = y + dy[direction]
                if (px, py) in visited:
                    for checking in range(len(value_list)):
                        if (px, py) in visited_list[checking]:
                            value_set.add(checking)
            else:
                board_value = 1
                while value_set:
                    pick = value_set.pop()
                    board_value += value_list[pick]
                board[x][y] = str(board_value%10)
for printing in range(N):
    print("".join(board[printing]))



