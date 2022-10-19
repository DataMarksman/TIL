# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
direction_dict = {1:3, 2:1, 3:0, 4:2}

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magic_Q = []
ans = 0
X, Y = N//2, N//2
balls = 0
D = 1
while True:
    for direct in range(3, 7):
        PX = X + dx[(D + direct) % 4]
        PY = Y + dy[(D + direct) % 4]
        if 0 <= PX < N and 0 <= PY < N:
            if board[PX][PY] != 0:
                D = (D + direct) % 4
                magic_Q.append(board[PX][PY])
                board[PX][PY] = 0
                X = PX
                Y = PY
                balls += 1
                break
    else:
        break
for turn in range(K):
    direction, length = map(int, input().split())
    direction = direction_dict[direction]
    distance = 0
    for destroy in range(length):
        distance += 4*(2*destroy)
        if distance < len(magic_Q):
            ans += magic_Q.pop(distance + direction*((destroy+1)*2))
        else:
            break

    flag = True
    while flag:
        value = -1
        count = 0
        temp_idx = 0
        idx = 0
        flag = False
        for checking in range(len(magic_Q)):
            if magic_Q[idx] != value:
                if count >= 4:
                    flag = True
                    for popping in range(count):
                        ans += magic_Q.pop(temp_idx)
                    idx = int(temp_idx)
                    value = magic_Q[idx]
                    count = 1
                    idx += 1
                else:
                    value = magic_Q[idx]
                    temp_idx = idx
                    count = 1
                    idx += 1
            else:
                count += 1
                idx += 1
        if count >= 4:
            flag = True
            for popping in range(count):
                ans += magic_Q.pop()
    New_Q = []
    refill_count = 0
    refill_value = 0
    for filling in range(len(magic_Q)):
        if magic_Q[filling] != refill_value and refill_count:
            New_Q.append(refill_count)
            New_Q.append(refill_value)
            refill_count = 1
            refill_value = magic_Q[filling]
        else:
            refill_count += 1
            refill_value = magic_Q[filling]
    if refill_count >= 1:
        New_Q.append(refill_count)
        New_Q.append(refill_value)

    if len(New_Q) >= balls:
        magic_Q = New_Q[:balls]
    else:
        if New_Q:
            while len(New_Q) < balls:
                New_Q += New_Q
            magic_Q = New_Q[:balls]
        else:
            break
print(ans)




