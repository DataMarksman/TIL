# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip('\r\n')
v = set()
for soc in range(5):
    num = int(input())
    if num in v:
        v.discard(num)
    else:
        v.add(num)
print(v.pop())