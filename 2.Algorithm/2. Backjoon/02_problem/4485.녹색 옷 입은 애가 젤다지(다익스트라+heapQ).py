# BOJ. 4485 녹색 옷 입은 애가 젤다지
# 설계 의도: 조건에 맞는 실행
# 개선점: 다익스트라 구현
# 1.
import sys
import heapq
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


N = int(sys.stdin.readline())
case_num = 1
while N != 0:
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = {0, }
    my_pick = [(board[0][0], 0), ]
    heapq.heapify(my_pick)
    flag = True
    while flag:
        pick = heapq.heappop(my_pick)
        x = pick[1] // N
        y = pick[1] % N
        current_value = pick[0]
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if 0 <= px < N and 0 <= py < N and (N*px + py) not in visited:
                heapq.heappush(my_pick, (board[px][py] + current_value, (px * N) + py))
                visited.add((px * N) + py)
            if (N**2)-1 in visited:
                print(f'Problem {case_num}: {board[N-1][N-1] + current_value}')
                flag = False
                break
    N = int(sys.stdin.readline())
    case_num += 1