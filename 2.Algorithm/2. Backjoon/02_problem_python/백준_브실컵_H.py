# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N, M = map(int, input().split())
clap_cnt = [0 for _ in range(M)]
for case in range(N):
    claps = list(map(int, input().split()))
    for clap in range(M):
        clap_cnt[clap] += claps[clap]

portion = min(M, int(input()))
max_clap = sum(clap_cnt[:portion])
now_clap = int(max_clap)
for checking in range(portion, M):
    now_clap += clap_cnt[checking] - clap_cnt[checking - portion]
    if now_clap > max_clap:
        max_clap = int(now_clap)

print(max_clap)