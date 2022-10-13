# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def finding(start_idx):
    pick_set = {start_idx, }
    temp_visited = set()

    while pick_set:
        pick = pick_set.pop()

def gravity():

    for fx in range(N-1, 1, -1):
        for fy in range(N):
            if board[fx][fy] < -1:
                board[fx][fy], board[fx-1][fy] =


def spinning():
    global board
    for spin in range((N+1)//2):
        for c in range((N-1)-spin, 1+spin, -1):
            board[(N-1) - c][c], board[(N-1) - c][(N-1) - c] =


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
while True:
    visited = set()
    for x in range(N - 1, 0, -1):
        for y in range(N - 1, 0, -1):
            if board[x][y] > 0 and (x, y) not in temp_visited:
