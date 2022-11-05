# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
import heapq
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# N, M, T = map(int, input().split())
# board = [[(0, 0, 0)]*N for _ in range(N)]
# for magics in range(M):
#     r, c, m, s, d = map(int, input().split())
#     pr = max(0, min(r + dx[d]*s, N-1))
#     pc = max(0, min(c + dy[d]*s, N-1))
#     board[pr][pc] = (board[pr][pc][0] + m, board[pr][pc][1] + s, board[pr][pc][2] + d)


N, M, T = map(int, input().split())
board = [[set()]*N for _ in range(N)]
for magics in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r][c].add((m, s, d))
turn = 0
while turn < T:
    turn += 1
    reboard = [[set()]*N for _ in range(N)]
    X, Y, M, S, D = heapq.heappop(idx_list)
    while idx_list:

        pick = heapq.heappop(idx_list)


