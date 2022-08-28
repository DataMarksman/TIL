# SWEA.
# 설계 목적: 자, 최소값을 찾기 위한 여정을 떠나보죠
# 1. 요컨데, 낚시터로 들어가는 발걸음을 최소화 하고 싶다는 건데, 1번
# 개선점:
# 1.

import sys
sys.stdin = open("sample_input.txt", "r")

dy = [-1, 1]

def positioning(gate_A, gate_B, gate_C, moving_sum, check_list):
    position = (gate_A[0]-1, gate_B[0]-1, gate_C[0]-1)
    waiting = (gate_A[1], gate_B[1], gate_C[1])
    flag = True
    fisher_queue = []
    while sum(waiting) > 0:
        if flag:
            for first_set in range(3):
                if waiting[first_set] >= 1:
                    check_list[position[first_set]] = 1
                    waiting[first_set] -= 1
                    moving_sum += 1
            else:
                flag = False
        elif waiting[1] > 0:
            gate_2_queue = [position[1]]
            while waiting[1] > 0:
                size = len(gate_2_queue)
                for batch in range(size):
                    second = gate_2_queue.pop(0)
                    for searching in range(2):
                        sec_y = second + dy[searching]
                        if 0 <= sec_y < N:
                            if waiting[1] > 0 and check_list[sec_y] == 0:
                                waiting[1] -= 1
                                check_list[sec_y] = 1
                                moving_sum += abs(sec_y - position[1])
                            elif waiting[1] > 0:
                                gate_2_queue.append(sec_y)
                            



        else:
            position_check = [0, 0, 0]








T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    board = [0]*N
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    sorted_list = sorted([A, B, C])
    A = sorted_list[0]
    B = sorted_list[1]
    C = sorted_list[2]
    print(A, B, C)
    min_walking = 99999999999999

    positioning(A, B, C, 0, [0]*N)
    while



    print(f'#{case_num} {ans}')