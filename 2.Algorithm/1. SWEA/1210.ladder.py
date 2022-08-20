T = 10                                                          #
for tc in range(1, T + 1):                                      # 
    case_num = int(input())                                     # 
    board_input = [list(map(int, input().split()))\
                    for _ in range(100)]
    board = [[0]*102 for _ in range(100)]                       # 보드 양쪽에 0 만들어주기
    for cols in range(100):                                     # 
        for rows in range(100):                                 #
            board[rows][cols+1] = board_input[rows][cols]       #
    start_point = []                                            # 스타트 포인트 저장할 스톡
    for starting in range(100):                                 # 
        if board[0][starting] == 1:                             # 스타트 지점 반환
            start_point += [[0, starting]]                      #
    flag = False                                                # 도착점 (2) 찾았는지 여부
    for ladder_start in start_point:                            # 각 스타트 지점에서 함수 시작
        start_dX = ladder_start[0]                              #
        start_dY = ladder_start[1]                              #
        flag = laddering(start_dX, start_dY, 1)                 # 2에 도착하면 flag = True
        if flag:                                                # 
            print(f'#{case_num} {start_dY}')                    # flag가 True면 프린트 이후 break
            break
