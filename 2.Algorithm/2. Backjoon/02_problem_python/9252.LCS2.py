# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
def lcs(X, Y):
    global answer
    # 함수 lcs는 두 문자열 X와 Y를 인자로 받아서 최장 공통 부분 수열을 찾는 함수입니다.

    m = len(X)
    n = len(Y)
    # X와 Y의 길이를 각각 m과 n에 저장합니다.

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # dp 테이블을 초기화합니다. dp[i][j]는 X의 처음 i개 문자와 Y의 처음 j개 문자의 최장 공통 부분 수열의 길이를 저장합니다.

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # dp 테이블을 채웁니다. X의 i번째 문자와 Y의 j번째 문자가 같으면 dp[i][j]는 dp[i - 1][j - 1] + 1이 되고, 그렇지 않으면 dp[i - 1][j]와 dp[i][j - 1] 중 큰 값이 dp[i][j]가 됩니다. 이렇게 dp 테이블을 채워가는 과정이 바로 동적 프로그래밍입니다.

    LCS = ""
    i = m
    j = n

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            LCS = X[i - 1] + LCS
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    # dp 테이블을 역으로 추적하면서 최장 공통 부분 수열을 생성합니다. 이것이 바로 동적 프로그래밍으로 문제를 해결하는 방식의 일반적인 방법 중 하나입니다.

    return LCS

A = input()
B = input()
# 두 문자열 A와 B를 입력 받습니다.

answer = lcs(A,B)
# A와 B의 최장 공통 부분 수열을 찾아서 answer에 저장합니다.

if len(answer) >= 1:
    print(len(answer))
    print(answer)
else:
    print(0)


"""
참고용 LCSubstr, 즉 최장 공통 부분 문자열 코드

import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

def LCSubstr(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n+1) for _ in range(m+1)]
    max_length = 0
    max_i = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    max_i = i
            else:
                dp[i][j] = 0

    return X[max_i-max_length: max_i]

A = input()
B = input()
answer = LCSubstr(A, B)
if len(answer) >= 1:
    print(len(answer))
    print(answer)
else:
    print(0)

이렇게 작성하면, 비교 문자열이 다를 경우, dp[i][j] = 0 으로 길이를 초기화 시킨다.
즉, 연속성이 보장되는 최장 연속 문자열 코드로 구현할 수 있다.
"""