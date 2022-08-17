# 2005. 파스칼의 삼각형 (재귀 버전)
def pascal(k):                               # 파스칼 함수를 만들거예요.
    if len(stack) > k:                       # 재귀 브레이크 조건 여부 파악하고
        p_stack = stack[:len(stack)]         # 스택 원본 값을 참조해서
        for num in range(1, k):              # 파스칼을 원본에 구현해요
            stack[num] = pascal(k-1)[num - 1] + pascal(k-1)[num]
        pascal(k + 1)                        # k+1 해서 다시 돌려요
        print(*stack[:k+1])
        return stack[:k+1]                  # 출력하고


for case_num in range(1, int(input()) + 1):  # 바로 값을 받을거예요.. 파이써닉하게
    print(f'#{case_num}')                    # 앞에 따로 떨어져 있어서 바로 출력
    stack = [1] * (int(input()))             # len(stack)으로 받아버려요.
    pascal(0)                                # go go!
