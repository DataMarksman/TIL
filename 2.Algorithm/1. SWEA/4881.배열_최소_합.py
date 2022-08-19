# import sys
# sys.stdin = open("sample_input.txt", "r")

def num_sum(arr, platform, n):
    print(n, arr)
    global stock_list
    stock = arr
    dummy_stock = stock[:]
    panel = platform
    dummy_board = platform[:]
    if n >= N:
        print(arr)
        stock_list += [sum(stock)]
    else:
        for pick in range(N-n):
            stock = dummy_stock[:]
            panel = dummy_board[:]
            stock += [panel[n][pick]]
            for erase in range(n, N-n):
                del panel[erase][pick]
            num_sum(stock, panel, n+1)


T = int(input())

for case_num in range(1, T + 1):
    stock_list = []
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    num_sum([], board, 0)
    print(f'#{case_num} {stock_list}')
