# BOJ. 17069. 파이프 옮기기 2
# 설계 의도: 그냥 약간 어려운 DP네요. DP 치고는 깔끔하게 떨어집니다.
# 1. 내가 있는 지점이 어떤 모양의 끝 점인지를 알면 된다.
# 2. 3가지 값을 각 DP 좌표에 배정해주고 각각이 가로, 대각선, 세로를 의미하게 한다.
# 개선점:
# 1. 더 빠르게 가능한가? 일단 36ms 인데..
import sys
input = sys.stdin.readline
N = int(input())
board = [[0]*(N+1)]
for get_line in range(N):
    board += [[0] + list(map(int, input().split()))]

# DP는 세 값을 가지고 간다. 가로, 좌상 대각선, 세로.
DP = [[[0, 0, 0] for i in range(N+1)] for j in range(N+1)]
DP[1][2][0] = 1
for first_dp in range(3, N+1):
    if board[1][first_dp] == 0:
        DP[1][first_dp][0] = DP[1][first_dp-1][0]


for x in range(2, N+1):
    for y in range(2, N+1):
        if board[x][y] == 0:
            DP[x][y][0] = DP[x][y-1][0] + DP[x][y-1][1]
            DP[x][y][2] = DP[x - 1][y][2] + DP[x - 1][y][1]
            if board[x - 1][y] == 0 and board[x][y - 1] == 0:
                DP[x][y][1] = DP[x - 1][y - 1][0] + DP[x - 1][y - 1][1] + DP[x - 1][y - 1][2]
print(sum(DP[N][N]))

