# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')


def day_trading(budget, date, idx, profit_sum):
    if idx >= C or budget == 0:
        return budget + profit_sum
    before_price = stock_movement[idx][date-1]
    present_price = stock_movement[idx][date]
    profit = present_price - before_price
    if profit <= 0 or budget - before_price < 0:
        return day_trading(budget, date, idx + 1, profit_sum)
    else:
        return max(day_trading(budget-before_price, date, idx + 1, profit_sum + present_price),
                   day_trading(budget, date, idx + 1, profit_sum))


C, D, M = map(int, input().split())
stock_movement = []
answer = int(M)

for future_stocks in range(C):
    stock_price = list(map(int, input().split()))
    stock_movement.append(stock_price)

for day_trade in range(1, D):
    answer = day_trading(answer, day_trade, 0, 0)

print(answer)