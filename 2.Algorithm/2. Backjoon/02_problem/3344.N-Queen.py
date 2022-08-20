# 2806. N-Queen

def queen_up(check, cross_check, r_cross_check, n, stock):
    global ans_list
    for i in range(N):
        if len(stock) >= N:
            ans_list += [stock]
        if check[i] == 0 and cross_check[n+i] == 0 and r_cross_check[N+(n-i)] == 0:
            check[i] = 1
            cross_check[n+i] = 1
            r_cross_check[N+(n-i)] = 1
            stock += [i+1]
            print(stock, len(stock), n)
            queen_up(check, cross_check, r_cross_check, n+1, stock)
            check[i] = 0
            cross_check[n+i] = 0
            r_cross_check[N+(n - i)] = 0
            stock.pop()


N = int(input())
ans_list = []
queen_up([0]*N, [0]*(2*N), [0]*(2*N), 0, [])
print(ans_list[0])

