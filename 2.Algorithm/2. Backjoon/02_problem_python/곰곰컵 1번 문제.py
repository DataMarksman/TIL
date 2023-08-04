# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
N = int(sys.stdin.readline().strip())
ans = 0
for case in range(N):
    if int(sys.stdin.readline().strip()[2:]) <= 90:
        ans += 1
print(ans)
