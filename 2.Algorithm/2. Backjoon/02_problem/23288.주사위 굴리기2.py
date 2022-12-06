# BOJ.
# 설계 의도: 주사위의 아래눈을 알면 위의 눈을 알 수 있으므로 위의 눈 생략.
# 0. 이어서, 각 사이드 의 값들을 넣어놓고 direction과 매칭
# 개선점:
# 다른게 아니라, 실제 주사위를 기반으로 돌려보고 있었는데, 실제 주사위랑 제시된 주사위가 다른 모양이었다...

import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# 주사위 아래면 > 좌표위의 값 이면 정방향, 아니라면 반대, 같으면 그대로
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
X = 0
Y = 0
ans = 0
direction = 0
dice_eye = 6
dice_control = [3, 5, 4, 2]
visited_dict = {}
for rolling in range(K):
    X += dx[direction]
    Y += dy[direction]

    if X < 0 or X >= N or Y < 0 or Y >= M:
        X -= (dx[direction] * 2)
        Y -= (dy[direction] * 2)
        direction = (direction + 2) % 4
    get_number = dice_control[direction]
    dice_control[direction] = 7 - dice_eye
    dice_control[(direction + 2) % 4] = dice_eye
    dice_eye = get_number

    if visited_dict.get((X, Y)):
        ans += visited_dict[(X, Y)]
    else:
        temp_visited = {(X, Y), }
        stack = {(X, Y), }
        temp_board_eyes = board[X][Y]
        while stack:
            x, y = stack.pop()
            for direct in range(4):
                px = x + dx[direct]
                py = y + dy[direct]
                if 0 <= px < N and 0 <= py < M and board[px][py] == temp_board_eyes and (px, py) not in temp_visited:
                    temp_visited.add((px, py))
                    stack.add((px, py))
        temp_score = int(len(temp_visited)) * temp_board_eyes
        ans += temp_score
        while temp_visited:
            visited_dict[tuple(temp_visited.pop())] = temp_score

    if dice_eye > board[X][Y]:
        direction = (direction + 1) % 4
    elif dice_eye < board[X][Y]:
        direction = (direction + 3) % 4

print(ans)

