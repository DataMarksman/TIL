# 현재 버전 테스트 13, 15, 18이 실패. 메모리나 시간 문제는 아닌 것 같고, 로직 문제 인듯 함.
# 케이스에 0을 넣어도 같은 문제가 발생. 즉 할인은 무조건 들어간다고 생각 해야함
# 어짜피 원하는 할인률이 1부터 시작해서 0은 걸러도 되는 부분.
# int 빼니 통과 됩니다. 소숫점 계산 나오나봄


import itertools
import math


def solution(users, emoticons):
    sale_per = [1, 2, 3, 4]
    K = int(len(emoticons))
    brute_set = set(itertools.product(sale_per, repeat = K))
    max_membership = 0
    max_profit = 0
    while brute_set:
        membership = 0
        profit = 0
        price_list = [0]*5
        pick = brute_set.pop()
        for emo_sale in range(K):
            price_list[pick[emo_sale]] += emoticons[emo_sale]*(1-(pick[emo_sale]/10))
        for members in range(len(users)):
            price = sum(price_list[math.ceil(users[members][0]/10):]) 
            if price >= users[members][1]:
                membership += 1
            else:
                profit += price
        if membership > max_membership:
            max_membership = membership
            max_profit = profit
        elif membership == max_membership and profit > max_profit:
            max_profit = profit
    answer = [max_membership, max_profit]
    return answer