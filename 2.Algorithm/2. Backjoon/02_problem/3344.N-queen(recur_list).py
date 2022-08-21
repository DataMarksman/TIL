# 2806. N-Queen
# 실행 시간 : 0.14634s
import sys
sys.setrecursionlimit(10**8)


def queen_up(check, cross_check, r_cross_check, stock, n, k):
    global count
    if n >= N:
        count += 1
        erase = stock.pop()
        check[erase] = 0
        cross_check[n + erase - 1] = 0
        r_cross_check[N + (n - erase) - 1] = 0
        k = erase
        return queen_up(check, cross_check, r_cross_check, stock, n - 1, k+1)

    elif k >= N:
        if len(stock) == 0:
            return print(count)
        else:
            erase = stock.pop()
            check[erase] = 0
            cross_check[n + erase - 1] = 0
            r_cross_check[N + (n - erase) - 1] = 0
            k = erase
            return queen_up(check, cross_check, r_cross_check, stock, n - 1, k+1)
    else:
        for i in range(k, N):
            if check[i] == 0 and cross_check[n+i] == 0 and r_cross_check[N+(n-i)] == 0:
                check[i] = 1
                cross_check[n+i] = 1
                r_cross_check[N+(n-i)] = 1
                stock += [i]
                return queen_up(check, cross_check, r_cross_check, stock, n + 1, 0)

        else:
            erase = stock.pop()
            check[erase] = 0
            cross_check[n + erase - 1] = 0
            r_cross_check[N + (n - erase) - 1] = 0
            k = erase
            return queen_up(check, cross_check, r_cross_check, stock, n - 1, k+1)


N = int(input())
count = 0
queen_up([0]*N, [0]*(2*N), [0]*(2*N), [], 0, 0)
