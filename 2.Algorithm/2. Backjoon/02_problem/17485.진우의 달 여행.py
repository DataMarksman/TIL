# BOJ. 17485. 진우의 달 여행
# 설계 의도: DP는 DP다. 그냥 각 좌표에 어디서 왔는지 출신을 넣어주면 된다.
# 개선점:
# 1. INF가 시간을 많이 먹나?
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
board = []
for get_line in range(N):
    board += [[INF] + list(map(int, input().split())) + [INF]]

DP = [[[0, 0, 0] for i in range(M+2)] for j in range(N)]
for first_dp in range(1, M+1):
    DP[1][first_dp][0] = board[1][first_dp] + board[0][first_dp - 1]
    DP[1][first_dp][1] = board[1][first_dp] + board[0][first_dp]
    DP[1][first_dp][2] = board[1][first_dp] + board[0][first_dp + 1]
for x in range(2, N):
    DP[x][1][0] = INF
    DP[x][1][1] = board[x][1] + min(DP[x - 1][1][0], DP[x - 1][1][2])
    DP[x][1][2] = board[x][1] + min(DP[x - 1][2][:2])
    DP[x][M][0] = board[x][M] + min(DP[x - 1][M - 1][1:])
    DP[x][M][1] = board[x][M] + min(DP[x - 1][M][0], DP[x - 1][M][2])
    DP[x][M][2] = INF
    for y in range(2, M):
        DP[x][y][0] = board[x][y] + min(DP[x - 1][y - 1][1:])
        DP[x][y][1] = board[x][y] + min(DP[x - 1][y][0], DP[x - 1][y][2])
        DP[x][y][2] = board[x][y] + min(DP[x - 1][y + 1][:2])
ans = INF
for printing in range(1, M+1):
    ans = min(min(DP[N-1][printing]), ans)
print(ans)
