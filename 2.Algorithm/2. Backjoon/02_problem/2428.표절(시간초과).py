# BOJ. 2428 표절
# 설계 의도:
# 1. for문 두개 돌리면서 조건에 맞는 케이스 카운팅
# 개선점:
# 인줄 알았는데 시간초과...

import sys

N = int(sys.stdin.readline())
num_list = [int(x) for x in sys.stdin.readline().split()]
num_set = set(num_list)
real_list = sorted(list(num_set))
num_list.sort()
count = 0
for i in range(len(real_list)):
    for j in range(len(real_list)):
        if i == j and real_list[j] > 1:
            count += (real_list[i]*(real_list[i]-1))//2
        elif 0.9*real_list[j] <= real_list[i] and i < j:
            count += num_list.count(real_list[i])*num_list.count(real_list[j])
print(count)
