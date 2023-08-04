# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())
MAX = sys.maxsize
A, B, C = map(int, input().split())
DP = [[A, MAX, MAX], [MAX, B, MAX], [MAX, MAX, C]]
for case_num in range(1, N):
    a, b, c = map(int, input().split())
    DP = [[a + min(DP[1][0], DP[2][0]), a + min(DP[1][1], DP[2][1]), a + min(DP[1][2], DP[2][2])],
          [b + min(DP[0][0], DP[2][0]), b + min(DP[0][1], DP[2][1]), b + min(DP[0][2], DP[2][2])],
          [c + min(DP[0][0], DP[1][0]), c + min(DP[0][1], DP[1][1]), c + min(DP[0][2], DP[1][2])]]
answer = min(DP[0][1], DP[0][2],
             DP[1][0], DP[1][2],
             DP[2][0], DP[2][1])
print(answer)



#
# 3
# 1 100 100
# 1 100 100
# 100 1 100