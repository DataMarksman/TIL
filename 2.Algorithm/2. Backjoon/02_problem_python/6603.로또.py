# BOJ. 6603 로또
# 설계 의도: itertools 쓸 줄 아시나요?
# 개선점:
# 1. 사실 없지 않나 싶다.
import sys
import itertools
num_list = list(map(int, sys.stdin.readline().split()))
while len(num_list) != 1 and num_list[0] != 0:
    print_list = sorted(list(itertools.combinations(num_list[1:], 6)))
    for printing in range(len(print_list)):
        print(*print_list[printing])
    print()
    num_list = list(map(int, sys.stdin.readline().split()))
