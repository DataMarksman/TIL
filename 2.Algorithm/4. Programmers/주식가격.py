# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

from heapq import *

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    time_queue = []
    pre_price = 0
    for pick in enumerate(prices):
        idx, price = pick
        if price < pre_price:
            while time_queue[0][0] < price:
                former_price, former_idx = heappop(time_queue)
                answer[former_idx] = idx - former_price
        heappush(time_queue,(price, idx))
        pre_price = price
    while len(time_queue) >= 1:
        former_price, former_idx = heappop(time_queue)
        answer[former_idx] = len(prices) - 1 - former_price

    return answer