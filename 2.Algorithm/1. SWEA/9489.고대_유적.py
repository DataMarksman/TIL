# 9386. 연속한 1의 개수
T = int(input())
for case_num in range(1, T+1):
    N, M = tuple(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    re_board = list(map(list, zip(*board)))
    max_length = 0
    for x in range(N):
        ver_len_count = 0
        for y in range(M):
            if board[x][y] == 1:
                ver_len_count += 1
            if board[x][y] == 0 or y == M-1:
                if ver_len_count > max_length:
                    max_length = int(ver_len_count)
                    ver_len_count = 0
                else:
                    ver_len_count = 0
    for r in range(M):
        col_len_count = 0
        for c in range(N):
            if re_board[r][c] == 1:
                col_len_count += 1
            if re_board[r][c] == 0 or c == N - 1:
                if col_len_count > max_length:
                    max_length = int(col_len_count)
                    col_len_count = 0
                else:
                    col_len_count = 0

    print(f'#{case_num} {max_length}')
