# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
N = int(input())
scores = list(map(int, input().split()))
start_from_DP = [[0,0,0] for _ in range(N)]
end_here_DP = [[0,0,0] for _ in range(N)]
start_from_DP[0] = [scores[0], scores[0], 0]
end_here_DP[0] = [scores[0], scores[0], 0]
for dp in range(1, N):
    score = scores[dp]
    start_from_DP[dp] = [score, score, max(start_from_DP[dp-1][2], end_here_DP[dp-1][2])]
    before_min, before_max, diff = start_from_DP[dp-1]
    up_diff = max(before_max, score) - min(before_min, score) + diff
    connected_min, connected_max, cntd_diff = end_here_DP[dp-1]
    down_diff = max(connected_max, score) - min(connected_min, score) - (connected_max - connected_min) +cntd_diff
    if down_diff >= up_diff:
        end_here_DP[dp] = [min(connected_min, score), max(connected_max, score), down_diff]
    else:
        end_here_DP[dp] = [min(before_min, score), max(before_max, score), up_diff]
answer = max(start_from_DP[N-1][2], end_here_DP[N-1][2])
# print(start_from_DP)
# print(end_here_DP)
print(answer)

"""
10
2 5 7 1 3 4 8 6 9 3
"""