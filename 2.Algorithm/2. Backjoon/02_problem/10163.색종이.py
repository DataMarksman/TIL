# 10163 색종이
N = int(input())
box_list = [list(map(int, input().split())) for _ in range(N)]
board = [[0]*1002 for _ in range(1002)]
ans_list = [0]*N
for idx in range(N):
    dx_s = box_list[idx][0]
    dx_e = box_list[idx][0] + box_list[idx][2]
    dy_s = box_list[idx][1]
    dy_e = box_list[idx][1] + box_list[idx][3]
    for dx in range(dx_s, dx_e):      # 박스 x 좌표 별
        for dy in range(dy_s, dy_e):  # 박스 y 좌표 별
            if board[dx][dy] == 0:
                board[dx][dy] = (idx + 1)                         # 현재 박스 발자취 덮어쓰기
                ans_list[idx] += 1
            elif board[dx][dy] != 0:
                ans_list[(board[dx][dy] - 1)] -= 1
                board[dx][dy] = (idx + 1)                         # 현재 박스 발자취 기록
                ans_list[idx] += 1

for print_box in range(N):
    print(ans_list[print_box])