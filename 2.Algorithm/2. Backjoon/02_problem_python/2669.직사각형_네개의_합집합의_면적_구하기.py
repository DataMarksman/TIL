# 2669 직사각형 네개의 합집합의 면적 구하기

box_list = [list(map(int, input().split())) for _ in range(4)]
board = [[0]*101 for _ in range(101)]
ans_count = 0                                                         # 이하 반복문
for idx_box in range(4):                                              # 각 박스별
    for dx in range(box_list[idx_box][0], box_list[idx_box][2]):      # 박스 x 좌표 별
        for dy in range(box_list[idx_box][1], box_list[idx_box][3]):  # 박스 y 좌표 별
            if board[dx][dy] == 0:                                    # 아직 안 밟은곳
                ans_count += 1                                        # 답지 + 1
                board[dx][dy] = 1                                     # 밟은 곳으로..
print(ans_count)