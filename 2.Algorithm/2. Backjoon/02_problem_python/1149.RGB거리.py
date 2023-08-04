# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline


N = int(input())
dp = list(map(int, input().split()))
for checking in range(N-1):
    temp_dp = [0, 0, 0]
    A, B, C = map(int, input().split())
    temp_dp[0] = min(dp[1], dp[2]) + A
    temp_dp[1] = min(dp[0], dp[2]) + B
    temp_dp[2] = min(dp[0], dp[1]) + C
    dp = temp_dp[:]
print(min(dp))

