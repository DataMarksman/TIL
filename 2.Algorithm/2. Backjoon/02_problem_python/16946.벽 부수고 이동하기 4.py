# BOJ. 16946. 벽 부수고 이동하기 4
# 설계 의도: 2중 포문으로 돌면서 각 위치에서 할 수 있는 모든 행동을 하고 넘어가자. 딱 한번만 돈다.
# 1. 밟는 위치가 0, 즉 길이라면 거기에서 이어지는 모든 길을 매핑하고 visited에 넣는다.
#   1.1 이렇게 길을 넣는 과정에서 한번의 과정에서 쌓인 길의 좌표 값을 dict로 idx를 매핑해놓는다.
#   1.2 해당 idx를 활용하는 리스트에다가 이렇게 한번의 과정에서 쌓인 길의 넓이를 저장한다. 이후 한번에 불러온다.
# 2. 밟는 위치가 1, 즉 벽이라면 사방탐색으로 길의 구역과 이어지는지 체크한다.
#   2.1 이때, 같은 구역을 여러번 밟을 수도 있으므로, 불러오는 것은 구역의 idx 값이다.
#   2.2 사방 탐색이 끝나면 구역 번호를 넣은 set을 해체하여 value들을 더하여 print_board에 입력한다.
#   2.3 이때, 프린트 보드를 따로 만들지 않으면, %10 하여 0이 되는 벽을 진행중에 길로 인식하여 문제가 된다.
# 개선점:
# 1. 원래의 board에 바로 값을 바꿔주는 식으로 진행했는데, 이렇게 되면, 벽 아래 벽이 있고, 윗벽이 %10 == 0일 경우,
#   아래의 벽에서 1개를 더 세어버리는 문제가 발생한다. 그냥 print board 만들고 풀자.
import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]



N, M = map(int, sys.stdin.readline().strip().split())

board = [list(sys.stdin.readline().strip()) for _ in range(N)]
print_board = [['0']*M for _ in range(N)]
visited = set()
visited_dict = {}
value_list = []
for i in range(N):
    for j in range(M):
        if (i, j) in visited:
            continue
        elif board[i][j] == '0':
            visited_count = 1
            visited.add((i, j))
            stack = {(i, j), }
            visited_dict[(i, j)] = len(value_list)
            while stack:
                pick = stack.pop()
                X = pick[0]
                Y = pick[1]
                for direction in range(4):
                    PX = X + dx[direction]
                    PY = Y + dy[direction]
                    if 0 <= PX < N and 0 <= PY < M and (PX, PY) not in visited:
                        if board[PX][PY] == '0':
                            visited.add((PX, PY))
                            visited_dict[(PX, PY)] = len(value_list)
                            stack.add((PX, PY))
                            visited_count += 1
            value_list.append(visited_count)
        elif board[i][j] == '1':
            temp_value = 1
            temp_value_set = set()
            for direction in range(4):
                pi = i + dx[direction]
                pj = j + dy[direction]
                if 0 <= pi < N and 0 <= pj < M and board[pi][pj] == '0':
                    if (pi, pj) in visited:
                        temp_value_set.add(visited_dict[(pi, pj)])
                    else:
                        visited_count = 1
                        visited.add((pi, pj))
                        visited_dict[(pi, pj)] = len(value_list)
                        stack = {(pi, pj), }
                        while stack:
                            pick = stack.pop()
                            X = pick[0]
                            Y = pick[1]
                            for deep_direction in range(4):
                                PX = X + dx[deep_direction]
                                PY = Y + dy[deep_direction]
                                if 0 <= PX < N and 0 <= PY < M and (PX, PY) not in visited:
                                    if board[PX][PY] == '0':
                                        visited_dict[(PX, PY)] = len(value_list)
                                        visited.add((PX, PY))
                                        visited_count += 1
                                        stack.add((PX, PY))
                        value_list.append(visited_count)
                        temp_value_set.add(len(value_list) - 1)
            else:
                while temp_value_set:
                    sum_number = temp_value_set.pop()
                    temp_value += value_list[sum_number]
                print_board[i][j] = str(temp_value%10)


for printing in range(N):
    print("".join(print_board[printing]))