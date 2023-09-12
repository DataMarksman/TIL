# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
from heapq import *
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())
study_queue = []
bj_queue = []
for case in range(N):
    study = input()
    if study[:7] == "boj.kr/":
        heappush(bj_queue, (int(study[7:]),study))
    else:
        heappush(study_queue, (len(study), study))
while study_queue:
    length, context = heappop(study_queue)
    print(context)
while bj_queue:
    number, context = heappop(bj_queue)
    print(context)