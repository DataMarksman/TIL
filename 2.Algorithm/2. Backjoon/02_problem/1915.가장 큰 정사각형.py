# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]


DP = [[0]*M for _ in range(N)]
max_size = 0
for first_x in range(M):
    if int(board[0][first_x]) > 0:
        DP[0][first_x] = 1
for x in range(1, N):
    for y in range(M):
        if board[x][y] != '0':
            DP[x][y] = DP[x - 1][y] + 1
            if DP[x][y] > max_size:
                for check in range(DP[x][y]):
                    if y - check >= 0:
                        if DP[x][y] > DP[x][y-check]:
                            break
                    else:
                        break
                else:
                    max_size = int(DP[x][y])
for printing in range(N):
    print(DP[printing])
print(max_size**2)





"""
00100
01010
10001
01010
00100




"""