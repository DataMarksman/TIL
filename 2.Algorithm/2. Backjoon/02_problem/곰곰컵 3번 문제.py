# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())
original_count = A + B + C

if X >= A:
    X = X - A
    A = 0
    Y += X//3
    X = X%3
else:
    A -= X
    X = 0

if Y >= B:
    Y = Y - B
    B = 0
    Z += Y//3
    Y = Y%3
else:
    B -= Y
    Y = 0

if Z >= C:
    Z = Z - C
    C = 0
    X += Z//3
    Z = Z%3
else:
    C -= Z
    Z = 0
if X >= A:
    X = X - A
    A = 0
    Y += X//3
    X = X%3
else:
    A -= X
    X = 0

if Y >= B:
    Y = Y - B
    B = 0
    Z += Y//3
    Y = Y%3
else:
    B -= Y
    Y = 0

if Z >= C:
    Z = Z - C
    C = 0
    X += Z//3
    Z = Z%3
else:
    C -= Z
    Z = 0

print(original_count - (A + B + C))