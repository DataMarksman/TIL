# BOJ. 21922. 학부연구생 민상
# 설계 의도: 조건에 맞는 실행
# 개선점:
# 1. 시간 엄청 오래 걸리네... 최적화를 하고 싶지만, 할 일이 많아서 패스하겠습니다.
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]   # 상 우 하 좌
dy = [0, 1, 0, -1]   # 상 우 하 좌
direction_dict = {(0, 1): 0, (0, 2): 2, (0, 3): 1, (0, 4): 3,    # 세로 칸막이
                  (1, 1): 3, (1, 2): 1, (1, 3): 0, (1, 4): 2,   # 가로 칸막이
                  (2, 1): 2, (2, 2): 0, (2, 3): 3, (2, 4): 1,  # 좌하우상 대각선
                  (3, 1): 1, (3, 2): 3, (3, 3): 2, (3, 4): 0}  # 좌상우하 대각선


N, M = map(int, input().split())
AC_set = set()
block_set = [set() for _ in range(5)]
ans_set = set()
board = []
for put_in in range(N):
    line = list(map(int, input().split()))
    for start_pick in range(M):
        if line[start_pick] == 9:
            AC_set.add((put_in, start_pick))
    board += [line]

start_set = set(AC_set)
while start_set:
    X, Y = start_set.pop()
    for direction in range(4):
        PX = X + dx[direction]
        PY = Y + dy[direction]
        D = int(direction)
        while True:
            if (PX, PY) in AC_set:
                break
            elif 0 <= PX < N and 0 <= PY < M:
                ans_set.add((PX, PY))
                if board[PX][PY] >= 1:
                    D = direction_dict[(D, board[PX][PY])]
                PX += dx[D]
                PY += dy[D]
            else:
                break
ans = len(AC_set | ans_set)
print(ans)