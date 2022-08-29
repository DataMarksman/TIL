# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T + 1):
    act_list = list(map(str, input().split()))
    N = int(act_list[0])
    entire_count = 0
    blue_count = 0
    orange_count = 0
    gauge = 0
    flag = True if act_list[1] == 'B' else False
    for acting in range(N):
        actor = act_list[acting*2 + 1]
        action = int(act_list[acting*2 + 2])
        if actor == 'B': #
            if flag:
                if gauge >= abs(action - blue_count)
                    entire_count += abs(action - blue_count) + 1
                    blue_count = action
                    gauge = gauge - abs(action - blue_count) + 1
                else:
                    entire_count += abs(action - blue_count) + 1
                    blue_count = action
                    gauge = abs(action - blue_count) + 1

        elif actor == 'O':


    print(f'#{case_num} {ans}')