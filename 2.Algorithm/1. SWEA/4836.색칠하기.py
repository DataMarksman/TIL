# 4836. 색칠하기

T = int(input())
for case_num in range(1, T + 1):            # 
    N = int(input())                        #
    board = [[0]*10 for _ in range(10)]     # 10 x 10 보드 판 만들기
    color_list = [list(map(int, input()\
            .split())) for _ in range(N)]   # 컬러 리스트 전부 받기
    red_list = []                           # 레드 리스트 스톡 배당
    blue_list = []                          # 블루 리스트 스톡 배당
    violet_count = 0                        # 보라색 카운트
    for lines in color_list:                # 컬러 리스트에서
        if lines[4] == 1:                   # 빨간색 칠하는 리스트 빼기
            red_list += [lines]             #
        elif lines[4] == 2:                 # 파란색 칠하는 리스트 빼기
            blue_list += [lines]            #
    for red in range(len(red_list)):        # 각 레드 리스트에서
        dx = red_list[red][0]               # 시작 x 좌표
        dy = red_list[red][1]               # 시작 y 좌표
        ex = red_list[red][2]               # 끝 x 좌표
        ey = red_list[red][3]               # 끝 y 좌표
        for x in range(dx, ex+1):           # 빨간 색을 칠한 범위를
            for y in range(dy, ey+1):       # 
                board[x][y] = 1             # 1로 바꾸기

    for blue in range(len(blue_list)):      # 각 파란 리스트에서
        dr = blue_list[blue][0]             # 시작 x 좌표
        dc = blue_list[blue][1]             # 시작 y 좌표
        er = blue_list[blue][2]             # 끝 x 좌표
        ec = blue_list[blue][3]             # 끝 y 좌표
        for r in range(dr, er+1):           # 블루 리스트로 돌면서
            for c in range(dc, ec+1):       # 
                if board[r][c] == 1:        # 밟는 장소가 1이라면
                    violet_count += 1       # 보라색 카운트 + 1
                board[r][c] = 2             # 보라색으로 바뀌면 2로 바꿈
    print(f'#{case_num} {violet_count}')    # 보라색 중복 카운팅 방지
