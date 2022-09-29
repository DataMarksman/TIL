# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
N = int(sys.stdin.readline())
island_up = [0]*(N+1)
island_sum = [0]*(N+1)
ans = 0
for put_in in range(2, N+1):
    lines = list(sys.stdin.readline().split())
    island_up[put_in] = int(lines[2])
    if lines[0] == 'W':
        island_sum[put_in] = int(lines[1]) * (-1)
    else:
        island_sum[put_in] = int(lines[1])
leaf_set = {i for i in range(2, N+1)}.difference(set(island_up))

while leaf_set:
    idx = int(leaf_set.pop())
    if island_sum[idx] > 0:
        survive = island_sum[idx]
    else:
        survive = 0
    pre_idx = set()
    while idx > 1:
        idx = island_up[idx]
        if island_sum[idx] != 0:
            if island_sum[idx] < 0:
                if survive + island_sum[idx] >= 0:
                    survive += island_sum[idx]
                    island_sum[idx] = 0
                    pre_idx.add(idx)
                else:
                    island_sum[idx] += survive
                    survive = 0
                    while pre_idx:
                        pick = pre_idx.pop()
                        island_up[pick] = idx
            else:
                survive += island_sum[idx]
                island_sum[idx] = 0
                pre_idx.add(idx)
    while pre_idx:
        pick = pre_idx.pop()
        island_up[pick] = 1
    ans += survive
print(ans)