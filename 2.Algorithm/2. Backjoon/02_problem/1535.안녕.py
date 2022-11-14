# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline


N = int(input())
HP = [0] + list(map(int, input().split()))
GET = [0] + list(map(int, input().split()))
DP = [[0] * 101 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        if HP[i] <= j:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j - HP[i]] + GET[i])
        else:
            DP[i][j] = DP[i-1][j]
print(DP[N][99])