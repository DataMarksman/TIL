# BOJ. 1946. 신입사원

# < ver.1 >
# 설계 의도: heap Q로 정렬에서 이점을 가져가자.
# 1. heap Q로 뽑아쓰기. 끝
# 개선점:
# 1. 느리다. 5620ms.
# import sys
# import heapq
# input = sys.stdin.readline
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     candiate = []
#     ans = 1
#     for line_up in range(N):
#         line = tuple(map(int, input().split()))
#         heapq.heappush(candiate, line)
#     start = heapq.heappop(candiate)
#     max_A = int(start[1])
#     while candiate:
#         pick = heapq.heappop(candiate)
#         if pick[1] < max_A:
#             max_A = pick[1]
#             ans += 1
#     print(ans)

# < ver.2 >
# 설계 의도: 카운팅 소트로, 필기 시험 점수를 idx로 받고 거기에 실기 점수를 넣자.
# 1. 대신 넣을 때, N - 필기 등수로 넣어서 pop(0)가 아니라 pop()을 쓰도록 하자. 연산 효율화.
# 개선점:
# 1. 약간 빨라졌다. 2480ms. 2배 이상 속도 증가. 그래도 느리다. 3자리수로 끊어보고 싶다.
"""
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    candiate = [0]*N
    ans = 1
    for line_up in range(N):
        A, B = map(int, input().split())
        candiate[N-A] = B
    score = candiate.pop()
    while candiate:
        pick = candiate.pop()
        if pick < score:
            score = pick
            ans += 1
    print(ans)


"""

import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    candiate = [0]*N
    ans = 1
    for line_up in range(N):
        A, B = map(int, input().split())
        candiate[N-A] = B
    score = candiate.pop()
    for go in range(len(candiate)):
        pick = candiate.pop()
        if pick < score:
            score = pick
            ans += 1
    print(ans)
