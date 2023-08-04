# 강환석
# 설계 의도: 다익스트라 구현
# 1. 기존 다익스트라에 좌표 데이터만 가지고 인덱싱 컨트롤.
# 2. 성능 최적화를 위해 가중치 누적값은 *100000 하고 x,y 값은 1차원 배열화 시켜서 int 하나로 묶어줌
# 개선점:
# 1. 현재 속도: 168ms. 개선하려고 할 수록 느려진다. 초기 모델이 가장 빠름.
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
    heapq.heapify(my_pick)
    flag = True
    ans = 0
    while flag:
        pick = heapq.heappop(my_pick)
        x = (pick%100000) // N
        y = (pick%100000) % N
        current_value = pick//100000
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if px == N-1 and py == N-1:
                ans = board[px][py] + current_value
                flag = False
                break
            elif 0 <= px < N and 0 <= py < N and (N*px + py) not in visited:
                heapq.heappush(my_pick, (((board[px][py] + current_value) * 100000) + ((px * N) + py)))
                visited.add((px * N) + py)
    print(f'Problem {case_num}: {ans}')
    N = int(sys.stdin.readline())
    case_num += 1