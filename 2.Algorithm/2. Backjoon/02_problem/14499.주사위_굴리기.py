# BOJ.
# 설계 의도: 주사위의 아래눈을 알면 위의 눈을 알 수 있으므로 위의 눈 생략.
# 0. 이어서, 각 사이드 의 값들을 넣어놓고 direction과 매칭
# 개선점:
# 다른게 아니라, 실제 주사위를 기반으로 돌려보고 있었는데, 실제 주사위랑 제시된 주사위가 다른 모양이었다...

import sys
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
direction_dict = {0:1, 1:0, 2:3, 3:2}
N, M, X, Y, K = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
direction_list = list(map(int, sys.stdin.readline().rstrip().split()))
dice_up = 0
dice_eye = 0
dice_control = [0, 0, 0, 0]
for rolling in range(K):
    direction = direction_list[rolling] - 1
    X = int(X) + dx[direction]
    Y = int(Y) + dy[direction]

    if X < 0 or X >= N or Y < 0 or Y >= M:
        X -= dx[direction]
        Y -= dy[direction]

    else:
        dice_up, dice_eye, dice_control[direction], dice_control[direction_dict[direction]]\
            = dice_control[direction_dict[direction]], dice_control[direction], dice_up, dice_eye

        if board[X][Y] == 0:
            board[X][Y] = int(dice_eye)
        else:
            dice_eye = int(board[X][Y])
            board[X][Y] = 0
        print(dice_up)

