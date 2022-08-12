# 5432. 쇠막대기 자르기

T = int(input())
for case_num in range(1, T+1):
    bar_list = list(str(input()))
    count_bar = 0
    ans_count = 0
    for check in range(len(bar_list)):
        if (bar_list[check] == '(') and (bar_list[check+1] != ')'):
            count_bar += 1
        elif (bar_list[check] == ')') and (bar_list[check-1] != '('):
            count_bar -= 1
            ans_count += 1
        elif (bar_list[check] == '(') and (bar_list[check+1] == ')'):
            ans_count += count_bar
    print(f'#{case_num} {ans_count}')
