# 클래스로 스택 직접 구현
class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.stack_component = [0]*self.size

    def push(self, item):
        self.top += 1
        if self.top == self.size:
            print('overflow')
        else:
            self.stack_component[self.top] = item

    def pop(self):
        self.top -= 1
        if self.top < 0:
            print('underflow')
        else:
            return self.stack_component[self.top+1]

    def show(self):
        print(self.stack_component[:self.top+1])


stack1 = Stack(10)
stack1.show()
# []

for i in range(5):
    stack1.push(i)
stack1.show()
# [0, 1, 2, 3, 4]

stack1.pop()
stack1.show()
# [0, 1, 2, 3]
