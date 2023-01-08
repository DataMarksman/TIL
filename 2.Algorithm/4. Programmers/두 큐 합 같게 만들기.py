# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:
import sys
from collections import deque


def solution(queue1, queue2):
    length = len(queue1)+len(queue2)
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    sum_all = sum_1 + sum_2
    if sum_all % 2 == 1:
        return -1
    elif sum_1 == sum_2:
        return 0
    Q1 = deque(queue1)
    Q2 = deque(queue2)
    temp_ans = 0
    while sum_1 != sum_2 and temp_ans <= length*2:
        temp_ans += 1
        if sum_1 > sum_2:
            pick = Q1.popleft()
            sum_1 -= pick
            sum_2 += pick
            Q2.append(pick)
        else:
            pick = Q2.popleft()
            sum_2 -= pick
            sum_1 += pick
            Q1.append(pick)

    if temp_ans >= length*2:
        answer = -1
    else:
        answer = temp_ans
    return answer