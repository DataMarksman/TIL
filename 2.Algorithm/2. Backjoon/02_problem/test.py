def fibo(n):
    if n <= 1:
        return 1
    ans = fibo(n-1) + fibo(n-2)
    return ans


N = int(input())
stack = []
flag = True
count = 1
for i in range(N//2, N):
    stack += [i]
while flag:
    count += 1
    combo = fibo(count - 1) / fibo(count)
    print(count, combo)
    tmp_list = []
    if count % 2 == 0:
        for k in range(len(stack)):
            if stack[k] >= combo * N: