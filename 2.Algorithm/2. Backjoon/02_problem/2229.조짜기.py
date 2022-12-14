# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
N = int(input())
DP = [[0,0] for _ in range(N+1)]
board = list(map(int, input().split()))
if N == 1:
    print(0)
elif N == 2:
    print(abs(board[0]-board[1]))
else:
    DP[1][1] = abs(board[1]-board[0])
    for x in range(2, N):
        DP[x][0] = max(max(DP[x-1]), max(DP[x-2]))
        DP[x][1] = max(max(DP[x-1][0], DP[x-2]) + abs(board[x]-board[x-1]), DP[x-2][0] + abs(board[x]-board[x-2]))
    print(max(max(DP[N-1]), max(DP[N-2])))

