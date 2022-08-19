# 1961.숫자 배열 회전
# 파이참이 자꾸 틀렸다고 하는데, 값은 맞게 나오는 상황. 기묘..
T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    n = int(N-1)
    board = [list(map(int, input().split())) for _ in range(N)]
    board_90 = [[0]*N for _ in range(N)]
    board_180 = [[0]*N for _ in range(N)]
    board_270 = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            board_90[y][n-x] = str(board[x][y])
            board_180[n-x][n-y] = str(board[x][y])
            board_270[n-y][x] = str(board[x][y])
    print(f'#{case_num}')
    for cols in range(N):
        tmp_90 = ''.join(board_90[cols])
        tmp_180 = ''.join(board_180[cols])
        tmp_270 = ''.join(board_270[cols])
        print(tmp_90, tmp_180, tmp_270)
