# 곤란하면 재귀다. 주식 최저가가 100이므로, 약간 효율화 해봤다.
def best_invest(date, budget, income, idx):
    global best_profit
    if idx >= N or budget < 100:
        if income > best_profit:
            best_profit = income
        return
    for searching in range(idx, N):
        if profit_list[searching][date] > 0 and budget - asset_list[searching][date] >= 0:
            best_invest(date, budget - asset_list[searching][date], income + profit_list[searching][date], searching)
    best_invest(date, budget, income, idx + 1)
    if income > best_profit:
        best_profit = income


T = int(input())
for tc in range(1, T+1):
    MS, MA = map(int, input().split())
    N, L = map(int, input().split())
    asset_list = []
    profit_list = [[] for _ in range(N)]
    ans = 0
    for product in range(N):
        line = list(map(int, input().split()))
        for times in range(L):
            profit_list[product].append(line[times+1] - line[times])
        asset_list += [line]

    for month in range(L):
        best_profit = 0
        best_invest(month, (int(MS) + int(MA)*month + int(ans)), 0, 0)
        ans += best_profit
    print(f'#{tc} {ans}')

"""
3
300 60
3 8
135 120 111 144 170 170 171 173 169
156 150 144 144 144 150 150 150 147
195 180 165 150 141 172 185 190 159
400 0
5 8
180 180 180 150 120 150 180 180 180
315 315 315 300 300 300 300 300 315
219 282 255 255 255 219 219 219 219
228 222 204 246 255 228 228 228 228
120 150 120 120 120 120 120 120 120
500 100
5 5
100 100 100 100 100 100
100 100 100 100 100 100
100 100 100 100 100 100
100 100 100 100 100 100
100 100 100 100 100 110

#1 448
#2 465
#3 906
#4 1847
#5 1094

"""