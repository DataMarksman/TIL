# 2635. 수 이어가기
def len_check(k):
    global max_len
    global ans_list
    stock_list = [N, k] + [0]*100
    top = 1
    while stock_list[top] >= 0:
        top += 1
        stock_list[top] = stock_list[top-2] - stock_list[top-1]
    if len(stock_list[:top]) > max_len:
        max_len = len(stock_list[:top])
        ans_list = stock_list[:top]


N = int(input())
ans_list = [N, ]
max_len = 0
if N == 1:
    max_len = 4
    ans_list = [1, 1, 0, 1]
elif N <= 10:
    for numbers in range(int(0.6*N), N+1):         # N+1 까지 범위를 주어야 하는 이유: 1
        len_check(numbers)
elif N <= 1000:
    for numbers in range(int(0.61*N), int(0.66*N)+1):         # N+1 까지 범위를 주어야 하는 이유: 1
        len_check(numbers)
else:
    for numbers in range(int(0.615*N), int(0.62*N)+1):         # N+1 까지 범위를 주어야 하는 이유: 1
        len_check(numbers)
print(max_len)
print(*ans_list)

