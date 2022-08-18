def fibo(n):
    if n <= 1:
        return 1
    elif n >= 2 and len(fibo_memo) < n+1:
        fibo_memo.append(fibo(n-1)+fibo(n-2))
    return fibo_memo[n]


fibo_memo = [1, 1, 2, 3, 5]
N = int(input())
stack = []
flag = True
count = 1
for i in range(N//2, N):
    stack += [i]
while flag:
    count += 1
    combo = fibo(count - 1) / fibo(count)
    tmp_list = []
    if count % 2 == 0:
        for k in range(len(stack)):
            if stack[k] <= combo * N:
                tmp_list += [k]
    else:
        for t in range(len(stack)):
            if stack[k] >= combo * N:
                tmp_list += [t]
    if len(tmp_list) >= 1:
        stack = tmp_list
        count += 1
    elif len(tmp_list) == 0:
        break
print(stack, count)

"""
while flag:
    count += 1
    
"""