# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

A, B = map(int, input().split())
multiple = A * B
while B > 0:
    A, B = B, A % B
print(A)
print(multiple // A)