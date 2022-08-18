# 4873. 반복 문자 지우기
def couple_breaker(couples, check):
    if check < 0:
        check = 0
    elif (check >= len(couples)-1) or (len(couples) < 2):
        return couples
    if couples[check] == couples[check+1]:
        del couples[check]
        del couples[check]
        return couple_breaker(couples, check-1)
    else:
        return couple_breaker(couples, check+1)


for case_num in range(1, int(input())+1):
    print(f'#{case_num} {len(couple_breaker(list(input()),0))}')