print("자, 스택을 구현해봅시다.")
print("먼저 넣어줄 값들을 입력해봅시다.")
print("아무것도 입력하지 않고 엔터를 누르면 뽑기로 넘어갑니다.")
stack = []
while True:
    stack.append(input('입력값: '))
    if stack[len(stack)-1] == '':
        del stack[len(stack)-1]
        print(f'현재까지 입력된 스택: ', *stack)
        break
    print(f'현재 입력된 스택값 목록: ', *stack)
print("이제 값들을 한개씩 빼주도록 합시다.")
print(f'처음으로 빠질 값은 가장 오른쪽, 즉 최근에 넣은 {stack.pop()}')
while len(stack) > 0:
    print(f'이번에 빼줄 값은: {stack.pop()}')
    print(f'남은 스택 값 목록: ', *stack)
print("이렇게 스택은 후입 선출, 즉 나중에 넣은 것이 먼저 나옵니다.")