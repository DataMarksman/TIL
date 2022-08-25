# SWEA.5097 회전
# 설계 목적: 스택이나 큐, 돌릴 줄 알아요? 물어보는 문제.
"""
# 1. pop(0)
T = int(input())
for case_num in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    count = 0
    while count < M:
        count += 1
        A = num_list.pop(0)
        num_list.append(A)
    print(f'#{case_num} {num_list[0]}')
"""
# 2. deque
from collections import deque

T = int(input())
for case_num in range(1, T+1):
    N, M = map(int, input().split())
    num_queue = deque(list(map(int, input().split())))
    num_queue.rotate(M)
    print(f'#{case_num} {list(num_queue)}')
