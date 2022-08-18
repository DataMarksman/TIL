# 1209. sum

T = 10
for tc in range(1,11):
    case_num = int(input())
    board = [list(map(int,input().split()))\
            for _ in range(100)]
    max_ver = 0
    max_col = 0
    max_sum = 0
    for y in range(100):
        count_col = 0
        count_ver = 0
        for x in range(100):
            count_col += board[x][y]
            count_ver += board[y][x]
            if count_col > max_col:
                max_col = count_col
            if count_ver > max_ver:
                max_ver = count_ver
    if max_ver > max_col:
        max_sum = max_ver
    else:
        max_sum = max_col
        
    max_cross = 0
    count_cross = 0
    for z in range(100):
        max_cross += board[z][z]
        count_cross += board[99-z][z]
    if count_cross > max_cross:
        max_cross = count_cross
    
    
    print(f'#{case_num} {max_sum}')
    
    
    
    
    
    