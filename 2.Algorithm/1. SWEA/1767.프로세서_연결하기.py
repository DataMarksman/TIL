# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.
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
                if check == 0 or check == N-1 or put_in == 0 or put_in == N-1:
                    line[check] = 2
                    visited.add((put_in, check))
                else:
                    core_set.add((put_in, check))
        board += [line]
    lining(core_set, visited, 0, 0)
    print(f'#{case_num} {min(sum_set)-max_connect}')
