# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)
def pulling(k):
    global ans_set
    if 0 < k < MAX:
        ans_set.add(k)
    if 0 <= k < MAX:
        pulling(k + A)
        pulling(k + B)


ans_set = set()
A, B, C = map(int, input().split())
A = int(A)
B = int(B)
MAX = int(C)

pulling(0)
ans_list = sorted(list(ans_set))
print(*ans_list)