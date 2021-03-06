'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''


stack = []
def push(input(x)):
    stack = stack + int(x)

def pop():
    print(stack[len(stack)])
    pop(stack[len(stack)])

def size():
    print(len(stack()))

def empty():
    if len(stack) == False:
        print(1)
    else:
        print(0)

def top():
    if len(stack) != False:
        print(int(stack[len(stack)]))
    else:
        print(int(-1))
