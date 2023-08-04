# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

def count_stair_numbers(N):
    MOD = 1000000000
    dp = [[[0 for _ in range(1024)] for _ in range(10)] for __ in range(N + 1)]

    # 초기값 설정: 길이가 1인 계단수는 1개씩 있다.
    for i in range(1, 10):
        dp[1][i][1 << i] = 1

    # 2부터 N까지
    for i in range(2, N + 1):
        for j in range(10):
            for k in range(1024):
                # 맨 끝자리가 0인 경우 (1로만 이동 가능)
                if j == 0:
                    dp[i][j][k | (1 << j)] += dp[i - 1][1][k]
                    dp[i][j][k | (1 << j)] %= MOD
                # 맨 끝자리가 9인 경우 (8로만 이동 가능)
                elif j == 9:
                    dp[i][j][k | (1 << j)] += dp[i - 1][8][k]
                    dp[i][j][k | (1 << j)] %= MOD
                # 그 외의 경우 (양 옆으로 이동 가능)
                else:
                    dp[i][j][k | (1 << j)] += dp[i - 1][j - 1][k] + dp[i - 1][j + 1][k]
                    dp[i][j][k | (1 << j)] %= MOD

    # 결과 출력
    result = sum(dp[N][i][1023] for i in range(10)) % MOD
    return result


N = int(input())
print(count_stair_numbers(N))
