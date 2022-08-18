# 2005. 파스칼의 삼각형 (재귀 버전)
def pascal(n, k):  # 파스칼 함수를 만들거예요.
    global stack
    if n > k:
        p_stack = stack[:n]  # 그 스택값을
        for num in range(1, k):  # 가져온 값으로 원본에 구현해요
            stack[num] = p_stack[num - 1] + p_stack[num]
        print(*stack[:k+1])
        pascal(n, k + 1)


for case_num in range(1, int(input()) + 1):  # 바로 값을 받을거예요.. 파이써닉하게
    print(f'#{case_num}')  # 앞에 따로 떨어져 있어서 바로 출력
    stack = [1] * (int(input()))  # len(stack)으로 받아버려요.
    pascal(len(stack), 0)  # go go!
