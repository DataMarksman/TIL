# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
from heapq import *
input = lambda: sys.stdin.readline().rstrip('\r\n')



N = int(input())
T_P, T_Gr, T_Gd, T_Bd = map(int, input().split())
pump_heapq = []
for pump_idx in range(N):
    pump_list = list(map(int, input().split()))
    for get_heap in range(pump_list[0]):
         heappush(pump_heapq, (pump_list.pop(), pump_idx, False))
    long_list = list(map(int, input().split()))
    for get_long in range(pump_list[0]):
         heappush(pump_heapq, (pump_list.pop(), pump_idx, True))

step_heapq = []
for step_idx in range(N):
    step_list = list(map(int, input().split()))
    for steps in range(step_list[0]):
        start = step_list[steps*2 + 1]
        end = step_list[steps*2 + 2]
        heappush(step_heapq,(start, end, step_idx))

PERFECT = 0
GREAT = 0
GOOD = 0
BAD = 0
MISS = 0
MAX_COMBO = 0

