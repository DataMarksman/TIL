# 4866. 괄호 검사
# 개선점: 스택은 먼저 만들어놓고 쓰자....
in_case = ['(', '{']
out_case = [')', '}']
T = int(input())
for tc in range(1, T+1):
    check_list = list((input()))
    stack = [0]*50
    top = -1
    flag = True
    for factors in range(len(check_list)):
        if top < -1:
            flag = False
            break
        else:
            if check_list[factors] in in_case:
                top += 1
                stack[top] = check_list[factors]
            elif check_list[factors] in out_case:
                if stack[top] == in_case[out_case.index(check_list[factors])]:
                    top -= 1
                else:
                    flag = False
                    break

    if (top == -1) and (flag is True):
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')
