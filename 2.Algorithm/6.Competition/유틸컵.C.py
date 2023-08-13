# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
from heapq import *
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())
lv_heap = []
ans = 0
lv_sum = 0
for lv_hp in range(N):
    heappush(lv_heap, -int(input()))
numb = min(42, len(lv_heap))
for lv_up in range(numb):
    target = -heappop(lv_heap)
    lv_sum += target
    if target >= 60:
        ans += 1
        if target >= 100:
            ans += 1
            if target >= 140:
                ans += 1
                if target >= 200:
                    ans += 1
                    if target >= 250:
                        ans += 1
print(lv_sum, ans)
