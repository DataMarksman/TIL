# BOJ. 2636 치즈
# 설계 의도: 조건에 맞는 실행
# 1. 이미 패딩이 되어있는 2차원 배열이다!
# 2. 그러니까, 0,0 에서 시작해서 0으로 된 곳을 싹다 visited에 넣고,
# 3. 가장 바깥에서 0과 마주하고 있는 1, 즉 치즈들만 cheese_set()과 visited에 넣고 0으로 바꿔준다.
#    -> 이 때, visited에 넣는 이유는, 같은 루틴 내에서 다시 밟지 않으려고!
# 4. 이렇게 해당 루틴에서 cheese에 넣은 좌표들은 재귀를 통해 다음 searching 목록이 된다.
# 5. 재귀를 다시 시작하면, searching 에서 시작해서 다시 위와 같은 행위를 반복하면, 치즈를 둘러싸고 있는 한장만 벗긴다.
# 6. 마지막 시행을 하면, 남은 치즈가 없게 된다. 즉, 재귀 처음에 len(searching)으로 빼놓은 값이 마지막에 없어진 치즈의 수다.
# 개선점:
# 72ms 까지 줄였는데, 더 줄일 수 있을 것 같다. set()은 위대하다.

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def melting(searching, visited, time):
    global board
    global ans_time
    global ans_cheese
    remain = len(searching)
    cheese = set()
    while searching:
        point = searching.pop()
        x = point[0]
        y = point[1]
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if 0 <= px < N and 0 <= py < M:
                if board[px][py] == 0 and (px, py) not in visited:
                    searching.add((px, py))
                    visited.add((px, py))
                elif board[px][py] == 1:
                    cheese.add((px, py))
                    visited.add((px, py))
                    board[px][py] = 0
    if cheese:
        melting(cheese, visited, time + 1)
    else:
        ans_time = time
        ans_cheese = remain


N, M = tuple(map(int, input().split()))
board = []
for lines in range(N):
    line = list(map(int, input().split()))
    board += [line]
start_set = set()
start_set.add((0, 0))
ans_time = 0
ans_cheese = 0
melting(start_set, set(), 0)
print(ans_time)
print(ans_cheese)
