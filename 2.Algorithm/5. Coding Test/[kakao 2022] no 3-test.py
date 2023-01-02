# 현재 버전 테스트 13, 15, 18이 실패. 메모리나 시간 문제는 아닌 것 같고, 로직 문제 인듯 함.
# 케이스에 0을 넣어도 같은 문제가 발생. 즉 할인은 무조건 들어간다고 생각 해야함


import itertools
import math



sale_per = [1, 2, 3, 4]
K = 5
brute_set = set(itertools.product(sale_per, repeat = 7))
print(brute_set)