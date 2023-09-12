# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
start, end = map(int, input().split())
criteria, n = map(int, input().split())
answer = min(end, criteria+n) - max(start, criteria-n)
if answer >= 0:
    print(answer+1)
else:
    print("IMPOSSIBLE")