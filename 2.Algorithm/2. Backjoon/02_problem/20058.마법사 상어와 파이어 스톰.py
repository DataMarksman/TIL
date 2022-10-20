# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 돌리기 위한 재귀 함수
def spinning(x_idx, y_idx, width):
    inner = 0
    for x in range(x_idx, x_idx+(width//2)):
        length = width - 2*inner
        step = 0
        for y in range(y_idx+inner, y_idx+inner+length-1):
            board[x][y], board[x+step][y_idx+inner+length-1], board[x+length-1][y_idx+inner+length-1-step], board[x+length-1-step][y_idx+inner] = \
                board[x + length - 1 - step][y_idx + inner], board[x][y], board[x+step][y_idx+inner+length-1], board[x+length-1][y_idx+inner+length-1-step]
            step += 1
        inner += 1
    if y_idx + width >= N:
        if x_idx + width < N:
            x_idx += width
            y_idx = 0
        else:
            return
    else:
        y_idx += width
    spinning(x_idx, y_idx, width)


def checking():
    ice_set = set()
    for r in range(N):
        for c in range(N):
            ice_count = 0
            for direction in range(4):
                pr = r + dx[direction]
                pc = c + dy[direction]
                if 0 <= pr < N and 0 <= pc < N:
                    if board[pr][pc] > 0:
                        ice_count += 1
            if ice_count < 3 and board[r][c] > 0:
                ice_set.add((r, c))
    while ice_set:
        ix, iy = ice_set.pop()
        board[ix][iy] -= 1


N, M = map(int, input().split())
N = int(2**N)
board = [list(map(int, input().split())) for _ in range(N)]
magic_Q = deque(map(int, input().split()))
for spelling in range(M):
    wide = 2**(magic_Q.popleft())
    if wide > 1:
        spinning(0, 0, wide)
        checking()
    else:
        checking()
sum_ans = 0
max_size = 0
visited = set()
for xx in range(N):
    for yy in range(N):
        sum_ans += board[xx][yy]
        if board[xx][yy] != 0 and (xx, yy) not in visited:
            Q = {(xx, yy), }
            visited.add((xx, yy))
            size_count = 0
            while Q:
                size_count += 1
                rx, ry = Q.pop()
                for direction in range(4):
                    rr = rx + dx[direction]
                    cc = ry + dy[direction]
                    if 0 <= rr < N and 0 <= cc < N:
                        if board[rr][cc] != 0 and (rr, cc) not in visited:
                            Q.add((rr, cc))
                            visited.add((rr, cc))
            if size_count > max_size:
                max_size = int(size_count)
print(sum_ans)
print(max_size)