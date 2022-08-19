# 1979. 어디에 단어가 들어갈 수 있을까
T = int(input())
for case_num in range(1, T+1):                    #
    N, K = map(int, input().split())              #
    size = N                                      # 퍼즐 판의 사이즈
    target_length = K                             # 목표 문자의 길이
    length_list = []                              # 각 공간의 길이를 저장
    board = [list(map(int, input().split())) for _ in range(size)]

    for x in range(size):                         #
        storage = 0                               # 각 행의 연결된 칸 개수 리셋
        cross_storage = 0                         # 각 열의 연결된 칸 개수 리셋
        for y in range(size):                     #
            if board[x][y] == 0:                  # 해당 위치값이 0 이면
                length_list += [storage]          # 현재 쌓아놓은 스토리지 반환
                storage = 0                       # 리셋
            elif board[x][y] == 1:                # 해당 위치값이 1이면
                storage += 1                      # 현재 스토리지 +1
            if board[y][x] == 0:                  # 열에서도 똑같이 반복
                length_list += [cross_storage]    #
                cross_storage = 0                 #
            elif board[y][x] == 1:                #
                cross_storage += 1                #
            if y == (size-1):                     # 행이건 열이건, 지금 움직이는 값은 y
                length_list += [storage]          # 끝에 도달하면 현재 스토리지 반환
                length_list += [cross_storage]    # 행의 값도 똑같이 반환

    ans = length_list.count(target_length)        # count 로 타겟 값의 개수 반환
    print(f'#{case_num} {ans}')
