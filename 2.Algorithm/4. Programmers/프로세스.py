# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

from collections import deque


def solution(priorities, location):
    priority_cnt = [0] * 10
    priority_queue = deque()
    answer = 0
    for check in range(len(priorities)):
        priority_cnt[priorities[check]] += 1
        priority_queue.append((priorities[check], check))

    while True:
        prioritiy, idx = priority_queue.popleft()
        if sum(priority_cnt[prioritiy+1:]) > 0:
            priority_queue.append((prioritiy, idx))
        else:
            answer += 1
            priority_cnt[prioritiy] -= 1
            if idx == location:
                break

    return answer