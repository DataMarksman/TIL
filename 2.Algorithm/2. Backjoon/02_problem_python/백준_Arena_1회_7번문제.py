# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

from itertools import permutations
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')


def cmp(expressions):
    all_results = set()

    for expr in expressions:
        all_results |= set(permutations(expr))

    return all_results + 2

N = int(input())
num_list = sorted(list(map(int, input().split())))

T = int(input())
aim_list = list(map(int, input().split()))

answer = []
for aim in aim_list:
    P = 0
    for origin in num_list:
        if origin <= aim:
            if aim % origin == 0:
                P += cmp(aim//origin)
        else:
            break
    answer.append(P)
print(*answer)