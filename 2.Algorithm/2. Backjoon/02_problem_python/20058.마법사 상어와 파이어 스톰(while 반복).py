# BOJ. 20058. 마법사 상어와 파이어 스톰
# 설계 의도: 원래는 재귀로 함수 기능 분절해서 돌렸는데... 채점 케이스가 미쳐서 main에 합쳐버림
# 1. 달팽이 돌듯이 뱅글뱅글 돌려줄 겁니다.
# 2. 그 이후에 각자 돌면서 사방 탐색으로 마이너스 해주고
# 3. 그 다음 카운팅 하고 BFS해서 출력
# 개선점:
# 1. 시간... 메모리... python3로 통과 못해서 미안하다!!!!!!!

from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
N = int(2**N)
board = [list(map(int, input().split())) for _ in range(N)]
magic_Q = deque(map(int, input().split()))
for spelling in range(M):
    wide = 2**(magic_Q.popleft())
    x_idx = 0
    y_idx = 0
    if wide > 1:
        while True:
            inner = 0
            for x in range(x_idx, x_idx + (wide // 2)):
                length = wide - 2 * inner
                step = 0
                for y in range(y_idx + inner, y_idx + inner + length - 1):
                    board[x][y], board[x + step][y_idx + inner + length - 1], board[x + length - 1][
                        y_idx + inner + length - 1 - step], board[x + length - 1 - step][y_idx + inner] = \
                        board[x + length - 1 - step][y_idx + inner], board[x][y], board[x + step][
                            y_idx + inner + length - 1], board[x + length - 1][y_idx + inner + length - 1 - step]
                    step += 1
                inner += 1
            if y_idx + wide >= N:
                if x_idx + wide < N:
                    x_idx += wide
                    y_idx = 0
                else:
                    break
            else:
                y_idx += wide
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
    else:
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