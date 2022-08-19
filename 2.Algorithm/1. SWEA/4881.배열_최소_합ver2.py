# 4881. 배열 최소 합 ver2
# import sys
# sys.stdin = open("sample_input.txt", "r")

def num_sum(arr, stack, n):
    global stock_list
    stock = arr
    file = stack
    if n >= N:
        print(f'완료 {n}{arr}')
        stock_list += [[sum(file)]]
    else:
        print(f'반복문 {n}{arr}')
        for check in range(N-n):
            if stock[check] == 0:
                file += [board[n][check]]
                stock[check] = 1
                num_sum(stock, file, n+1)
                stock[check] = 0

T = int(input())

for case_num in range(1, T + 1):
    stock_list = []
    N = int(input())
    board = [[int(i) for i in input().split()] for _ in range(N)]
    num_sum([0]*N, [], 0)
    print(f'#{case_num} {min(stock_list)}')
