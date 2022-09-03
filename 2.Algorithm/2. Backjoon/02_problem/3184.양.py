# BOJ. 3184 양
# 설계 의도:
# 1. 2차원 배열 전부 탐색하다가 # 아닌 곳 만나면 그 구간 델타 탐색으로 정찰
# 2. 지나간 곳들은 전부 #으로 마킹하고, 그 구간 내의 양/늑대 수 카운팅
# 3. 그 구간에 더이상 갈 수 있는 곳이 없으면 카운팅 비교해서 양/늑대 중 많은 쪽 반환
# 개선점:
import sys
sys.setrecursionlimit(10**6)
dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]


def battle(x, y):
    global board
    global wolf_remain
    global sheep_remain
    stack = set()
    stack.add((x, y))
    wolves = 0
    sheeps = 0
    while stack:
        position = stack.pop()
        kx = position[0]
        ky = position[1]
        if board[kx][ky] == 'o':
            board[kx][ky] = '#'
            sheeps += 1
        elif board[kx][ky] == 'v':
            board[kx][ky] = '#'
            wolves += 1
        for direction in range(4):
            px = kx + dx[direction]
            py = ky + dy[direction]
            if 0 <= px < N and 0 <= py < M:
                if board[px][py] == '.':
                    stack.add((px, py))
                    board[px][py] = '#'
                elif board[px][py] == 'o':
                    stack.add((px, py))
                    board[px][py] = '#'
                    sheeps += 1
                elif board[px][py] == 'v':
                    stack.add((px, py))
                    board[px][py] = '#'
                    wolves += 1
    if wolves >= sheeps:
        wolf_remain += wolves
    else:
        sheep_remain += sheeps


N, M = tuple(map(int, input().split()))
board = [list(input()) for _ in range(N)]
wolf_remain = 0
sheep_remain = 0
for r in range(N):
    for c in range(M):
        if board[r][c] != '#':
            battle(r, c)

print(sheep_remain, wolf_remain)