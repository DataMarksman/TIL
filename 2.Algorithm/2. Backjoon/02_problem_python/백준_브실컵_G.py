# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N, M = map(int, input().split())
A = 1
B = 1
for cross in range(N):
    A = (A * M)%1000000007
    B = (B * (M-1))%1000000007
if B > A:
    A += 1000000007
print((A - B)%1000000007)