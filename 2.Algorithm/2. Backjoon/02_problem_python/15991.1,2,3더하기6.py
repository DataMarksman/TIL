# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    count = 0
    if N % 2 == 1:
        alpha = N // 2
        for i in range(alpha):
            for j in range((alpha//2)+1):
                for k in range((alpha//3)+1):
                    if i + j*2 + k*3 == alpha:
                        count += 1*(i if i > 0 else 1)*(j if j > 0 else 1)*(k if k > 0 else 1)

    elif N % 2 == 0:
        beta = N // 2
    print(count)

