# 1974. 스도쿠 검증 (이전 풀이)
# 설계 의도: 한번에 가로,세로,박스형 값을 전부 체크하자.
# 핵심: [board[(dy//3)+3*(dx//3)][(dy%3)+3*(dx%3)]] -> 3x3 박스 체크용

# import sys
# sys.stdin = open("input_sudoku.txt", "r")

T = int(input())
for case_num in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for dx in range(9):
        if ans:
            set_ver = set()
            set_col = set()
            set_box = set()
            for dy in range(9):
                set_ver.add(board[dx][dy])
                set_col.add(board[dy][dx])
                set_box.add(board[(dy // 3) + 3 * (dx // 3)][(dy % 3) + 3 * (dx % 3)])
            if len(set_ver) != 9 or len(set_col) != 9 or len(set_box) != 9:
                ans = 0
    print(f'#{case_num} {ans}')

