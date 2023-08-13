# # BOJ.
# # 설계 의도: 조건에 맞는 실행
# # 개선점:
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

T = int(input())
for testcase in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    if sum(num_list) > 0:
        print("YES")
    else:
        minus_cnt = 0
        plus_queue = []
        calculate_flag = False
        current_numb = 0
        while num_list:
            aim = num_list.pop()
            if calculate_flag:
                if aim > 0:
                    if plus_queue:
                        if plus_queue[-1] + current_numb > 0:
                            plus_queue[-1] += current_numb
                            plus_queue.append(aim)
                        elif aim + current_numb > 0:
                            plus_queue.append(aim + current_numb)
                        else:
                            minus_cnt += 1
                            plus_queue.append(aim)
                    else:
                        if aim + current_numb > 0:
                            plus_queue.append(aim + current_numb)
                        else:
                            minus_cnt += 1
                            plus_queue.append(aim)
                    current_numb = 0
                    calculate_flag = False
                elif plus_queue and plus_queue[-1] + current_numb > 0:
                    plus_queue[-1] += current_numb
                    current_numb = 0
                    calculate_flag = False
                else:
                    current_numb += aim

            else:
                if aim > 0:
                    plus_queue.append(aim)
                elif aim == 0:
                    continue
                else:
                    current_numb = aim
                    calculate_flag = True
        if current_numb != 0:
            if plus_queue and plus_queue[-1] + current_numb > 0:
                pass
            else:
                minus_cnt += 1
        if len(plus_queue) - minus_cnt > 0:
            print("YES")
        else:
            print("NO")


#
# def solution(sequence):
#     n = len(sequence)
#
#     if sum(sequence) > 0:
#         return True
#
#     for i in range(n):
#         if sequence[i] < 0:
#             left_sum = sum(sequence[:i])
#             right_sum = sum(sequence[i+1:])
#             if left_sum > 0 or right_sum > 0:
#                 return True
#     return False
#
#
# T = int(input())
# for testcase in range(T):
#     N = int(input())
#     print("YES" if solution(list(map(int, input().split()))) else "NO")
