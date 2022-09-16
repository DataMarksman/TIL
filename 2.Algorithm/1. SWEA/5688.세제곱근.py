# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    ans = N**(1/3)
    upper_ans = int(ans) + 1
    if abs(ans - int(ans)) <= 0.00001:
        print(f'#{case_num} {int(ans)}')
    elif abs(ans - upper_ans) <= 0.00001:
        print(f'#{case_num} {upper_ans}')
    else:
        print(f'#{case_num} {-1}')


