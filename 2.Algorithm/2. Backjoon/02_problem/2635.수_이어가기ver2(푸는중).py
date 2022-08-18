def fibo(n):
    if n <= 1:
        return 1
    ans = fibo(n-1) + fibo(n-2)
    return ans


def fibo_check(cnt):
    global even_stack
    global odd_stack
    n = fibo(cnt-1) / fibo(cnt)
    if cnt % 2 == 0:
        for k in range(len(odd_stack)):
            if odd_stack[k] <= n * N:
                even_stack.append(odd_stack[k])
        else:
            if len(even_stack) >= 1:
                odd_stack = []
                return fibo_check(cnt +1)
            else:
                return odd_stack
    elif cnt % 2 != 0:
        for t in range(len(even_stack)):
            if even_stack[t] >= n * N:
                odd_stack.append(even_stack[t])
        else:
            if len(odd_stack) >= 1:
                even_stack = []
                return fibo_check(cnt + 1)
            else:
                return even_stack


N = int(input())
even_stack = []
odd_stack = []
flag = True
for i in range(N//2, N):
    even_stack += [i]
    odd_stack += [i]

print(fibo_check(5))

"""
while flag:
    cnt += 1
    
"""