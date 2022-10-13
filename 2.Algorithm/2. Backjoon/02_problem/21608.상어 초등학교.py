# BOJ. 21608. 상어 초등학교
# 설계 의도: 조건에 맞는 실행

import sys
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def spotting(k, love):
    love = set(love)
    max_love = len(love & visited)
    love_count = -1
    empty_count = -1
    good_idx = (N, N)
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                temp_love = 0
                temp_empty = 0
                for direction in range(4):
                    px = x + dx[direction]
                    py = y + dy[direction]
                    if 0 <= px < N and 0 <= py < N:
                        if board[px][py] in love:
                            temp_love += 1
                        elif not board[px][py]:
                            temp_empty += 1
                if temp_love > love_count:
                    love_count = temp_love
                    empty_count = temp_empty
                    good_idx = (x, y)
                elif temp_love == love_count or temp_love == max_love:
                    if temp_empty > empty_count:
                        empty_count = temp_empty
                        good_idx = (x, y)
                        if max_love == love_count and empty_count == 4:
                            return good_idx
    return good_idx


N = int(input())
visited = set()
board = [[0]*N for _ in range(N)]
compare_set = [set() for c in range((N*N)+1)]
ans = 0
for cases in range(1, (N*N)+1):
    line = list(map(int, input().split()))
    visited.add(line[0])
    idx = spotting(line[0], set(line[1:]))
    board[idx[0]][idx[1]] = line[0]
    compare_set[line[0]] = set(line[1:])
for r in range(N):
    for c in range(N):
        pick = board[r][c]
        happiness = 0
        for direct in range(4):
            cx = r + dx[direct]
            cy = c + dy[direct]
            if 0 <= cx < N and 0 <= cy < N:
                if board[cx][cy] in compare_set[pick]:
                    happiness += 1
        if happiness >= 1:
            ans += 10**(happiness-1)
print(ans)