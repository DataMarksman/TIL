# BOJ. 4485 녹색 옷 입은 애가 젤다지
# 설계 의도: 조건에 맞는 실행
# 개선점: 다익스트라 구현
# 1.
import sys
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


N = int(sys.stdin.readline())
case_num = 1
while N != 0:
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    INF = 140626
    value_list = [INF] * (N**2)
    value_list[0] = board[0][0]
    visited = set()
    current_value = 0
    flag = True
    while flag:
        pick = value_list.index(min(value_list))
        x = pick // N
        y = pick % N
        current_value = value_list[pick]
        value_list[pick] = INF
        visited.add(pick)
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if px == N-1 and py == N-1:
                value_list[px * N + py] = board[px][py] + current_value
                flag = False
                break
            elif 0 <= px < N and 0 <= py < N and (N*px + py) not in visited:
                if board[px][py] + current_value < value_list[px*N + py]:
                    value_list[px * N + py] = board[px][py] + current_value
    print(f'Problem {case_num}: {value_list[N*N - 1]}')
    N = int(sys.stdin.readline())
    case_num += 1