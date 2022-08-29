# 1. 전기자동차 충전소
# 설계 의도:
# 0.
# 1. 맨하탄 거리 기준으로 충전소를 설치함.
#    이 때 고려해야 할 부분은 최대 2개라는 점.
#   우선적으로 1개로 고려해야하므로, 첫루트는 1개 완전 탐색
# 2. 1개로 완전 탐색이 불가능할 경우,
#    set에 차이의 합을 저장하는 순열 조합으로 간다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def lining(core, visit, connected, line_sum):
    global sum_set
    global max_connect
    core = set(core)
    visit = set(visit)
    if core:
        core_a = core.pop()
        x = core_a[0]
        y = core_a[1]
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            flag = True
            while 0 <= px < N and 0 <= py < N:
                if board[px][py] == 0 and (px, py) not in visit:
                    px += dx[direction]
                    py += dy[direction]
                else:
                    flag = False
                    break
            if flag:
                px = x
                py = y
                tmp_visit = set(visit)
                tmp_count = 0
                while 0 <= px < N and 0 <= py < N:
                    tmp_count += 1
                    visit.add((px, py))
                    px += dx[direction]
                    py += dy[direction]
                line_sum += tmp_count
                lining(core, visit, connected + 1, line_sum)
                line_sum -= tmp_count
                visit = set(tmp_visit)
        else:
            lining(core, visit, connected, line_sum)
    else:
        print(connected, line_sum)
        if connected > max_connect:
            max_connect = int(connected)
            sum_set.clear()
            sum_set.add(int(line_sum))
        elif connected == max_connect:
            sum_set.add(int(line_sum))


T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    board = []
    core_set = set()
    visited = set()
    max_connect = 0
    sum_set = set()
    for put_in in range(N):
        line = list(map(int, input().split()))
        for check in range(N):
            if line[check] == 1:
                if check == 0 or check == N-1 or line == 0 or line == N-1:
                    line[check] = 2
                    visited.add((put_in, check))
                else:
                    core_set.add((put_in, check))
        board += [line]
    lining(core_set, visited, 0, 0)
    print(f'#{case_num} {min(sum_set)-max_connect}')







"""
1
7
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
"""

