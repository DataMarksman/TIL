# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())
lt = list(map(int, input().split()))
ans = []
for tc in range(N):
    if lt[tc] == 300:
        ans.append(1)
    elif 300 > lt[tc] >= 275:
        ans.append(2)
    elif 275 > lt[tc] >= 250:
        ans.append(3)
    else:
        ans.append(4)
print(*ans)