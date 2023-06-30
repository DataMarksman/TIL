# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip('\r\n')


def steal_treasure(t, treasure_data):
    for _ in range(t):
        n, w = map(int, input().split())
        enemy_data = list(map(int, input().split())) + list(map(int, input().split()))

        dp = [[[float('inf')] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    dp[i][j][1] = enemy_data[i - 1]
                else:
                    dp[i][j][1] = max(dp[i][j][1], enemy_data[i - 1] + enemy_data[j - 1])

        for k in range(2, n + 1):
            for i in range(1, n + 1):
                j = i + k - 1
                if j > n:
                    break
                for m in range(1, w + 1):
                    for x in range(i, j):
                        dp[i][j][m] = min(dp[i][j][m], dp[i][x][m - 1] + dp[x + 1][j][1])

        print(dp[1][n][w])


# 예시 입력

