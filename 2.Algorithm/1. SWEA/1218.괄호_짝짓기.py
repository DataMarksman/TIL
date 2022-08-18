# 1218. 괄호 짝짓기
in_case = ['(', '[', '{', '<']
out_case = [')', ']', '}', '>']

for tc in range(1, 11):
    N = int(input())
    check_list = list((input()))
    stack = [0]*(N+1)
    top = -1
    flag = True
    for idx in range(N):
        if check_list[idx] in in_case:
            top += 1
            stack[top] = check_list[idx]
        elif check_list[idx] in out_case:
            if stack[top] == in_case[out_case.index(check_list[idx])]:
                top -= 1
            else:
                flag = False
                break
    print(f'#{tc} {1 if (top == -1) and (flag is True) else 0}')

