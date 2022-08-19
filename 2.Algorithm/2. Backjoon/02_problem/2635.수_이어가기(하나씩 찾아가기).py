# 2635. 수 이어가기
def len_check(k):
    global max_len
    global ans_list
    stock_list = [N, k] + [0]*200
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
for numbers in range(N//2, N+1):
    len_check(numbers)
print(max_len)
print(*ans_list)













