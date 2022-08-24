# import sys
# sys.stdin = open("sample_input.txt", "r")






T = int(input())
for case_num in range(1, T+1):
    A, B = tuple(map(int, input().split()))
    ans = str('')
    while A // B != 2:
        if A == B:
            break
        elif A > B and A // B > 2:
            A = A+1
            B = B*2
            ans += 'X'
        elif A > B and A // B == 1:
            A = A*2
            B = B+1
            ans += 'Y'
        elif A < B:
            A = A * 2
            B = B + 1
            ans += 'Y'
    T = A % B
    ans += 'YX'*T
    ans += 'X'
    print(f'#{case_num} {ans}')


