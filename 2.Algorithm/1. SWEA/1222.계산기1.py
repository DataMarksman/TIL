# SWEA.1224 계산기2
# 설계 목적: 후위연산 학습
# 1.
# 개선점:
# 1.

T = 10
for case_num in range(1,T+1):
    N = int(input())
    ori_list = list(input())
    num_list = []
    for stuff in ori_list:
        if stuff.isnumeric():
            num_list += [int(stuff)]
    ans = sum(num_list)
    print(f'#{case_num} {ans}')



