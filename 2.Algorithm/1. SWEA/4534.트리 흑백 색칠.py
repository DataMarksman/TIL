# CNS 때도 멀티탭 못 풀었는데, 이번에도 못 풀었당...
# 검은색으로 진입하면 다음에 흰색만 가능
# 흰색으로 진입하면 다음에 검/흰 둘다 가능

def root_dp(col, pre_idx, idx):
    result = 1
    # col == 0 이 검정, 1 이 하양
    for dp in node_list[idx]:
        if dp == pre_idx:
            continue
        elif len(node_list[dp]) == 1 and node_list[dp][0] == idx:
            continue
        else:
            result *= root_dp(1, idx, dp)
    else:
        for dp in node_list[idx]:
            if dp == pre_idx:
                continue
            elif len(node_list[dp]) == 1 and node_list[dp][0] == idx:
                result *= 2
            else:
                result *= root_dp(1, idx, dp) + root_dp(0, idx, dp)
    return result % 1000000007


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    node_list = [[] for _ in range(N+1)]
    if N == 2:
        A, B = map(int, input().split())
        ans = 3
    else:
        ans = 0
        for input_node in range(N-1):
            A, B = map(int, input().split())
            node_list[A].append(B)
            node_list[B].append(A)
        for checking in range(N+1):
            if len(node_list[checking]) > 0:
                ans = root_dp(0, 0, checking) + root_dp(1, 0, checking)
                break
    print(f'#{case_num} {ans}')