# BOJ. 2638 치즈
# 설계 의도: 한번은 묵히고, 묵혔던건 꺼내고. 더블 체크 세트
#
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N, M = map(int, input().split())
visited = set()
board = [list(map(int, input().split())) for _ in range(N)]


time = 0
Queue = {(0,0),}
while len(visited) < M*N:
    cheese_set = set()
    melting_set = set()
    close_set = set()
    while Queue:
        X, Y = Queue.pop()
        for direction in range(4):
            PX = X + dx[direction]
            PY = Y + dy[direction]
            if 0 <= PX < N and 0 <= PY < M and (PX, PY) not in visited:
                if board[PX][PY]:
                    close_set.add((X,Y))
                    if (PX, PY) in cheese_set:
                        melting_set.add((PX, PY))
                    else:
                        cheese_set.add((PX, PY))
                else:
                    visited.add((PX, PY))
                    Queue.add((PX, PY))
    while melting_set:
        R, C = melting_set.pop()
        visited.add((R, C))
        Queue.add((R, C))
    Queue |= close_set
    time += 1
print(time)

