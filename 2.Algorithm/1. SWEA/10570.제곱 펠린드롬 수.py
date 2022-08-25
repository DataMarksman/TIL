# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

def palindrome(n):
    n = list(str(n))
    flag = True
    while len(n) > 1:
        a = n.pop(0)
        b = n.pop()
        if a == b:
            continue
        else:
            flag = False
            break
    if flag:
        return True


T = int(input())
for case_num in range(1, T+1):
    S, E = tuple(map(int, input().split()))
    count = 0
    check_list = []
    for check in range(S, E+1):
        if palindrome(check):
            C = check ** (1 / 2)
            if C.is_integer():
                if palindrome(int(C)):
                    check_list += [(check, check**(1/2))]
                    count += 1
    print(f'#{case_num} {count}')


