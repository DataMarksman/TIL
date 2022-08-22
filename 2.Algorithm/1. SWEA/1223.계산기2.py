# SWEA.1223 계산기2
# 설계 목적: 후위연산 학습
# 1.
# 개선점:
# 1.

T = 10
for case_num in range(1,T+1):
    N = int(input())
    input_list = list(input())
    num_list = []

    while input_list:
        pick = input_list.pop(0)
        if pick.isnumeric():
            num_list += [int(pick)]
        elif pick == '*':
            A = int(num_list.pop())
            B = int(input_list.pop(0))
            C = A*B
            num_list.append(C)
    ans = sum(num_list)
    print(f'#{case_num} {ans}')
