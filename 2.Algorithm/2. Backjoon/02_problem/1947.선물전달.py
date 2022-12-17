# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
dp = [0]*(N+2)
dp[0] = 0
dp[1] = 1
for dp_check in range(2, N+1):
    dp[dp_check] = ((dp_check-1)*(dp[dp_check-1] + dp[dp_check-2]))%1000000000
print(dp[N-1]%1000000000)
