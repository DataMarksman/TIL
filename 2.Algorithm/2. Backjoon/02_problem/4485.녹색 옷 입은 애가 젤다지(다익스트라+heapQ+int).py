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
    my_pick = [board[0][0]*100000, ]
    while True:
        pick = heapq.heappop(my_pick)
        x = (pick%100000) // N
        y = (pick%100000) % N
        current_value = pick//100000
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            idx = (px * N) + py
            if 0 <= px < N and 0 <= py < N and idx not in visited:
                heapq.heappush(my_pick, (((board[px][py] + current_value) * 100000) + idx))
                visited.add(idx)
        if (N**2)-1 in visited:
            print(f'Problem {case_num}: {board[N-1][N-1] + current_value}')
            break
    N = int(sys.stdin.readline())
    case_num += 1