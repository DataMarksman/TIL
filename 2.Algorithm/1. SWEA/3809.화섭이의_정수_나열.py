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
    num_list = []
    first_line = list(map(int, input().split()))
    num_list += first_line
    K = len(first_line)
    size = N//K if N % K == 0 else (N//K) + 1

    for put_in in range(size-1):
        line_in = list(map(int, input().split()))
        num_list += line_in

    num_set = set()
    flag = True
    x = -1
    for i in range(N):
        num_set.add(num_list[i])
        if i < N - 1:
            num_set.add(num_list[i]*10 + num_list[i+1])
            if i < N - 2:
                num_set.add(num_list[i] * 100 + num_list[i + 1] * 10 + num_list[i + 2])

    while flag:
        x += 1
        if x not in num_set:
            flag = False
            break
    print(f'#{case_num} {x}')
