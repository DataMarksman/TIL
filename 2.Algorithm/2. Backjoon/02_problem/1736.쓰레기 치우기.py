# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys


def bf(start_x, start_y):
    for R in range(start_x, N):
        for C in range(start_y, M):
            if board[R][C] == 1:
                if (R, C) not in visited:
                    visited.add((R, C))
                    if C > start_y:
                        start_y = int(C)
                else:
                    break


N, M = map(int, sys.stdin.readline().split())
stop_count = 0
board = []
for input_line in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    stop_count += sum(line)
    board += [line]

visited = set()
ans = 0
for X in range(N):
    if len(visited) < stop_count:
        for Y in range(M):
            if board[X][Y] == 1:
                if (X, Y) not in visited:
                    ans += 1
                    bf(X, Y)
                break
    else:
        break
print(ans)
