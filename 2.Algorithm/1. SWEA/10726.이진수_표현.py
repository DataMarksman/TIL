# SWEA. 10726 이진수 표현
# 설계 목적:
# 1.
# 개선점:
# 1. 이진수로 바꾼 다음에 앞에 b0 생기는거 커버 해야합니다~ 그거 빼먹으니까 1만개 중 9997개 맞음.

T = int(input())
for case_num in range(1, T + 1):
    N, M = tuple(map(int, input().split()))
    check = list(str(bin(M)))[2:][::-1][:N]
    print(check)
    if len(check) < N or '0' in check:
        print(f'#{case_num} OFF')
    else:
        print(f'#{case_num} ON')