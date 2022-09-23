# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
def calcul(A, B, pattern):
    global ans
    if ans or len(pattern) >= 1000 or len(bin(A)) > 502 or len(bin(B)) > 502:
        return
    if A == B:
        ans = pattern
    else:
        if A > B:
            calcul(A + 1, B * 2, pattern + 'X')
            calcul(A * 2, B + 1, pattern + 'Y')
        else:
            calcul(A * 2, B + 1, pattern + 'Y')
            calcul(A + 1, B * 2, pattern + 'X')


T = int(input())
for case_num in range(1, T + 1):
    N, M = map(int, input().split())
    ans = ''
    calcul(N, M, '')
    print(f'#{case_num} {ans}')