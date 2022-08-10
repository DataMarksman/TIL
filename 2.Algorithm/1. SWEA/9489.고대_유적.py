# 9386. 연속한 1의 개수

T = int(input())
for case_num in range(1,T+1):
    N, M = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    max_len_col = 0
    max_len_ver = 0
    for y in range(M):
        count_col = 0
        for x in range(N):
            if board[x][y] == 1:
                count_col += 1
                if count_col > max_len_col:
                    max_len_col = count_col
            elif board[x][y] == 0:
                count_col = 0
    
    for r in range(N):
        count_ver = 0
        for c in range(M):
            if board[r][c] == 1:
                count_ver += 1
                if count_ver > max_len_ver:
                    max_len_ver = count_ver
            elif board[r][c] == 0:
                count_col = 0
                
    if max_len_col > max_len_ver:
        print(f'#{case_num} {max_len_col}')
    else:
        print(f'#{case_num} {max_len_ver}')