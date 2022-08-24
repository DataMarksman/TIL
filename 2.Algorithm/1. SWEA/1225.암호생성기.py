# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")

T = 10
for tc in range(1, T+1):
    case_num = int(input())
    num_list = list(map(int, input().split()))
    flag = True
    while flag:
        for idx in range(1, 6):
            target = num_list.pop(0)
            target -= idx
            if target < 0:
                target = 0
                num_list.append(target)
                flag = False
                break
            else:
                num_list.append(target)

    print(f'#{case_num}', *num_list)
