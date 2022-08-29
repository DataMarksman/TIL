# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    station = [0] * 1001

    for in_put in range(N):
        bus = list(map(int, input().split()))
        if bus[0] == 1:
            for check_n in range(bus[1], bus[2]+1):
                station[check_n] += 1
        elif bus[0] == 2:
            control_h = 0
            if bus[1] % 2 == 1:
                control_h = 1
            for check_h in range(bus[1], bus[2]+1):
                if check_h % 2 == control_h:
                    station[check_h] += 1
                elif check_h == bus[2]:
                    station[check_h] += 1
        elif bus[0] == 3:
            flag_h = True
            if bus[1] % 2 != 0:
                flag_h = False
            for check_jh in range(bus[1]+1, bus[2]):
                if flag_h and check_jh % 4 == 0:
                    station[check_jh] += 1
                elif not flag_h and check_jh % 3 == 0 and check_jh % 10 != 0:
                    station[check_jh] += 1
                elif check_jh == bus[1] or check_jh == bus[2]:
                    station[check_jh] += 1

    print(f'#{case_num} {max(station)}')