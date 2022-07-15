def f(x):
    if p == p[::-1]:
        return 1
    else:
        return 0

t = int(input())

for i in range(1,t+1):
    p = input()
    print("#%d" %i, f(p))
    