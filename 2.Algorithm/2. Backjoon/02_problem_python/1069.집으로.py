# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
X, Y, D, T = map(int, input().split())
cross = (X**2 + Y**2)**0.5
print('cross:', cross)
if D > T:
    if cross % D == 0:
        print((cross/D)*T)
    else:
        stopping = (cross//D)*T
        remain = cross % D
        remain_time = stopping + remain
        over_remain = D - remain
        over_time = stopping + T + over_remain
        # print(remain_time,over_time)
        print(min(remain_time, over_time))
else:
    print(cross)
