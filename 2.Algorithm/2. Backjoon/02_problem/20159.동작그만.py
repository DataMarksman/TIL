# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
count = [[0, 0] for _ in range((N//2)+2)]
ans = [0]*((N//2)+2)
for check in range(N):
    if check%2 == 1:
        count[check+1][0] = count[check][0] + num_list[check]
        count[(N-1)-check]

    else:
        count[check + 1][0] = count[check][0]




