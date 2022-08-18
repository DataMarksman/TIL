def fibo(n):                                # 피보나치 수열...
    if n <= 1:                              # 메모이즘을 사용하고
        return 1                            # memo[idx]로 위치값을 불려와도,
    ans = fibo(n-1) + fibo(n-2)             # idx값의 변동에 맞추어 값이 바뀌지 않음
    return ans


def fibo_check(cnt):                        # cnt 가 짝수 일 때에는 조건부 이하인지 확인
    global even_stack                       # cnt 가 홀수 일 때에는 조건부 이상인지 확인
    global odd_stack
    if cnt % 2 == 0:
        for k in range(len(odd_stack)):
            if odd_stack[k] <= ((fibo(cnt-1) / fibo(cnt)) * N):
                even_stack.append(odd_stack[k])
        else:
            if len(even_stack) >= 1:         # 조건에 맞는 값이 짝수 스택에 저장되면
                odd_stack = []               # 홀수 스택은 리셋
                return fibo_check(cnt + 1)   # cnt를 +1 하여 이번에는 홀수 루틴 적용
            else:
                return odd_stack             # 이번 루틴에서 걸러진 값이 없으면 이전 루틴 값 반환
    elif cnt % 2 != 0:
        for t in range(len(even_stack)):
            if even_stack[t] >= ((fibo(cnt-1) / fibo(cnt)) * N):
                odd_stack.append(even_stack[t])
        else:
            if len(odd_stack) >= 1:
                even_stack = []
                return fibo_check(cnt + 1)
            else:
                return even_stack


N = int(input())
even_stack = []
odd_stack = []
flag = True
for i in range(N//2, N):                       # 첫 시행용 N//2 ~ N 까지의 요소 채워두기
    even_stack += [i]
    odd_stack += [i]

print(fibo_check(3))