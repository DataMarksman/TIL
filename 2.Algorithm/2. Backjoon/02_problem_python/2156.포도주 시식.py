# BOJ. 2156. 포도주 시식
# 설계 의도: 패턴 3분할. DP
# 1. 1개 집는 패턴(이번에 집는 패턴),
# 2. 2개 집는 패턴(전꺼 이번꺼),
# 3. 안집는 패턴 이렇게 3개를 보고 싶어요... 그 중에 큰거를 가지고 가겠습니다.
import sys
input = sys.stdin.readline
N = int(input())
num_list = [int(input()) for _ in range(N)]
DP = [0]*(N+1)
if N <= 2:
    print(sum(num_list))
else:
    DP[0] = num_list[0]
    DP[1] = num_list[0] + num_list[1]
    DP[2] = max(num_list[0] + num_list[1], num_list[0] + num_list[2], num_list[1] + num_list[2])
    for dping in range(3, N):
        DP[dping] = max(max(DP[dping-2] + num_list[dping], DP[dping-3] + num_list[dping-1] + num_list[dping]), DP[dping-1])
    print(DP[N-1])