# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline

def div_coq(x, y):
    if y == 1:
        return x % C
    elif y % 2 == 0:
        return (div_coq(x, y//2) ** 2) % C
    else:
        return ((div_coq(x, y // 2) ** 2) * x) % C


A, B, C = map(int, input().split())
A = A % C
print(div_coq(A, B))
