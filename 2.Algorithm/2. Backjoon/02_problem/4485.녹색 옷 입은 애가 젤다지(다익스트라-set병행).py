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
    visited = set()
    min_set = set()
    flag = True
    pick = (board[0][0], 0)
    ans = 0
    if N == 1:
        ans = board[0][0]
        flag = False
    while flag:
        x = pick[1] // N
        y = pick[1] % N
        current_value = pick[0]
        visited.add(pick[1])
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if px == N-1 and py == N-1:
                ans = board[px][py] + current_value
                flag = False
                break
            elif 0 <= px < N and 0 <= py < N and (N*px + py) not in visited:
                min_set.add((board[px][py] + current_value, px * N + py))
        while pick[1] in visited and min_set:
            pick = min(min_set)
            min_set.discard(min(min_set))
    print(f'Problem {case_num}: {ans}')
    N = int(sys.stdin.readline())
    case_num += 1