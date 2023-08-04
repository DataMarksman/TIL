# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
n = int(input())
step = [int(input()) for i in range(n)] + [0] * 2
dp = [0]*(n+2)
dp[0] = step[0]
dp[1] = step[0] + step[1]
dp[2] = max(dp[0] + step[2], step[1] + step[2])

for d in range(3, n):
    dp[d] = max(dp[d-3] + step[d-1] + step[d], dp[d-2] + step[d])
print(dp[n-1])