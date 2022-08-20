import sys
sys.stdin = open("input.txt", "r")

# 상 0 하 1 좌 2 우 3 상은 없으니 하,좌,우만 고려


def laddering(input_0, input_1, go_dir, count):                 # 재귀용 함수 (X좌표, Y좌표, 방향)
    global count_list
    dX = input_0                                                # dX 좌표
    dY = input_1                                                # dY 좌표
    cur_dir = go_dir                                            # 방향 설정
    while dX < 100:                                             # 밑으로 뚫고 나가지 않도록 범위 설정
        if cur_dir == 1:                                        # < 방향이 [아래] > 일 경우
            if board[dX][dY + 1] == 1:                          # 오른쪽 길이 있으면
                cur_dir = 3                                     # 방향을 오른쪽으로 바꾸고
                dY += 1                                         # dY 좌표 +1
            elif board[dX][dY - 1] == 1:                        # 왼쪽 길이 있으면
                cur_dir = 2                                     # 방향을 왼쪽으로 바꾸고
                dY -= 1                                         # dY 좌표 -1
            elif board[dX][dY + 1] == 2:                        # 만약 내 아래에 2가 있다면
                return True                                     # True 반환
            elif board[dX + 1][dY] == 1:                        # 이도저도 아니면 아래로 내려가고
                dX += 1                                         # dX 좌표 +1
        elif cur_dir == 2:                                      # < 방향이 [왼쪽] > 일 경우
            if board[dX][dY + 1] == 2:                          # 만약 내 아래에 2가 있다면
                return True                                     # True 반환
            elif board[dX + 1][dY] == 1:                        # 내 아래에 길이 있으면
                cur_dir = 1                                     # 방향을 아래로 바꾸고
                dX += 1                                         # dX 좌표 +1
            elif board[dX][dY - 1] == 1:                        # 내 왼쪽에 길이 있다면
                dY -= 1                                         # dY 좌표 +1
        elif cur_dir == 3:                                      # < 방향이 [오른쪽] > 일 경우
            if board[dX][dY + 1] == 2:                          # 만약 내 아래에 2가 있다면
                return True                                     # True 반환
            elif board[dX + 1][dY] == 1:                        # 내 아래에 길이 있으면
                cur_dir = 1                                     # 진행방향 아래로 바꾸고
                dX += 1                                         # dX 좌표 +1
            elif board[dX][dY + 1] == 1:                        # 내 오른쪽에 길이 있다면
                dY += 1                                         # 오른쪼그로 마저 진행
        return laddering(dX, dY, cur_dir, count + 1)            # 재귀용 함수에 집어넣기
    if dX == 100:                                               # 100층에 도착했다면
        count_list += [count]


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
    count_list = []
    flag = False                                                # 도착점 (2) 찾았는지 여부
    for ladder_start in start_point:                            # 각 스타트 지점에서 함수 시작
        start_dX = ladder_start[0]                              #
        start_dY = ladder_start[1]                              #
        flag = laddering(start_dX, start_dY, 1, 0)                 # 2에 도착하면 flag = True
    if flag:                                                #
        print(f'#{case_num} {min(count_list)}')                    # flag가 True면 프린트 이후 break
        break
