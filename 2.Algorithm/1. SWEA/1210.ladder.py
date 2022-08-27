# 1210. ladder 1
# 설계: 그냥 가.

def laddering(input_0, input_1, go_dir):
    po_0 = input_0
    po_1 = input_1
    cur_dir = go_dir
    while po_0 < 99:
        if cur_dir == 1:
            if board[po_0][po_1 + 1] == 1:
                cur_dir = 3
                po_1 += 1
                return laddering(po_0, po_1, cur_dir)
            elif board[po_0][po_1 - 1] == 1:
                cur_dir = 2
                po_1 -= 1
                return laddering(po_0, po_1, cur_dir)
            elif board[po_0 + 1][po_1] == 2:
                return True
            elif board[po_0 + 1][po_1] == 1:
                po_0 += 1
                return laddering(po_0, po_1, cur_dir)
        elif cur_dir == 2:
            if board[po_0 + 1][po_1] == 2:
                return True
            elif board[po_0 + 1][po_1] == 1:
                cur_dir = 1
                po_0 += 1
                return laddering(po_0, po_1, cur_dir)
            elif board[po_0][po_1 - 1] == 1:
                po_1 -= 1
                return laddering(po_0, po_1, cur_dir)
        elif cur_dir == 3:
            if board[po_0 + 1][po_1] == 2:
                return True
            elif board[po_0 + 1][po_1] == 1:
                cur_dir = 1
                po_0 += 1
                return laddering(po_0, po_1, cur_dir)
            elif board[po_0][po_1 + 1] == 1:
                po_1 += 1
                return laddering(po_0, po_1, cur_dir)
    if po_0 == 99:
        if board[po_0][po_1] == 2:
            return True
        else:
            return False


T = 10
for tc in range(1, T + 1):
    case_num = int(input())
    board_input = [list(map(int, input().split())) for _ in range(100)]
    board = [[0]*102 for _ in range(100)]
    for cols in range(100):
        for rows in range(100):
            board[rows][cols+1] = board_input[rows][cols]
    start_point = []
    for starting in range(len(board[0])):
        if board[0][starting] == 1:
            start_point += [starting]
    flag = False
    for ladder_start in range(len(start_point)):
        input_start = int(start_point[ladder_start])
        flag = laddering(0, input_start, 1)
        if flag:
            print(f'#{case_num} {input_start-1}')
            break
