# 10163 색종이
# 설계 의도: N개의 박스를 그린다면, N번 탐색하면서 이전에 그려놨던 자취를 덮어쓰자.
N = int(input())
box_list = [list(map(int, input().split())) for _ in range(N)]
board = [[0]*1002 for _ in range(1002)]              # 혹시 몰라서 1002로 설정
ans_list = [0]*N                                     # 박스별 카운팅(=넓이) 저장소
for idx in range(N):                                 # 상자 순서대로 그리기
    dx_s = box_list[idx][0]                          # x 좌표 시작점
    dx_e = box_list[idx][0] + box_list[idx][2]       # x 좌표 끝점
    dy_s = box_list[idx][1]                          # y 좌표 시작점
    dy_e = box_list[idx][1] + box_list[idx][3]       # y 좌표 끝점
    for dx in range(dx_s, dx_e):                     # 박스 x 좌표 순회 반복문
        for dy in range(dy_s, dy_e):                 # 박스 y 좌표 순회 반복문
            if board[dx][dy] == 0:                   # 해당 좌표가 비어있으면
                board[dx][dy] = (idx + 1)            # 현재 박스 발자취 덮어쓰기
                ans_list[idx] += 1                   # 현재 박스의 카운트 +1
            elif board[dx][dy] != 0:                 # 이미 발자국 있으면
                ans_list[(board[dx][dy] - 1)] -= 1   # 이전 발자국 지우고, 해당 카운트 -1
                board[dx][dy] = (idx + 1)            # 현재 박스 발자취 덮어쓰기
                ans_list[idx] += 1                   # 현재 박스 카운팅 +1

for print_box in range(N):
    print(ans_list[print_box])