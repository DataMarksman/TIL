# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

N = int(input())
island_up = [0]*(N+1)
island_sum = [0]*(N+1)
sheep_set = set()
ans = 0
for put_in in range(2, N+1):
    lines = list(input().split())
    island_up[put_in] = int(lines[2])
    if lines[0] == 'W':
        island_sum[put_in] = int(lines[1]) * (-1)
    else:
        island_sum[put_in] = int(lines[1])
        sheep_set.add(put_in)
size = len(sheep_set)
for checking in range(size):
    pick = sheep_set.pop()
    survive = island_sum[pick]
    while survive > 0:
        pick = island_up[pick]
        if pick == 1:
            break
        elif island_sum[pick] < 0:
            if survive + island_sum[pick] > 0:
                survive += island_sum[pick]
                island_sum[pick] = 0
            else:
                island_sum[pick] = abs(survive + island_sum[pick])
                survive = 0
    if survive > 0:
        ans += survive
print(ans)