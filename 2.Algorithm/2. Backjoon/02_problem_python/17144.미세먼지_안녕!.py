# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import copy
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

R, C, T = map(int, input().split())
height = int(R)
wide = int(C)
board = []
start = []
for put_in in range(R):
    lines = list(map(int, input().split()))
    if lines[0] == -1:
        start += [put_in]
    board += [lines]
turn_count = 0
while turn_count < T:
    re_board = [[0]*wide for _ in range(height)]
    for x in range(height):
        for y in range(wide):
            count_x = 0
            dust = board[x][y]
            if dust > 0:
                for direction in range(4):
                    px = x + dx[direction]
                    py = y + dy[direction]
                    if 0 <= px < height and 0 <= py < wide and board[px][py] != -1:
                        count_x += 1
                        re_board[px][py] += dust//5
                re_board[x][y] += (dust - (dust//5 * count_x))
    re_board[start[0]-1][0] = 0
    re_board[start[1]+1][0] = 0
    for rearrange_A in range(start[0]-1, 0, -1):
        re_board[rearrange_A][0] = int(re_board[rearrange_A - 1][0])
    for rearrange_B in range(start[1]+1, height-1):
        re_board[rearrange_B][0] = int(re_board[rearrange_B + 1][0])

    for rearrange_C in range(wide - 1):
        re_board[0][rearrange_C] = int(re_board[0][rearrange_C+1])
        re_board[height - 1][rearrange_C] = int(re_board[height - 1][rearrange_C+1])

    for rearrange_D in range(0, start[0]):
        re_board[rearrange_D][wide - 1] = int(re_board[rearrange_D + 1][wide - 1])
    for rearrange_E in range(height-1, start[1], -1):
        re_board[rearrange_E][wide - 1] = int(re_board[rearrange_E - 1][wide - 1])

    for rearrange_F in range(wide - 1, 1, -1):
        re_board[start[0]][rearrange_F] = int(re_board[start[0]][rearrange_F - 1])
        re_board[start[1]][rearrange_F] = int(re_board[start[1]][rearrange_F - 1])
    re_board[start[0]][1] = 0
    re_board[start[1]][1] = 0
    re_board[start[0]][0] = -1
    re_board[start[1]][0] = -1
    board = copy.deepcopy(re_board)
    turn_count += 1
ans = 2
for rx in range(height):
    for ry in range(wide):
        ans += board[rx][ry]
print(ans)

