# SWEA. 5178 노드의 합
# 설계 목적: 내가 비어있으면, 내 자식들의 합을 나한테 배정해줘!
# 1.
# 개선점:
# 1.


T = int(input())
for case_num in range(1, T + 1):
    N, M, L = map(int, input().split())
    ans = 0
    for leaf in range(M):
        idx, K = map(int, input().split())
        while idx >= 1:
            if idx == L:
                ans += K
                break
            elif idx < L:
                break
            idx //= 2
    print(f'#{case_num} {ans}')
