# BOJ. 1947. 선물 전달
# 설계 의도: DP..
# 1. 점화식 세우다가 수학 공부를 했다...
# 개선점:
# 더 빠르게 어떻게 하는거죠?
import sys
input = sys.stdin.readline
N = int(input())

# N 이 3보자 작을때, 리스트 에러 막기 위함.
dp = [0]*(N+2)

# 이 부분에서 dp[0]을 고려 안해줘서 뒤에서 계속 아사리가 났다.
dp[1] = 0
# 1 명일때, 0개의 케이스
dp[2] = 1
# 2명일때, 1가지

# 3명 부터 N명까지의 케이스를 뽑는데, 아까처럼 idx 0부터 시작하면, 명수 -1에서 에러난다.
for dp_check in range(3, N+1):
    # 점화식 대로 진행하면 문제 없다.
    dp[dp_check] = ((dp_check-1)*(dp[dp_check-1] + dp[dp_check-2]))%1000000000
print(dp[N]%1000000000)
