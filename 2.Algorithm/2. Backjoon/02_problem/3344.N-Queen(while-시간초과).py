# 2806. N-Queen

N = int(input())

flag = True
stock = []
check = set()
cross_check = set()
r_cross_check = set()
start = 0
n = 0
while flag:
    if n >= N and len(stock) >= N:
        print(*stock, sep='\n')
        flag = False

    else:
        for i in range(start, N):
            if (i not in check) and (n+i not in cross_check) and (N+(n-i) not in r_cross_check):
                check.add(i)
                cross_check.add(n+i)
                r_cross_check.add(N+(n-i))
                stock.append(i+1)
                n += 1
                start = 0
                break
        else:
            stack = stock.pop()
            check.remove(stack-1)
            cross_check.remove(stack + n - 2)
            r_cross_check.remove(N+(n-stack))
            n -= 1
            while stack + 1 > N:
                stack = stock.pop()
                check.remove(stack - 1)
                cross_check.remove(stack + n - 2)
                r_cross_check.remove(N + (n - stack))
                n -= 1
            start = stack
