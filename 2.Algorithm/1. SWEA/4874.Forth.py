# SWEA. 4874 Forth
# 설계 목적: 후위 연산 계산 구현
# 1.
# 개선점:
# 1.


T = int(input())
for case_num in range(1, T+1):
    origin_list = list(input().split())
    stack = []
    ans = 0

    for pong in origin_list:
        if pong.isnumeric():
            stack.append(int(pong))
        elif len(stack) >= 2:
            if pong == '*':
                B = stack.pop()
                A = stack.pop()
                C = A*B
                stack.append(int(C))
            elif pong == '/':
                B = stack.pop()
                A = stack.pop()
                C = A//B
                stack.append(int(C))
            elif pong == '+':
                B = stack.pop()
                A = stack.pop()
                C = A+B
                stack.append(int(C))
            elif pong == '-':
                B = stack.pop()
                A = stack.pop()
                C = A-B
                stack.append(int(C))
        elif pong == '.':
            break
        else:
            ans = 'error'
            break
    if ans == 0 and len(stack) == 1:
        ans = stack.pop()
    else:
        ans = 'error'
    print(f'#{case_num} {ans}')





