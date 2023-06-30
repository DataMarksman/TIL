# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

import sys


def solution(board):
    answer = sys.maxsize
    width = len(board[0])
    height = len(board)
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    wall_set = set()
    start_point = (0, 0)
    goal_point = (0, 0)

    for y in range(height):
        for x in range(width):
            if board[y][x] == "D":
                wall_set.add((y, x))
            elif board[y][x] == "R":
                start_point = (y, x)
            elif board[y][x] == "G":
                goal_point = (y, x)

    def recur_find_root(depth, y, x, visited):
        nonlocal answer

        if depth >= answer:
            return
        elif (y, x) == goal_point:
            answer = min(depth, answer)
            return
        visited = set(visited)
        visited.add((y, x))

        for direction in range(4):
            py = int(y)
            px = int(x)
            while 0 <= py < height and 0 <= px < width:
                py += dy[direction]
                px += dx[direction]

                if (py, px) == goal_point:
                    answer = min(depth, answer)
                    break

                elif (py, px) in wall_set:
                    py -= dy[direction]
                    px -= dx[direction]
                    if (py, px) not in visited and 0 <= py < height and 0 <= px < width:
                        recur_find_root(depth + 1, py, px, visited | {(py, px), })
                    else:
                        break

                elif 0 > py or py >= height or 0 > px or px >= width:
                    py -= dy[direction]
                    px -= dx[direction]
                    if (py, px) not in visited and 0 <= py < height and 0 <= px < width:
                        recur_find_root(depth + 1, py, px, visited | {(py, px), })
                    else:
                        break
    recur_find_root(1, start_point[0], start_point[1], {start_point, })
    if answer == sys.maxsize:
        answer = -1
    return answer


board_1 = ["...D..R",
           ".D.G...",
           "....D.D",
           "D....D.",
           "..D...."]
board_2 = [".D.R",
           "....",
           ".G..",
           "...D"]
print(solution(board_1))
print(solution(board_2))
