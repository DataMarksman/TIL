# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
def shaf(x,y):
    A = sum(i for i in range(1, x+y))
    B = A - (y-1)
    return B


def andmark(n):
    target = 0
    sum_target = 0
    while sum_target < n:
        target += 1
        sum_target += target
    C = sum_target-n
    D = (target-C, C+1)
    return D


T = int(input())
for case_num in range(1, T + 1):
    N, M = tuple(map(int, input().split()))
    first_answer = andmark(N)
    second_answer = andmark(M)
    ans = shaf(first_answer[0]+second_answer[0], first_answer[1]+second_answer[1])
    print(f'#{case_num} {ans}')