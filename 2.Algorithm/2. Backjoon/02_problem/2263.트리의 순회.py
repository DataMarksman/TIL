# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)
def reorder(k):
    if k <= N:
        reorder(k*2)
        re_list[k] = in_list.pop(0)
        reorder(k*2 + 1)


def preorder(t):
    if t <= N:
        ans.append(re_list[t])
        preorder(t*2)
        preorder(t*2 + 1)


N = int(input())
in_list = list(map(int, input().split()))
post_list = list(map(int, input().split()))
re_list = [0]*(N+1)
ans = []
reorder(1)
print(*re_list)
preorder(1)
print(*ans)


"""
21
1 3 2 7 4 6 5 15 11 9 12 8 13 10 14 21 19 17 20 16 18
1 2 3 4 5 6 7 11 12 9 13 14 10 8 15 19 20 17 18 16 21
"""
