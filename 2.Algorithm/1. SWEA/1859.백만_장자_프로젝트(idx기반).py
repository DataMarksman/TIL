# SWEA. 1859 백만 장자 프로젝트
# 설계 목적:
# 1. 그냥 좌표 찍고 거기서부터 앞으로 긁어오기.
# 개선점:
# 1. 처음에 문제 조건을, 하루에 얻을 수 있는 최대 이득이 10,000 이라고 인지해서 문제를 어렵게 풀고 있었다.
#   문제 조건을 제대로 정리하고 풀도록 하자....

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    price_list = list(map(int, input().split()))
    sum_profit = 0
    while price_list:
        max_price = max(price_list)
        target = price_list.index(max_price)
        if target == 0:
            price_list.pop(0)
        else:
            sum_profit += (max_price*target) - sum(price_list[:target])
            price_list = price_list[target:]
    print(f'#{case_num} {sum_profit}')


