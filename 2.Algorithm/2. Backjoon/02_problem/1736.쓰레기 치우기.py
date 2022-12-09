# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
N, M = map(int, sys.stdin.readline().split())
stop_count = 0
board = []
for input_line in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    stop_count += sum(line)
    board += [line]

stop_flag = True
visited = set()
ans = 0
start_X = 0
while len(visited) < stop_count:
    temp_X = int(start_X)
    start_Y = 0
    for X in range(start_X, N):
        for Y in range(start_Y, M):
            if board[X][Y] == 1:
                if (X, Y) in visited:
                    break
                else:
                    visited.add((X, Y))
                    if Y > start_Y:
                        start_Y = int(Y)
                    if start_X == temp_X and X != start_X:
                        temp_X = int(X)
    start_X = int(temp_X)
    ans += 1

print(ans)