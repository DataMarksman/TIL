# 1220. magnetic
import sys
sys.stdin = open("input_magnetic.txt", "r")

dx = [0, 1, -1]


T = 10
for case_num in range(1, T+1):
    M = int(input())
    board = [[0]*102]
    magnetic_list = []
    count = 0
    for put_in in range(100):
        data = [0] + list(map(int, input().split())) + [0]
        for info in range(100):
            if data[info] == 1:
                magnetic_list += [[put_in+1, info+1, 1]]
                count += 1
            elif data[info] == 2:
                magnetic_list += [[put_in+1, info+1, 2]]
                count += 1
        board += [data]
    else:
        board += [[0]*102]
    turn = 0
    while turn <= 100:
        for factors in magnetic_list:
            if factors[2] == 5 or factors[2] == 7:
                pass
            elif board[factors[0]+dx[factors[2]]][factors[1]] == 5:
                board[factors[0]][factors[1]] = 5
                factors[2] = 5
            elif board[factors[0]+dx[factors[2]]][factors[1]] == 2-((factors[2]-1)%2):
                board[factors[0]][factors[1]] = 5
                factors[2] = 5
            elif board[factors[0]+dx[factors[2]]][factors[1]] == factors[2]:
                pass
            elif board[factors[0]+dx[factors[2]]][factors[1]] == 0:
                board[factors[0]][factors[1]] = 0
                board[factors[0] + dx[factors[2]]][factors[1]] = factors[2]
                factors[0] += dx[factors[2]]
                if factors[0] < 0 or factors[0] > (M-1):
                    factors[0] = 10000
                    factors[2] = 7
                    count -= 1
        turn += 1

    print(f'#{case_num} {count}')

