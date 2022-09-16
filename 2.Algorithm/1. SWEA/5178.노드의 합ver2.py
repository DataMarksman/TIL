# SWEA. 5178 노드의 합
# 설계 목적: 내가 비어있으면, 내 자식들의 합을 나한테 배정해줘!
# 1.
# 개선점:
# 1.


T = int(input())
for case_num in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree_list = [0]*(N+1)
    for leaf in range(M):
        idx, K = tuple(map(int, input().split()))
        tree_list[idx] = K
    ans = 0
    tree_set = set()
    tree_set.add(L)
    while tree_set:
        pick = tree_set.pop()
        if pick <= N:
            if tree_list[pick]:
                ans += tree_list[pick]
            else:
                tree_set.add(pick * 2)
                tree_set.add(pick * 2 + 1)
    print(f'#{case_num} {ans}')
