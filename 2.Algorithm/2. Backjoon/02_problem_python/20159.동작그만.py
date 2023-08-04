# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
num_list = [0] + list(map(int, input().split())) + [0]
count = [[0, 0] for _ in range(N+2)]
ans = [0]*(N+2)
for check in range(1, N+2):
    if check % 2 == 1:
        count[check][0] = count[check-1][0] + num_list[check]

    else:
        count[check][0] = count[check - 1][0]

    if check%2 == 0:
        count[N+1 - check][1] = count[N + 2 - check][1] + num_list[N+2 - check]
    else:
        count[N + 1 - check][1] = count[N + 2 - check][1]

    ans[check] += count[check][0]
    ans[N+1 - check] += count[N+1 - check][1]
print(count)
print(ans)
print(max(ans))




