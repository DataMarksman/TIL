# SWEA. 5178 노드의 합
# 설계 목적: 내가 비어있으면, 내 자식들의 합을 나한테 배정해줘!
# 1.
# 개선점:
# 1.

def rooting(point):
    if point <= N:
        if tree_list[point] == 0:
            tree_list[point] = rooting(point*2) + rooting(point*2 + 1)
            return tree_list[point]
        else:
            return tree_list[point]
    else:
        return int(0)


T = int(input())
for case_num in range(1, T + 1):
    N, M, L = map(int, input().split())
    N = int(N)
    M = int(M)
    L = int(L)
    tree_list = [0]*(N+1)
    for leaf in range(M):
        idx, K = tuple(map(int, input().split()))
        tree_list[idx] = K
    rooting(1)
    print(f'#{case_num} {tree_list[L]}')
