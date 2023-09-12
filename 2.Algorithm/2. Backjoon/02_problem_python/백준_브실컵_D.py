# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
S, M, N = map(int, input().split())
size = int(S)
U = 0
for case in range(M+N):
    if bool(int(input())):
        U += 1
    else:
        U -= 1
    if U > size:
        size *= 2
print(size)
