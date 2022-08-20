
# SWEA. 1859 백만 장자 프로젝트
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    price_list = list(map(int, input().split()))
    sum_profit = 0
    selling_price = 0
    flag = False
    while price_list:
        max_price = max(price_list)
        target = price_list.index(max_price)
        if target == 0:
            price_list.pop(0)
        else:
            if flag:
                profit = selling_price
                flag = False
            else:
                profit = 0

            for selling in range(target+1):
                selling_price = max_price - price_list.pop(target-selling)
                profit += selling_price
                if profit > 10000:
                    profit -= selling_price
                    flag = True
                    break
            sum_profit += profit

    print(f'#{case_num} {sum_profit}')

