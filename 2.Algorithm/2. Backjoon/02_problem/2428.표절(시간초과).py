# BOJ. 2428 표절
# 설계 의도:
# 1. for문 두개 돌리면서 조건에 맞는 케이스 카운팅
# 개선점:
# 인줄 알았는데 시간초과...

import sys

N = int(sys.stdin.readline())
num_list = [int(x) for x in sys.stdin.readline().split()]

num_list.sort()
count = 0
for i in range(N-1):
    for j in range(i+1, N):
        if 0.9*num_list[j] <= num_list[i]:
            count += 1
print(count)
