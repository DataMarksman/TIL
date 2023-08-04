# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)


N = int(input())

A = N // 5
B = N % 5
ans = -1
if B == 0:
    ans = A
elif B == 3:
    ans = A + 1
elif B == 4 and A >= 1:
    ans = A + 2
elif B == 1 and A >= 1:
    ans = A + 1
elif B == 2 and A >= 2:
    ans = A + 2

print(ans)