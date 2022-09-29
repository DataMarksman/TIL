# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
def kruskal(x, y):
    global pair_list
    if x == y:
        if pair_list[x] != x:
            pair_list[x] = kruskal(pair_list[x], pair_list[x])  # path compression
        return pair_list[x]
    pair_list[kruskal(y, y)] = kruskal(x, x)


T = int(input())
for case_num in range(1, T + 1):
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))
    pair_list = list(range(N+1))
    for pairing in range(M):
        kruskal(input_list[2*pairing], input_list[2*pairing+1])
    for rechecking in range(1, N+1):
        kruskal(rechecking, rechecking)
    ans_set = set(pair_list[1:])
    print(pair_list[1:])
    print(f'#{case_num} {len(ans_set)}')

"""
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4

"""