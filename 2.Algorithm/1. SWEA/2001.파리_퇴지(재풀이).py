# SWEA 2001. 파리 퇴치

for case_num in range(1, int(input())+1):
    N, M = map(int, input().split())
    wide = N
    size = M
    max_kill = 0
    board = [list(map(int, input().split())) for _ in range(N)]
    for x in range(wide-size):
        for y in range(wide-size):
            hit_count = int(0)
            for r in range(size):
                for c in range(size):
                    hit_count += int(board[x + r][y + c])
            if hit_count > max_kill:
                max_kill = hit_count
    print(f'#{case_num} {max_kill}')


