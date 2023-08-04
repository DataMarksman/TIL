# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

N = int(input())
island_up = [0]*(N+1)
island_sum = [0]*(N+1)
sheep_list = []
# wolf_list = []
ans = 0
for put_in in range(2, N+1):
    lines = list(input().split())
    Sheep = int(lines[1])
    cur_idx = int(put_in)
    island_up[cur_idx] = int(lines[2])
    if lines[0] == 'W':
        island_sum[cur_idx] = Sheep * (-1)
        # wolf_list.append([Sheep * (-1), cur_idx])
    else:
        island_sum[cur_idx] = Sheep
        sheep_list.append([Sheep, cur_idx])

print(island_up)
print(island_sum)
# print(wolf_list)
print(sheep_list)

# for wolf_check in range(len(wolf_list)):
#     wolf_pack = island_sum[wolf_list[wolf_check][1]]
#     wolf_idx = wolf_list[wolf_check][1]
#     while wolf_idx > 1:
#         wolf_idx = island_up[wolf_idx]
#         if island_sum[wolf_idx] < 0:
#             wolf_pack += island_sum[wolf_idx]

for checking in range(len(sheep_list)):
    survive = island_sum[sheep_list[checking][1]]
    idx = sheep_list[checking][1]
    while survive > 0:
        print(idx, survive)
        idx = island_up[idx]
        if idx == 1:
            break
        elif island_sum[idx] < 0:
            if survive + island_sum[idx] > 0:
                survive += island_sum[idx]
                island_sum[idx] = 0
            else:
                island_sum[idx] = abs(survive + island_sum[idx])
                survive = 0
    if survive > 0:
        ans += survive
print(ans)