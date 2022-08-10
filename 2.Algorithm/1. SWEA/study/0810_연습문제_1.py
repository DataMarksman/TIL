# 2차원 배열 연습 문제
# 뭔가 귀찮아져서 그냥 삼항연산으로 퉁쳤습니다. 내장함수 안썼으니 인정인가요?
T = int(input())
for case_num in range(1,T+1):                                                    # 
    N = int(input())                                                             #
    board = [[0]*(N+2) for _ in range(N+2)]                                      # 사방을 0 벽으로 둘러싸기 위해 N+2 크기의 보드 제작
    for input_line in range(1,N+1):                                              # 1 ~ N 좌표로 값을 받아서 저장하면
        lines = list(map(int,input().split()))                                   # 사방에 0으로된 벽 안쪽으로 값이 입력된다.
        for numbers in range(1,N+1):                                             # board[0][~~] board[~~][0] board[N+1][~~] board[~~][N+1]
            board[input_line][numbers] = lines[numbers-1]                        # 위의 범위는 전부 0으로 된 벽이 된다.
    sum_stock = 0                                                                # 각 좌표의 상하좌우 합친걸 합치는 거라면, 처음부터 쌓자.
    for y in range(1,N+1):                                                       # 
        for x in range(1,N+1):                                                   # 0으로된 벽을 제외한 범위를 탐색하기 위해 1~N 돌립니다.
            up = (board[x][y] - board[x][y-1] if board[x][y-1] != 0 else 0)      # 현재 밟고 있는 곳의 위에 있는 좌표가 0 벽인지 확인하고 차이 반환
            down = (board[x][y] - board[x][y+1] if board[x][y+1] != 0 else 0)    # 현재 밟고 있는 곳의 아래에 있는 좌표가 0 벽인지 확인하고 차이 반환
            left = (board[x][y] - board[x-1][y] if board[x-1][y] != 0 else 0)    # 현재 밟고 있는 곳의 왼쪽에 있는 좌표가 0 벽인지 확인하고 차이 반환
            right = (board[x][y] - board[x+1][y] if board[x+1][y] != 0 else 0)   # 현재 밟고 있는 곳의 오른쪽에 있는 좌표가 0 벽인지 확인하고 차이 반환
            sum_stock += (up if up >= 0 else (-1)*up)                            # 음수면 -1 곱해서 바로 스톡에 저장
            sum_stock += (down if down >= 0 else (-1)*down)                      # 음수면 -1 곱해서 바로 스톡에 저장
            sum_stock += (left if left >= 0 else (-1)*left)                      # 음수면 -1 곱해서 바로 스톡에 저장
            sum_stock += (right if right >= 0 else (-1)*right)                   # 음수면 -1 곱해서 바로 스톡에 저장
    print(f'#{case_num} {sum_stock}')