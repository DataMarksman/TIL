# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# input = sys.stdin.readline
#
# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]
#
#
# N, M, T = map(int, input().split())
# board = [[set()] * N for _ in range(N)]
# pick_set = set()
# for magics in range(M):
#     r, c, m, s, d = map(int, input().split())
#     pick_set.add((r-1, c-1, m, s, d, 0))
# ans = 0
# turn = 0
# while turn < T:
#     turn += 1
#     idx1 = 0
#     while pick_set:
#         x, y, fireballs, speed, D, turns = pick_set.pop()
#         tx = (x + (dx[D] * speed)) % N if x + (dx[D] * speed) >= 0 else (N - (abs(x + (dx[D] * speed)) % N)) % N
#         ty = (y + (dy[D] * speed)) % N if y + (dy[D] * speed) >= 0 else (N - (abs(y + (dy[D] * speed)) % N)) % N
#         board[tx][ty].add((fireballs, speed, D, turns))
#     for xx in range(N):
#         for yy in range(N):
#             if len(board[xx][yy]) >= 2:
#                 length = len(board[xx][yy])
#                 FB, SP, DS, turns = board[xx][yy].pop()
#                 fire_magics = int(FB)
#                 speed_count = int(SP)
#                 direction_odd = int(DS) % 2
#                 direction_flag = True
#                 while board[xx][yy]:
#                     FB, SP, DS, turns = board[xx][yy].pop()
#                     fire_magics += FB
#                     speed_count += SP
#                     if direction_odd != int(DS) % 2:
#                         direction_flag = False
#                 direction_plus = 0 if direction_flag else 1
#                 if fire_magics > 4:
#                     new_speed = speed_count // length
#                     for distribute in range(4):
#                         new_dist = (distribute*2)+direction_plus
#                         # px = (xx+dx[new_dist]) % N if xx+dx[new_dist] >= 0 \
#                         #     else (N - (abs(xx + (dy[new_dist] * new_speed)) % N)) % N
#                         # py = (yy + dx[new_dist]) % N if yy + dx[new_dist] >= 0 \
#                         #     else (N - (abs(yy + (dy[new_dist] * new_speed)) % N)) % N
#                         pick_set.add((xx, yy, fire_magics//5, new_speed, new_dist, turn))
#             elif board[xx][yy]:
#                 FB, SP, DS, turns = board[xx][yy].pop()
#                 pick_set.add((xx, yy, FB, SP, DS, turns))
# while pick_set:
#     ans += pick_set.pop()[2]
# print(ans)

import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


N, M, T = map(int, input().split())
board = [[[]] * N for _ in range(N)]
pick_set = []
for magics in range(M):
    r, c, m, s, d = map(int, input().split())
    pick_set.append((r-1, c-1, m, s, d))
ans = 0
turn = 0
while turn < T:
    turn += 1
    while pick_set:
        x, y, fireballs, speed, D = pick_set.pop()
        tx = (x + (dx[D] * speed)) % N if x + (dx[D] * speed) >= 0 else (N - (abs(x + (dx[D] * speed)) % N)) % N
        ty = (y + (dy[D] * speed)) % N if y + (dy[D] * speed) >= 0 else (N - (abs(y + (dy[D] * speed)) % N)) % N
        board[tx][ty].append((fireballs, speed, D))
    for xx in range(N):
        for yy in range(N):
            if len(board[xx][yy]) >= 2:
                length = len(board[xx][yy])
                FB, SP, DS = board[xx][yy].pop()
                fire_magics = int(FB)
                speed_count = int(SP)
                direction_odd = int(DS) % 2
                direction_flag = True
                while board[xx][yy]:
                    FB, SP, DS = board[xx][yy].pop()
                    fire_magics += FB
                    speed_count += SP
                    if direction_odd != int(DS) % 2:
                        direction_flag = False
                direction_plus = 0 if direction_flag else 1
                if fire_magics > 4:
                    new_speed = speed_count // length
                    for distribute in range(4):
                        new_dist = (distribute*2)+direction_plus
                        # px = (xx+dx[new_dist]) % N if xx+dx[new_dist] >= 0 \
                        #     else (N - (abs(xx + (dy[new_dist] * new_speed)) % N)) % N
                        # py = (yy + dx[new_dist]) % N if yy + dx[new_dist] >= 0 \
                        #     else (N - (abs(yy + (dy[new_dist] * new_speed)) % N)) % N
                        pick_set.append((xx, yy, fire_magics//5, new_speed, new_dist))
            elif board[xx][yy]:
                FB, SP, DS = board[xx][yy].pop()
                pick_set.append((xx, yy, FB, SP, DS))
while pick_set:
    ans += pick_set.pop()[2]
print(ans)