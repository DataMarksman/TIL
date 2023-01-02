
T = int(input())
for tc in range(1, T+1):
    MS, MA = map(int, input().split())
    N, L = map(int, input().split())
    asset_list = []
    dp_list = [[] for i in range(N)]
    ratio_list = [[] for j in range(L)]
    for dp_set in range(N):
        line = list(map(int, input().split()))
        for checking in range(L):
            profit = line[checking] - line[checking-1]
            if profit > 0:
                dp_list[checking].append(profit)
                ratio_list[dp_set].append(line[checking]/line[checking-1])
            else:
                dp_list[checking].append(0)
                ratio_list[dp_set].append((0)
        asset_list += [line]
    for sales in range(1, L+1):
        left = int(MS) + MA*sales
        for compare in range(N):
            target = asset_list[compare][sales] - asset_list[compare][sales-1]
            if target > best:
                best = target



    print(f'#{tc} {ans}')


"""

5
2
5 5
2
4 2
2
3 4
4
2 3 10 5
4
1 2 3 4

"""