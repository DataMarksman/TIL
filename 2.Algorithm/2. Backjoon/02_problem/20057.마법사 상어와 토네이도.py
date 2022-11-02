# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def blow(index, direction):
    global ans
    global board
    X, Y = index
    target = int(board[X][Y])
    remain = int(target)
    board[X][Y] = 0
    PX = X - dx[direction]
    PY = Y - dy[direction]

    # 일단 뒤로 한칸 가서 위 아래 보기.
    PX_UP = PX + dx[(direction+3)%4]
    PY_UP = PY + dy[(direction+3)%4]
    if 0 <= PX_UP < N and 0 <= PY_UP < N:
        board[PX_UP][PY_UP] += int(target*0.01)
    else:
        ans += int(target*0.01)
    remain -= int(target*0.01)

    PX_Down = PX + dx[(direction+1)%4]
    PY_Down = PY + dy[(direction+1)%4]
    if 0 <= PX_Down < N and 0 <= PY_Down < N:
        board[PX_Down][PY_Down] += int(target*0.01)
    else:
        ans += int(target*0.01)
    remain -= int(target * 0.01)

    # 다시 한칸 앞으로 와서 위 두칸 아래 두칸 보기
    PX = int(X)
    PY = int(Y)
    PX_UP = PX + dx[(direction + 3) % 4]
    PY_UP = PY + dy[(direction + 3) % 4]
    if 0 <= PX_UP < N and 0 <= PY_UP < N:
        board[PX_UP][PY_UP] += int(target * 0.07)
    else:
        ans += int(target * 0.07)
    remain -= int(target * 0.07)

    PX_UP += dx[(direction + 3) % 4]
    PY_UP += dy[(direction + 3) % 4]
    if 0 <= PX_UP < N and 0 <= PY_UP < N:
        board[PX_UP][PY_UP] += int(target * 0.02)
    else:
        ans += int(target * 0.02)
    remain -= int(target * 0.02)

    PX_Down = PX + dx[(direction + 1) % 4]
    PY_Down = PY + dy[(direction + 1) % 4]
    if 0 <= PX_Down < N and 0 <= PY_Down < N:
        board[PX_Down][PY_Down] += int(target * 0.07)
    else:
        ans += int(target * 0.07)
    remain -= int(target * 0.07)

    PX_Down += dx[(direction + 1) % 4]
    PY_Down += dy[(direction + 1) % 4]
    if 0 <= PX_Down < N and 0 <= PY_Down < N:
        board[PX_Down][PY_Down] += int(target * 0.02)
    else:
        ans += int(target * 0.02)
    remain -= int(target * 0.02)

    # 한칸 앞으로 가서 위 아래로 10% 짜리 보기
    PX = X + dx[direction]
    PY = Y + dy[direction]

    PX_UP = PX + dx[(direction + 3) % 4]
    PY_UP = PY + dy[(direction + 3) % 4]
    if  0 <= PX_UP < N and 0 <= PY_UP < N:
        board[PX_UP][PY_UP] += int(target * 0.1)
    else:
        ans += int(target * 0.1)
    remain -= int(target * 0.1)

    PX_Down = PX + dx[(direction + 1) % 4]
    PY_Down = PY + dy[(direction + 1) % 4]
    if 0 <= PX_Down < N and 0 <= PY_Down < N:
        board[PX_Down][PY_Down] += int(target * 0.1)
    else:
        ans += int(target * 0.1)
    remain -= int(target * 0.1)

    # 마지막 5% 짜리
    PX += dx[direction]
    PY += dy[direction]
    if 0 <= PX < N and 0 <= PY < N:
        board[PX][PY] += int(target * 0.05)
    else:
        ans += int(target * 0.05)
    remain -= int(target * 0.05)

    # 이제 알파로 돌아와서 나머지 정산
    PX -= dx[direction]
    PY -= dy[direction]
    if 0 <= PX < N and 0 <= PY < N:
        board[PX][PY] += int(remain)
    else:
        ans += int(remain)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
idx_X = N//2
idx_Y = N//2
length = 2
D = 0
flag = True
while flag:
    for turns in range((length//2)):
        idx_X += dx[D]
        idx_Y += dy[D]
        if idx_X == 0 and idx_Y < 0:
            flag = False
            break
        else:
            blow((idx_X, idx_Y), D)
    D = (D + 1)%4
    length += 1
print(ans)

