# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())

print(int(N*(N+1)/2))
print(int((N*(N+1)/2)**2))
print(int((N*(N+1)/2)**2))