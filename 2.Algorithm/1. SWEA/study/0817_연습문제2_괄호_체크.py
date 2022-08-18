# 괄호 검사
# 괄호 쌍이 맞으면 1, 안맞으면 -1
for tc in range(1, int(input())+1):
    check_list = list(input())
    top = -1
    for factors in check_list:
        if factors == '(':
            top += 1
        if factors == ')':
            top -= 1
    if top == -1:
        ans = 1
    else:
        ans = -1
    print(f'#{tc} {ans}')

