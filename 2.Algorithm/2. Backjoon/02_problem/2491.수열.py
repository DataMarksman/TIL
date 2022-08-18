# BOJ.2491 수열
# 설계 의도: 그냥 심플하게 생각해보자.
# 이전 버전에서 개선 한 점: 논리를 가능한 간결하게 진행.

N = int(input())
num_list = list(map(int, input().split()))
up_stock = 1
down_stock = 1
max_stock = 1
for checking in range(1, N):
    if num_list[checking] >= num_list[checking-1]:
        up_stock += 1
        if num_list[checking] > num_list[checking-1]:
            down_stock = 1
        if up_stock > max_stock:
            max_stock = int(up_stock)
    if num_list[checking] <= num_list[checking-1]:
        down_stock += 1
        if num_list[checking] < num_list[checking-1]:
            up_stock = 1
        if down_stock > max_stock:
            max_stock = int(down_stock)
print(max_stock)