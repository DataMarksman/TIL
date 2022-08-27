# 1210. ladder 2
# 설계: 그냥 가.
# 1. 근데 재귀는 못 쓸 것 같아.
# 2. 조타 설정할 때, 자기 있는 곳을 가장 마지막에 보도록 설정해서 for문 하나로 조건 다 주고 싶음
dx = [1, 0, 0]
dy = [0, 1, -1]


T = 10
for tc in range(1, T + 1):
    case_num = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    start_point = []
    for start_check in range(100):
        if board[0][start_check] == 1:
            start_point.append(start_check)
    min_n = 99999
    ans = 100

    while start_point:
        direction = 0
        n = 0
        start_num = start_point.pop(0)
        current_idx = (0, start_num)

        while current_idx[0] < 99:
            if direction == 0:
                for check in range(3):
                    px = current_idx[0] + dx[(check+1)%3]
                    py = current_idx[1] + dy[(check+1)%3]
                    if 0 < px <= 99 and 0 <= py <= 99:
                        if board[px][py] == 1:
                            direction = (check+1)%3
                            current_idx = (px, py)
                            break
            elif direction >= 1:
                for check in range(2):
                    px = current_idx[0] + dx[check*direction]
                    py = current_idx[1] + dy[check*direction]
                    if 0 < px <= 99 and 0 <= py <= 99:
                        if board[px][py] == 1:
                            direction = check*direction
                            current_idx = (px, py)
                            break
            n += 1

        if n <= min_n:
            min_n = n
            ans = start_num

    print(f'#{case_num} {ans}')
