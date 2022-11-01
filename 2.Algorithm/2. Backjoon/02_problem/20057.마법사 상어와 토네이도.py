# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def blow(index, direction):
    X, Y = index
    target = float(board[X][Y])
    PX = X + dx[direction]
    PY = Y + dy[direction]
    board[PX][PY]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

idx = ((N+1)//2, (N+1)//2)
length = 2
D = 0
while idx != (0, 0):
    for turns in range((length//2)):
        idx = (idx[0]+dx[D], idx[1]+dy[D])

    D += 1
    length += 1










