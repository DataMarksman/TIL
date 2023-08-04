# BOJ. 11053. 가장 긴 증가하는 부분 수열
# 설계 의도: LIS 구현
# 1. 돌면서 앞에서부터 쌓아간다.
# 2. 이전 값과 지금 값을 비교해서 길이 1(나 자신) + 1 을 할 것인지, 이전의 max 값을 가져올 것인지.
# 개선점:
# 1. DP 머리가 부족한가 봅니다. 진짜 너무너무 어렵습니다...
import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
dp = [1]*N
for i in range(1, N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))