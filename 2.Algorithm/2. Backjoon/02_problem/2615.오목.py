# BOJ.
# 설계 의도: 조건에 맞는 실행
# 1. 검은돌이 1, 흰돌이 2, 다 돌면 0 그대로 출력.
# 2. 결과가 1 이상이면 처음에 찾아서 멈춘 그 좌표 출력하도록 설정.
# 개선점:
def checking(x, point):
    check = [0, 0, 0]
    for row_check in range(point-2, point+3):
        check[board[x][row_check]] += 1
    else:
        position = check.index(5)
        if position:
            position = check.index(max(check))
            if point - 3 < 0:
                if board[x][point+3] != position:
                    return position
            elif point - 3 > N:
                if board[x][point - 3] != position:
                    return position
            elif board[x][point+3] != position and board[x][point - 3] != position:
                return position


N = 19
board = [list(map(int, input().split())) for _ in range(19)]
re_board = list(map(list, zip(*board)))
winner = 0
answer = (0, 0)
row = 2
flag = True
while row < N-2 and flag:
    if not winner:
        for col in range(2, N-2):
            if 4 <= col + 4 < N and flag:
                if checking(row, col):
                    answer = (row, col)
                    flag = False
                    break
            if 4 <= row + 4 < N and flag:
                if checking(col, row):
                    answer = (col, row)
                    flag = False
                    break



    x += 1

if winner:
    print(winner)
    print(answer[0]+1, answer[1]+1)
else:
    print(winner)
# x+cross_r, y-cross_r